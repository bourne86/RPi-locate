# My RPi-Zero-W tracker
## Initial install
Use 2019-06-20-raspbian-buster-lite.img on RPi-Zero-W https://downloads.raspberrypi.org/raspbian_lite_latest</br>
Also TL-WN722N adapter </br>
## Setup
sudo apt-get update </br>
sudo apt-get upgrade </br>
sudo apt-get install python-pip </br>
sudo pip install requests </br>
sudo pip install dropbox </br>
sudo pip install pathlib </br>
sudo apt-get install git </br>
sudo apt-get install libssl-dev autoconf automake libtool libnl-3-dev libnl-genl-3-dev libssl-dev libsqlite3-dev libpcre3-dev shtool libpcap-dev screen </br>
wget https://download.aircrack-ng.org/aircrack-ng-1.5.2.tar.gz </br>
tar -zxvf aircrack-ng-1.5.2.tar.gz </br>
cd aircrack-ng-1.5.2 </br>
autoreconf -i </br>
./configure --with-experimental </br>
make </br>
sudo make install </br>
sudo ldconfig </br>
## Do this once
sudo airodump-ng-oui-update </br>
## Add to startup
sudo nano /etc/rc.local </br>
sudo airmon-ng start wlan1 </br>
## Edit Cron
sudo crontab -e </br>
*/1 * * * * /home/pi/ip-logger.py </br>
