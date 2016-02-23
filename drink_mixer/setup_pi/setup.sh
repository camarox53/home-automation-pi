#! /bin/bash
# Run with sudos

# Put SSH Keys into place on root and pi
wget https://launchpad.net/~cumorris/+sshkeys
mkdir -p /home/pi/.ssh
touch /home/pi/.ssh/authorized_keys
cp +sshkeys /home/pi/.ssh/authorized_keys
cp +sshkeys /home/root/.ssh/authorized_keys

# Update and install new Packages
apt-get update
apt-get install apache2 

# Setup log files
touch /var/log/drinkmixer.log
chmod 644 /var/log/drinkmixer.log
chown www-data:www-data /var/log/drinkmixer.log

# Give www-data sudos for scripts
cp ../files/sudoers /etc/sudoers.d/sudoers

# Copy .htpasswd file into place
cp ../files/.htpasswd /etc/apache2/.htpasswd

# Copy the apache2 config file into place
cp ../files/default /etc/apache2/sites-available/default

# Restart apache2 
service apache2 restart 



