#! /bin/bash

echo
if [ $USER != 'root' ]
then
  echo 'Run as root. Exiting.'
  exit
fi

logpath='/var/log/auth.log'
echo 'Using log file: ' $logpath

echo 'Copying the log to current directory...'
cp $logpath ./log

echo 'Done. Parsing the log...'
python3  map.py

echo 'Done. You can now access coordinates via the program output and/or generated map.html'
echo 'Removing log file.'

rm log

echo 'Done.'
