# Quinterest (PHP7)
A Searchable Quizbowl Database, updated for modern standards

## Prerequesites

- [PHP](https://www.php.net/)
- [Node.js](https://nodejs.org/)
- [MySQL/MariaDB](https://mariadb.org/)
- [Python 3](https://www.python.org/)

## Downloading

[Download](https://github.com/eyanje/Quinterest-PHP7/archive/master.zip) and extract the zip files.

Run `downloadquizbug.bat` to download QuizBug.

## Apache Installation

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
apt-get install php libapache2-mod-php php-mcrypt php-mysql a2enmod proxy_fcgi setenvif
```

Start apache with `service start apache2`
Quinterest should now be running at `http://localhost/`

## Quickstart Server

Run `.\start.bat` to start the php server at localhost.

## Creating the database

### Linux

Run `./setupdb` to setup the database.

### Windows

Run `.\setupdb.bat` to setup the database.

As of now, there is no automated table updating.
