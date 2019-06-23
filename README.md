# My RPi-Zero-W tracker
sudo apt-get update </br>
sudo apt-get upgrade </br>
sudo apt-get install python-pip </br>
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
ldconfig </br>
