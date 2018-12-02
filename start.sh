#! /bin/bash

echo
if [ $USER != 'root' ]
then
  echo 'Run as root. Exiting.'
  exit
fi

logpath='/var/log/auth.log'

echo 'Receiving list of available logs...'

ls /var/log/*.log | grep ^ | grep "/var/log/"

echo '======================================'

echo 'Done. Enter log file absolute path:'

read logpath

echo 'Using log file: ' $logpath

echo 'Copying the log to current directory...'
cp $logpath ./log

echo '======================================'

echo 'Done. Parsing the log...'
python3  map.py

echo '======================================'

echo 'Done. You can now access coordinates via the program output and/or generated map.html'
echo 'Removing log file.'

rm log

webpagepath='/var/www/html/map.html'
echo 'Moving generated map to the specified location:' $webpagepath

echo '======================================'

mv ./map.html $webpagepath
echo 'Done.'
