# BioThings Plugin Template
VSCode Dev Container based environment for developing BioThings plugins

## Usage

### 0. Install prerequisite software
You will need:
- Docker with Docker Compose (installing Docker Desktop is sufficient)
- Visual Studio Code
- [Docker Extension for VSC](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)
- ["Remote - Containers" Extension for VSC](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

### 1. Generate a new repo from the template

On GitHub, just click the big green button "Use this template". You can also download this and copy all the files (except this README.md file), make sure you copy the files and directories whose names begins with "." (a dot).

### 2. Update files to reflect your plugin

Open up the newly generated repository in Visual Studio Code, then:

- In `.devcontainer/devcontainer.json` set the `name` field to your liking.
- And then, set the `workspaceFolder` to `/data/biothings/plugins/{name-of-your-plugin}`
- In `.devcontainer/docker-compose.yml` set the second item in `services.biothings.volumes` to reflect your plugin path, like `..:/data/biothings/plugins/{name-of-your-plugin}`
- Then, in `services.biothings.build.args`, set `API_NAME` and `API_GIT` to relfect the flavor of BioThings Hub you prefer. Possible combinations include:

        - vanilla-hub: https://github.com/biothings/biothings_studio.git
        - mychem.info: https://github.com/biothings/mychem.info.git
        - mygeneset.info: https://github.com/biothings/mygeneset.info.git
        - outbreak.info: https://github.com/outbreak-info/outbreak.api.git
        - etc.

- Finally, in the command palette (under the Menu in VSC: View - Command Palette), choose "Remote Containers: Rebuild and Reopen in Container" to re-launch VSC connecting to the container.
- Wait until it is done (it may take longer to install the VSC extensions in the background), in the left side bar, choose Run & Debug, and you can launch BioThings Hub with your plugin.
- Now you can develop your plugin in VSC.
