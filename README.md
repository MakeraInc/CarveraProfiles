This repository manages Carvera profiles such as machine/tool bits settings and post processors for different software[CarveraProfiles](https://www.makera.com). 

Checkout the [Releases Page](https://github.com/MakeraInc/CarveraProfiles/releases) for downloads.

----

# Fusion 360

## Install PostProcessor
1. Start Fusion 360.

2. Navigate to the Manufacture Workspace.

![F360 Workspace](/img/F360-Workspace.png)

3. Under the Manage group, select the Post Library button.

![F360 Post Library](/img/F360-Post-Library.png)

4. Navigate to the "My Posts->Local" folder.

5. Click the "Import" button.

![F360 Post Import](/img/F360-Post-Import.png)

6. Select the "Carvera.cps" file and finish the importing.

## Install Machine
1. Under the Manage group, select the Machine Library button.

![F360 Machine Library](/img/F360-Machine-Library.png)

2. Navigate to the "My Machines->Local" folder.

3. Click the "Import" button.

![F360 Machine Import](/img/F360-Machine-Import.png)

4. Select the "Carvera 3-axis.mch" file and finish the importing.

5. Repeat importing the "Carvera 4-axis.mch" file.

## Install Tool Library
1. Under the Manage group, select the Post Library button.

![F360 Tool Library](/img/F360-Tool-Library.png)

2. Navigate to "All->Local".

3. Right click the "Local" folder and click the "New folder" button, create a new folder named "Carvera Tools".

4. Right click the new folder and then click the "Import libraries" button

![F360 Tool Import](/img/F360-Tool-Import.png)

5. Select the "Example Tools.tools, Spare Tools.tools, PCB Tools.tools" files and finish the importing.

## Using Fusion360 Profiles
1. When creating setups, select the "Makera Carvera 3-axis" or "makera Carvera 4-axis" machine.

![F360 Setup](/img/F360-Setup.png)

2. When doing post process, select the Makera Carvera machine and Carvera post file.

![F360 Post Process](/img/F360-Post-Process.png)




----
# VCarve Desktop

## Install PostProcessor
1. Start VCarve Desktop

2. Navigate to the “Machine” menu and click “Post-Processor Management”.

3. Click the “Install Post-Processor” button.

4. Select and import the “Carvera ATC (mm) (!.cnc).pp” file.

5. Repeat importing the “Carvera Wrap X2A ATC (mm) (!.cnc).pp” file and “Carvera Laser (mm) (!.cnc).pp" file.

## Create Machine
1. Navigate to the “Machine” menu and click “Machine Configuration Management”.

2. Click the “Add a custom machine” button.

3. Fill in the information as shown below.

4. Select the post processors just imported and set the “Carvera ATC (mm)(*.cnc)” as default.

5. Click “Apply” then “OK”  to save the configuration.

## Install Tool Database
1. Navigate to the “Toolpaths” menu and click “Tool Database”.

2. Click the “Import a tool database” button.

3. Select the “CarveraTools.vtdb” file.

4. Click the “Merge” button on the popup confirm dialog and finish the import.

## Using VCarve Desktop Profiles
When saving Tool paths, select Carvera Desktop CNC Machine and a suitable post processor for your job.



----
# LightBurn

## Setup Device
1. Start LightBurn.

2. Click the “Device” button.

3. Click the “Import” button in the popup dialog.

4. Select the “LightBurn.lbdev” file and finish importing the Makera Carvera device.

## Using LightBurn Profiles
When saving GCode, select “Makera” as the current device.



