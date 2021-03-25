# !/bin/bash 
apt-get update
sudo su -
useradd ubuntu
sudo apt-get install build-essential xrdp xfce4 xfce4-terminal xfce4-goodies xorg dbus-x11 x11-xserver-utils software-properties-common apt-transport-https wget -y
# Setting up XRDP
sudo sed -i.bak '/fi/a #xrdp multiple users configuration \n xfce-session \n' /etc/xrdp/startwm.shsudo ufw allow 3389/tcp
sudo /etc/init.d/xrdp restart
sudo systemctl restart xrdp
sudo apt-get install build-essential libcurl4-gnutls-dev libxml2-dev libssl-dev firefox -y
sudo ufw allow 3389
# Setting up VSCode
sudo apt update
sudo apt install software-properties-common apt-transport-https -y
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
sudo sh -c 'echo "deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
sudo apt update
sudo apt install code -y
