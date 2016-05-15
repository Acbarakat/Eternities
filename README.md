# Eternities

## Getting Started
Download [Python 2.7](https://www.python.org/) - 3.X should also work but might require import fixes

To install all required auxiliary libraries use the following scripts depending on your OS/Environment

Windows:
 ```
 requirements_win.bat
 ```

Linux:
 ```
 sudo requirements_lin.sh
 ```

 An experimental profiling tool for the kv lang is also included. You can activate it by setting the environment variable KIVY_PROFILE_LANG=1. It will then generate an html file named builder_stats.html.

## Creating a Linux VM (to compile for mobile)

### Prerequisites
- Download and install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- Download and install [VirtualBox VM VirtualBox Extension Pack](https://www.virtualbox.org/wiki/Downloads)
- Download and run [Ubuntu VM](https://virtualboxes.org/images/ubuntu/)

### Getting the VM prepared
After installing VitualBox, the Extension Pack, and running the ubuntu OVA file, go to the VM settings and adjust the ram, cpu cores, etc. how you see if. The following are things that must be set:
- **Settings > USB** : make sure Enable USB Controller is checked. If you have your mobile devices connected, you can set the filter to just those devices. This will automatically give those devices to the VM rather than the manual step of going to **Devices > USB > YOURRMOIBLEDEVICE** whenever you launch the VM
- **Settings > Shared Folders** : Add the file path your working directory to the Machines Folders. Check auto-mount. I would also add Read-Only as you should not be compiling directory from your working directory. Instead you must copy to the local VM disk. If your working directory is within the VM you can ignore this step.

### Connecting to the share folder
To access your Shared Folders you must do the following
```
#This you only need to do one time
sudo apt-get install virtualbox-guest-dkms
sudo usermod -a -G vboxsf $USER

#This you must do on every startup unless you edited the auto-mount file (SHARENAME variable should be whatever your sharefolder name was.)
sudo mount -t vboxsf -o uid=$UID,gid=$(id -g) $SHARENAME /mnt/$SHARENAME
```

### Syncing the workspace
You should always copy the project to the local vm and never try to build out of the share folder. Permissions issues can and will arise. Here is an example of a good sync locally:
```
#SHARENAME is the folder you setup
#SHAREPROJECT is the working project dir

rsync -arvzI /mnt/$SHARENAME/$SHAREPROJECT /home/ubuntu/Desktop --exclude-from="Exclude.txt"
```

Where the Exclude.txt is:
```
*/.vs
*/.git*
*/.buildozer
*.pyproj
*.pyc
*.sln
*.MD
*.bat
```

### Installing/Updating the project prerequisites
Once you have copied/synced locally and wish to try it out in the android device. You have to run the following:
```
sudo requirements_lin.sh
```

