# ERSC_Launcher_Auto_Updater
 Auto Updater for Elden Ring seamless CoOp
By Lucas Eng

This is a fully built out auto runner for Elden Ring seamless Co-Op.


Steps:

Take the zip file (ersc_auto_update.zip), extract all of the elements, and put those elements into your game folder where you would
normally put the ersc_launcher. Run the executable which in the first time will prompt you to enter your seamless Co-Op password.
The password lives in the cooppassword file within text_resources. After that is entered, it will automatically run the ersc_launcher,
and you will NOT have to enter the password again. 

This script functions by downloading the latest version of ersc_launcher via github, and putting it within the directory the executable is in,
and writing the coop password into the corresponding location. 

Should a new update be released, upon running the new executable it will remove your current version of ersc_launcher, install the new one, replace 
your password, and run it. 



For anyone who wishes to tinker with it, the:
'''
make
make clean
'''
commands create the zip file required. 
