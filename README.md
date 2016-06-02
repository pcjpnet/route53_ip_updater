# Route53 IP Updater

Route53 DDNS IP Updater Script


1. Install option packages  
    sudo aptitude install python-pip  
    sudo aptitude install python-dev  
    sudo pip install boto  
    sudo pip install netifaces  

2. Install these script files  
    sudo mkdir /opt/update_route53  
    sudo chown $USER:$USER /opt/update_route53  
    svn checkout https://pc-jp.net/svn/update_route53/trunk/ /opt/update_route53  

3. Change settings in "ip_update.py" (key, sec, commands)  

4. Add crontab  
    */10 * * * * python -B /opt/update_route53/ip_update.py  


