#! /bin/bash

echo "Content-Type: text/html"
echo ""
echo "<html>"
echo "<p>Your drink is being processed</p>"
sudo -S python /home/pi/piscripts/bottles/wiskey.py -a oneoz >> /var/log/drinkmixer.log & 
sudo -S python /home/pi/piscripts/bottles/vodka.py -a oneoz >> /var/log/drinkmixer.log & 
echo "</html>"