#! /bin/bash

echo "Content-Type: text/html"
echo ""
echo "<html>"
echo "<p>Your drink is being processed</p>"
sudo -S python /home/pi/piscripts/drink_mixer/bottles/whiskey.py -a oneoz >> /var/log/drinkmixer.log & 
sudo -S python /home/pi/piscripts/drink_mixer/bottles/vodka.py -a oneoz >> /var/log/drinkmixer.log & 
echo "</html>"
echo "<meta http-equiv='refresh' content='5; url=http://192.168.1.102'>"
