sudo apt-get update

sudo apt-get upgrade

sudo apt-get install python-pip

pip install dropbox

pip install pathlib

sudo apt-get install git

sudo apt-get install libssl1.1 libssl-dev build-essential autoconf automake libtool pkg-config libnl-3-dev libnl-genl-3-dev libssl-dev libsqlite3-dev libpcre3-dev ethtool shtool rfkill zlib1g-dev libpcap-dev screen

wget https://download.aircrack-ng.org/aircrack-ng-1.5.2.tar.gz

tar -zxvf aircrack-ng-1.5.2.tar.gz

cd aircrack-ng-1.5.2

autoreconf -i

./configure --with-experimental

make

make install

ldconfig
