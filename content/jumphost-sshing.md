---
title: SSHing into a Remote Host, Through a Jumphost
tags:
  - ssh
  - ngrok
  - walkthrough
date: 2023-04-15
slug: jumphost-sshing
---

1. Ensure the requirements:
    - An architecture with 3 hosts: one for development, one for production, and one jumphost;
    - An account `<USERNAME>` created on the production host;
    - An SSH server installed on the production host, on port 22;
    - A public SSH key linked attached to the account;
    - A private SSH key placed on the development host, on `<PATH_TO_PRIVATE_KEY>`; and
    - A project folder on the development host, on `<PATH_TO_SYNCED_FOLDER>`.
2. Login to ngrok, eventually with SSO (e.g. GitHub).
3. After login, you will be redirected to the setup page. Copy the link to the binary (not. `<BINARY_LINK>`) specific to the production host's architecture.
4. Login to the production host, and download the binary with `wget <BINARY_LINK>`.
5. Authenticate yourself to ngrok: `./ngrok config add-authtoken <ACCOUNT_TOKEN>`.
6. Expose the SSH server using ngrok: `./ngrok tcp 22`.  This step will give you a URL respecting the structure `tcp://<NGROK_SUBDOMAIN>:<PORT>`.
7. In the Visual Studio Code installed on the development host, install the SFTP extension.
8. In the folder you want to sync, create the file `.vscode/sftp.json` with the content inserted on the end on the list.
9. In the IDE, run the command "*SFTP: Sync Local -> Remote*" to upload the initial state of the project folder.
10. Furthermore, once you save a file in your project's folder, it will be automatically updated on the remote host too.

```json
{
    "name": "Development Host",
    "host": "<NGROK_SUBDOMAIN>",
    "protocol": "sftp",
    "port": <PORT>,
    "username": "<USERNAME>",
    "privateKeyPath": "<PATH_TO_PRIVATE_KEY>",
    "remotePath": "<PATH_TO_SYNCED_FOLDER>",
    "uploadOnSave": true,
    "useTempFile": false,
    "openSsh": false,
    "ignore": [".vscode"]
}
```
