# Quinterest (PHP7)
A Searchable Quizbowl Database, updated for modern standards

## Installation

Clone the repository
```
$ git clone https://github.com/eyanje/Quinterest-PHP7
```
This should place all the files in the folder ./Quinterest-PHP7

Make sure Apache2 is installed
```
$ apt-get install apache2
```

For easy installation, copy the files from ./Quinterest-PHP7 to /var/www/html

Next, install and enable the PHP and MySQL mods
```
apt-get install php-fpm
sudo apt-get install php libapache2-mod-php php-mcrypt php-mysql
sudo a2enmod proxy_fcgi setenvif
```

Start apache with `service start apache2`
Quinterest should now be running at `http://localhost/`

## Creating the database

Quinterest requires a database of questions to use.
If anyone figures out how to do this, please message me.





