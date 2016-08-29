#! /bin/bash

echo "Content-Type: text/html"
echo ""
echo "<html>"
echo "<p>Your request is being processed</p>"
sudo -S python /home/pi/home_auto/scripts/test.py  >> /var/log/homeauto.log & 
#sudo -S python /home/pi/piscripts/home_auto/ >> /var/log/homeauto.log & 
echo "</html>"
