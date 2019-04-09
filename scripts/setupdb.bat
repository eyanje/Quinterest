@echo off

echo This script will setup the database, tables, and new user for Quinterest
SET username=quinterestdb
SET password=quinterestdb

echo The new user will be $username with password $password
echo Logging into mysql as root
echo Enter the password for mysql's root if prompted

mysql -e "GRANT ALL PRIVILEGES ON quinterestdb.* TO '%username%'@'localhost' identified by '%password%';"

echo Creating databases
echo When prompted for a password, enter quinterestdb
mysql -u %username% -p -e "source db/createdatabase;" quinterestdb
mysql -u %username% -p -e "source db/createtossupstable;" quinterestdb
mysql -u %username% -p -e "source db/createbonustable;" quinterestdb
