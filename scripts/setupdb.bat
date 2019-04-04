@echo off

echo This script will setup the database, tables, and new user for Quinterest
SET username=quinterestdb
SET $password=quinterestdb

echo The new user will be $username with password $password
echo Logging into mysql as root
echo Enter the password for mysql's root if prompted

mysql -e "GRANT ALL PRIVILEGES ON quinterestdb.* TO '%username%'@'localhost' identified by '%password%';"

echo Creating databases
mysql -u %username% --password=%password% -e "source db/createdatabase;" quinterestdb
mysql -u %username% --password=%password% -e "source db/createtossupstable;" quinterestdb
mysql -u %username% --password=%password% -e "source db/createbonustable;" quinterestdb
