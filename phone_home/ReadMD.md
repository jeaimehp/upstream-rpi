# Discord Situation Report Communicator

## Author: Miles Hernandez
### Email: amillionmiels@gmail.com
### Discord: Mvlti#3338

## Description
Records Host Information, Storage Info, Time Running, and Date of Raspberry PIs and reports the situation report to a Discord Server both autonomously and on command.
Additional Features to be implemented include an indicator of the strength of the wireless signal and a number of the stored audio files onboard the RPI.

The most important variable to alter for personal use is the Discord Token for the bot delivering the sitrep. When creating your own Discord Bot, call upon its individual Token, which can be viewed from the Build-A-Bot screen.

pythonSitrepRequirements.txt lists each import requirement for DiscordSitrep to run, and sitrepSetup.bash should automatically install the required files when run.

Hidden file .gitignore hides the file holding the private Token
Hidden file .env contains the private Token.
