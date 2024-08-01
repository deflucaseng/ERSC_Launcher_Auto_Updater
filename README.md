# ERSC_Launcher_Auto_Updater
 Auto Updater for Elden Ring seamless CoOp







Create new icon download that can be used.

Check for a first time temp use file, for which you can add the passcode. 


On click runs a python script that checks for an update, if so installs it in the appropriate place


pyinstaller --onefile --add-data "assets;assets" --add-data "text_resources;text_resources" --add-data "text_resources\cooppassword;." --add-data "text_resources\version;." scripts/launcher.py


firsttime.tmp
text_resources\version
text_resources\cooppassword
scripts\auto_updater.py
scripts\launcher.py
scripts\setup.py
assets\soyjack.png
