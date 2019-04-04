# Quinterest (PHP7)
A Searchable Quizbowl Database, updated for modern standards

## Prerequesites

- [PHP](https://www.php.net/)
- [Node.js](https://nodejs.org/)
- [MySQL/MariaDB](https://mariadb.org/)
- [MySQL Python Connector](https://dev.mysql.com/downloads/connector/python/)
- [Python 3](https://www.python.org/)

## Downloading

[Download](https://github.com/eyanje/Quinterest-PHP7/archive/master.zip) and extract the zip files.

## Setting up

Run `.\setup.bat` to set up the database and python.

### History Bowl

Convert every pdf file in `db\python\history_bowl\` into a docx. You can use [https://pdf2docx.com/]

Run `.\historybowl.bat` to put the history bowl questions in the database. You will have to supply information on the tournament.
You may leave spaces blank, but it may impact searchability.

## Quickstart Server

Run `.\start.bat` to start the php server at localhost.
