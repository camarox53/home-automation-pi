#! /bin/bash

sudo apt-get udpdate

sudo touch /var/log/drinkmixer.log
sudo chmod 644 /var/log/drinkmixer.log
sudo chown www-data:www-data /var/log/drinkmixer.log

