# file.io tool for MacOS users

## What is file.io?

[file.io](https://file.io) is a web service where you can upload and share a file anonymous and secure.

As stated in their site:

```
Simply upload a file, share the link, and after it is downloaded,
the file is completely deleted. For added security, set an expiration on the file and it is
deleted within a certain amount of time, even if it was never downloaded.

All files are encrypted when stored on our servers.
```

## How to use it?

1) Select the items you want to upload
2) Press `cmd + u` (or the command you have assigned)
3) URL of the file and key will appear in a blank TextEdit window.

## Added security and privacy layers

We added two more layers:

- We use TOR for uploading the files
- Files are compressed and encrypted using AES CBC 256 (built-in from 7z and using a random 32 byte key)

## Instructions

### Set Automator script

1) Open Automator
2) Create a new quick action with no input
3) Paste contents of `fileio.applescript` (you might want to change the way the python script is called or specify the python binary directly)
4) Save your script

### Create shortcut

1) Open System Preferences > Keyboard > shortcuts
2) On the left panel, select Services
3) Enable your quick action and assign a shortcut, for example `cmd + u`

### Grant Finder full disk access

1) Open System Preferences > Security and Privacy
2) On the left panel, select Full Disk Access
3) Add Finder (It is in `/System/Library/CoreServices`)

### Place the python script

1) Place the python script in a path like `/usr/local/bin`

## Supported platforms

Only MacOS is supported, but PR for other platforms are welcome.


