@echo off

echo Starting PHP server at 0.0.0.0:80

php -S 0.0.0.0:80 -c %CD%/php.ini 
