# PhoneLayoutGUI
## Description
This is a utility for configuring the button layouts on these select phone models
  + Aastra 6737i
  + Aastra 6739i
  + Yealink EXP40 Module
  + Yealink T48G
  + Yealink T46G
  + Yealink T42S
  + Yealink T41P

This tool exists to make the task of editing button layouts easy. Without this utility, editing the button layouts on the listed phone models requires you to go line by line through a text file. A simple change like moving a button to the first position requires the user to manually update the index of each button in the list. This task can become very time consuming when working with layouts that contain many buttons. With this utility, moving a button to a new position will automatically update the index of each button for the user, making a once daunting task trivial. This tool allows edits of different attributes of each button by double clicking on a button you wish to edit. You may also add/delete buttons from the list with ease.

## How to use
1. Download project locally and find Driver.py file
2. After running Driver.py you will be prompted to select the model of phone you wish to edit
3. Once you select the model you wish to edit, you can create a new config, or paste an existing config into the text field
4. A new window will be created that contains the config you entered. You may now double click buttons to edit them, drag and drop them to move the buttons around or delete them, and add buttons using the add button
5. Once you are happy with the changes made, click continue and the new config text will be displayed. You may now copy the new config text to update the config on your phone. 

