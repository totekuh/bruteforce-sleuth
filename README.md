# bruteforce-sleuth
<br>A Linux tool that can be used to analyze and locate failed preauth attempts found in system logs, thus potentially identifying security threats.
Use this tool to track your attackers until their Internet Service Provider.

<br/> bruteforce-sleuth is fully capable with ssh-bruteforcing trails. Use /var/log/auth.log (or you can provide any log file that you want)

<br>Requirements: Python 3.7.*; pip, pip requests folium; any web-server to share the results page.
<br>
<br>Extract a system log with IP addresses (e.g. it can be your ssh-server log: /var/log/auth.log)
<br>Run start.sh as root to get the longitude and latitude of all disconnected IPs from the log.
<br><img src="https://imgur.com/LLdtLA9.jpg"/>
<br>You will see the list of coordinates with map.html generated:
<br><img src="https://imgur.com/UwepPdi.jpg"/>
<br>Run any web server (i.e. apache2) and open the interactive map at http://0.0.0.0/map.html.
<br><img src="https://imgur.com/vg6ZtrL.jpg"/>
<br>Track with details every failed attemp to bruteforce your server.
<br><img src="https://i.imgur.com/p943AEL.jpg"/>
<br/>Generated results will be placed at /var/www/html/map.html and /var/www/html/map-clustered.html
<br/>
<br/>If you are not interested in details and you just want to know which regions are more annoying than others - then you can use Clustered map.
<br/><img src="https://imgur.com/BLuHKHP.jpg"/>
