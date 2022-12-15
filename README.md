This repository manages Carvera profiles such as machine/tool bits settings and post processors for different software[CarveraProfiles](https://www.makera.com). 

Checkout the [Releases Page](https://github.com/MakeraInc/CarveraProfiles/releases) for downloads.

----

# Fusion 360

## Install PostProcessor
1. Start Fusion 360.
2. Navigate to the Manufacture Workspace.
3. Under the Manage group, select the Post Library button.
![F360 Post Navi](/img/F360-Post-Navi.png)
4. Navigate to ‘My Posts->Local’ folder.
5. Click the ‘Import’ button.
![F360 Post Import](/img/F360-Post-Import.png)
6. Select the “Carvera.cps” file and finish the importing.

## Mac/OSX Installation
![Mac OS Setup](/img/Mac-Setup.png)

1. Double-click the dmg file to mount it 
3. Double-click the LightBurn.dmg file to mount it
4. Drag the CarveraController application into your applications folder
5. Launch CarveraController from the launcher as normal
6. You can now eject the DMG file (drag it to the trash bin)

### Solution for APP damage error
![APP Damage](/img/APP-Damage-Error.png)

If you encounter the warning as above, open the terminal window and execute the command below:

**sudo xattr -r -d com.apple.quarantine /Applications/CarveraController.app**

![APP Damage Solution](/img/APP-Damage-solution.png)

Reopen the CarveraController application, it should be OK now.

## Android Installation

1. Open your Android device's file explorer app. ...
2. Locate your APK file in your file explorer app and select it.
3. The APK installer menu will appear—tap Install. ...
4. Allow time for the app to install.
5. Tap Done or Open once the installation is complete.



