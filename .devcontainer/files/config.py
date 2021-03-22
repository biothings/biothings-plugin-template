from config_hub import *
from biothings.utils.loggers import setup_default_log
import os
import urllib.parse

src_parsed = urllib.parse.urlparse(os.environ.get('SRC_URI'))
target_parsed = urllib.parse.urlparse(os.environ.get('TARGET_URI'))
hub_parsed = urllib.parse.urlparse(os.environ.get('HUB_URI'))
api_name = "__REPLACE_WITH_API_NAME"

if not os.path.isfile('/data/biothings/ssh_host_key'):
	if os.path.exists('/data/biothings/ssh_host_key'):
		raise FileExistsError("/data/biothings/ssh_host_key exists but is not a regular file")
	
	from cryptography.hazmat.primitives.asymmetric import rsa as pk
	from cryptography.hazmat.primitives import serialization as crypto_ser

	print("Generating SSH Keys for BioThings Hub...")
	privkey = pk.generate_private_key(65537, 2048)
	with open('/data/biothings/ssh_host_key', 'wb') as f:
		f.write(
			privkey.private_bytes(
				crypto_ser.Encoding.PEM, 
				crypto_ser.PrivateFormat.OpenSSH, 
				crypto_ser.NoEncryption()
			)
		)
	pubkey = privkey.public_key().public_bytes(crypto_ser.Encoding.OpenSSH, crypto_ser.PublicFormat.OpenSSH)
	with open('/data/biothings/ssh_host_key.pub', 'wb') as f:
		f.write(pubkey)
	print("SSH Key has been generated, Public Key:\n")
	print(pubkey.decode('ASCII'))
	print()
	del privkey, pubkey, crypto_ser, pk

DATA_ARCHIVE_ROOT = f'/data/biothings/datasources'
DATA_PLUGIN_FOLDER = f'/data/biothings/plugins'
DATA_UPLOAD_FOLDER = f'/data/biothings/dataupload'

DIFF_PATH = f"/data/biothings/diff"
RELEASE_PATH = f"/data/biothings/release"
CACHE_FOLDER = f"/data/biothings/cache"
ES_BACKUPS_FOLDER = f"/data/biothings/esbackup"

LOG_FOLDER = f"/data/biothings/logs"
logger = setup_default_log("hub", LOG_FOLDER)

RUN_DIR = f'/data/biothings/run'

DATA_SRC_SERVER = src_parsed.hostname or 'localhost'
DATA_SRC_PORT = src_parsed.port or 27017
DATA_SRC_DATABASE = os.environ.get('SRC_DB', 'biothings_src')
DATA_SRC_SERVER_USERNAME = urllib.parse.unquote(src_parsed.username) if src_parsed.username else ''
DATA_SRC_SERVER_PASSWORD = urllib.parse.unquote(src_parsed.password) if src_parsed.password else ''

DATA_TARGET_SERVER = target_parsed.hostname or 'localhost'
DATA_TARGET_PORT = target_parsed.port or 27017
DATA_TARGET_DATABASE = os.environ.get('TARGET_DB', 'biothings_target')
DATA_TARGET_SERVER_USERNAME = urllib.parse.unquote(target_parsed.username) if target_parsed.username else ''
DATA_TARGET_SERVER_PASSWORD = urllib.parse.unquote(target_parsed.password) if target_parsed.password else ''

# FIXME: deal with other uri later
assert hub_parsed.scheme == 'mongodb'
DATA_HUB_DB_DATABASE = os.environ.get('HUB_DB', 'biothings_hub')
HUB_DB_BACKEND = {
		"module" : "biothings.utils.mongo",
		"uri" : os.environ.get('HUB_URI', 'mongodb://localhost:27017'),
    }

CONFIG_READONLY = False

# FIXME: deal with the version issue
# At least for BIOTHINGS_VERSION, it is trying to use the git repo version
# which does not seem to make sense
BIOTHINGS_VERSION = 'fixme'

# SSH port for hub console
HUB_SSH_PORT = 7022
HUB_API_PORT = 7080

# Hub name/icon url/version, for display purpose
HUB_NAME = f"Studio for {api_name}"
if api_name in ('mychem.info', 'myvariant.info', 'mygene.info'):
	HUB_ICON = f"http://biothings.io/static/img/{api_name.rstrip('.info')}-logo-shiny.svg"
HUB_VERSION = "master"

USE_RELOADER = True # so no need to restart hub when a datasource has changed

MAX_QUEUED_JOBS = 1

# cleanup config namespace
del os, urllib, src_parsed, target_parsed, hub_parsed, api_name, setup_default_log