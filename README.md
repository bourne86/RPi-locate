# My RPi-Zero-W tracker
## Initial install
Use 2019-04-08-raspbian-stretch-lite.img on RPi-Zero-W </br>
Also TL-WN722N adapter </br>
## Setup
sudo apt-get update </br>
sudo apt-get upgrade </br>
sudo apt-get install python-pip </br>
pip install requests </br>
pip install dropbox </br>
pip install pathlib </br>
sudo apt-get install git </br>
sudo apt-get install libssl1.1 libssl-dev build-essential autoconf automake libtool pkg-config libnl-3-dev libnl-genl-3-dev libssl-dev libsqlite3-dev libpcre3-dev ethtool shtool rfkill zlib1g-dev libpcap-dev screen </br>
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
## Then do this
sudo airmon-ng start wlan1 </br>
sudo timeout 10s airodump-ng wlan1mon --background 1 -w mydump -o csv </br>
## Edit Cron
sudo crontab -e
*/1 * * * * /home/pi/screen.py
*/1 * * * * /home/pi/edit.py
