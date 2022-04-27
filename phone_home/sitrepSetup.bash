#!/bin/bash
echo "installing python modules"
sudo pip install -r pythonSitrepRequirements.txt

echo "Create .env file in this directory with Discord credentials (token)"

echo "Modifying /etc/rc.local to start the Discord server sitrep at startup"
sudo sed -i "/^exit 0/i\# Start Discord Server" /etc/rc.local
sudo sed -i "/^exit 0/i\sudo\ python3\ \/home\/pi\/upstream\/phone_home\/DiscordSitrep.py\ \&" /etc/rc.local
