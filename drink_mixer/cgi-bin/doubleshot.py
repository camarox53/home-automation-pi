#! /bin/bash

echo "Content-Type: text/html"
echo ""
echo "<html>"
echo "<p>Pumping has started</p>"
sudo -S python /home/pi/piscripts/bottles/wiskey.py -a oneoz > /dev/null & 
sudo -S python /home/pi/piscripts/bottles/vodka.py -a oneoz > /dev/null & 
echo "</html>"
