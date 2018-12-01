# geo-ip-lookup
<br>A Linux tool that can be used to analyze and locate failed preauth attempts found in system logs, thus potentially identifying security threats.

<br>Requirements: Python 3.7.*; pip, pip requests folium; any web-server to share the results page.
<br>
<br>Extract a system log with IP addresses (e.g. it can be your ssh-server log: /var/log/auth.log)
<br>Run start.sh as root to get the longitude and latitude of all disconnected IPs from the log.
<br><img src="https://i.imgur.com/vLrkrgI.jpg"/>
<br>You will see the list of coordinates with map.html generated:
<br><img src="https://i.imgur.com/etcs9RV.jpg"/>
<br>Open the interactive map.
<br><img src="https://i.imgur.com/Xf4rWSD.jpg"/>
<br>Track every failed attemp to connect to your server.
<br><img src="https://i.imgur.com/p943AEL.jpg"/>
