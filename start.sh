#! /bin/bash

echo
if [ $USER != 'root' ]
then
  echo 'Run as root. Exiting.'
  exit
fi

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
python3 log_parser.py

echo 'Done. Generating the map...'
python3 map.py

echo '======================================'

echo 'Done. You can now access coordinates via the program output and/or generated map.html'
echo 'Removing log file...'

rm log

mappagepath='/var/www/html/map.html'
mapclusteredpagepath='/var/www/html/map-clustered.html'

echo 'Moving generated map to the specified location:' $mappagepath
echo 'Moving generated clustered map to the specified location:'$mapclusteredpagepath

echo '======================================'

mv ./map.html $mappagepath
mv ./map-clustered.html $mapclusteredpagepath
echo 'Done.'
