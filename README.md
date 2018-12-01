# geo-ip-lookup
<br>A Linux tool that can be used to analyze the system logs for the recorded IP addresses and identify geolocation of your pottential attackers.

<br>Required: Python 3.7.*; pip, pip requests folium; any web-server to share the result page.
<br>
<br>Extract the system log with IP addresses (e.g. it can be your ssh-server log: /var/log/auth.log)
<br>Run the start.sh script as root and get the longitude and latitude of all IP's from the log.
<br><img src="https://i.imgur.com/vLrkrgI.jpg"/>
<br>With everything just done, you will see the list of coordinates with map.html generated:
<br><img src="https://i.imgur.com/etcs9RV.jpg"/>
<br>Visit an interactive map with results.
<br><img src="https://i.imgur.com/Xf4rWSD.jpg"/>
<br>Track every failed attemp to connect your server.
<br><img src="https://i.imgur.com/p943AEL.jpg"/>
