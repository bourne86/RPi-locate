# My RPi-Zero-W tracker
## Initial install
Use 2019-06-20-raspbian-buster-lite.img on RPi-Zero-W https://downloads.raspberrypi.org/raspbian_lite_latest</br>
## Setup
sudo apt-get update </br>
sudo apt-get upgrade </br>
sudo apt-get install python-pip </br>
sudo pip install requests </br>
sudo pip install dropbox </br>
sudo pip install pathlib </br>
sudo apt-get install git </br>
## Edit Cron
sudo crontab -e </br>
*/1 * * * * /home/pi/analyser.py </br>
