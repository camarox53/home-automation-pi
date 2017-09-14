#! /bin/bash

echo "Content-Type: text/html"
echo ""
echo "<html>"
echo "<p>Your request is being processed</p>"
sudo -S python /home/pi/piscripts/home_auto/scripts/lights_chill.py 
echo "</html>"
echo "<meta http-equiv='refresh' content='5; url=http://192.168.1.102'>"
