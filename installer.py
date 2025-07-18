#!/usr/bin/env python
# filepath: c:\Users\PC-ACCOUNTING4\python\rachel_orangepi_installer.py
# suggested by copilot

import sys
import os
import subprocess
import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument("--khan-academy",
                       choices=["none", "ka-lite"],
                       default="ka-lite",
                       help="Select Khan Academy package to install (default = \"ka-lite\")")
argparser.add_argument("--no-wifi",
                       dest="install_wifi",
                       action="store_false",
                       help="Do not configure local wifi hotspot.")
args = argparser.parse_args()

def install_kalite():
    sudo("apt-get install -y python3-pip") or die("Unable to install pip.")
    sudo("pip3 install ka-lite-static") or die("Unable to install KA-Lite")
    sudo("printf '\nyes\nyes\nno\n' | kalite manage setup --username=rachel --password=rachel --hostname=rachel --description=rachel")
    sudo("mkdir -p /etc/ka-lite") or die("Unable to create /etc/ka-lite configuration directory.")
    cp("files/init-functions", "/etc/default/ka-lite") or die("Unable to install KA-Lite configuration script.")
    cp("files/init-service", "/etc/init.d/ka-lite") or die("Unable to install KA-Lite service.")
    sudo("chmod +x /etc/init.d/ka-lite") or die("Unable to set permissions on KA-Lite service.")
    sudo("sh -c 'echo root >/etc/ka-lite/username'") or die("Unable to configure the userid of the KA-Lite process.")
    if exists("/etc/systemd"):
        sudo("mkdir -p /etc/systemd/system/ka-lite.service.d") or die("Unable to create KA-Lite service options directory.")
        cp("files/init-systemd-conf", "/etc/systemd/system/ka-lite.service.d/10-extend-timeout.conf") or die("Unable to increase KA-Lite service startup timeout.")
    sudo("update-rc.d ka-lite defaults") or die("Unable to register the KA-Lite service.")
    sudo("service ka-lite start") or die("Unable to start the KA-Lite service.")
    sudo("sh -c '/usr/local/bin/kalite --version > /etc/kalite-version'") or die("Unable to record kalite version")
    return True

def install_kiwix():
    sudo("mkdir -p /var/kiwix/bin") or die("Unable to make create kiwix directories")
    kiwix_version = "0.9"
    sudo("sh -c 'wget -O - http://downloads.sourceforge.net/project/kiwix/"+kiwix_version+"/kiwix-server-"+kiwix_version+"-linux-armv5tejl.tar.bz2 | tar xj -C /var/kiwix/bin'") or die("Unable to download kiwix-server")
    cp("files/kiwix-sample.zim", "/var/kiwix/sample.zim") or die("Unable to install kiwix sample zim")
    cp("files/kiwix-sample-library.xml", "/var/kiwix/sample-library.xml") or die("Unable to install kiwix sample library")
    cp("files/rachel-kiwix-start.pl", "/var/kiwix/bin/rachel-kiwix-start.pl") or die("Unable to copy rachel-kiwix-start wrapper")
    sudo("chmod +x /var/kiwix/bin/rachel-kiwix-start.pl") or die("Unable to set permissions on rachel-kiwix-start wrapper")
    cp("files/init-kiwix-service", "/etc/init.d/kiwix") or die("Unable to install kiwix service")
    sudo("chmod +x /etc/init.d/kiwix") or die("Unable to set permissions on kiwix service.")
    sudo("update-rc.d kiwix defaults") or die("Unable to register the kiwix service.")
    sudo("service kiwix start") or die("Unable to start the kiwix service.")
    sudo("sh -c 'echo "+kiwix_version+" >/etc/kiwix-version'") or die("Unable to record kiwix version.")
    return True

def install_kiwix2025():
    sudo("apt install kiwix-tools -y") or die("Unable to install kiwix2025")
    return True


def install_kolibri():
    print("Installing Kolibri...")
    sudo("apt-get install -y python3-pip ffmpeg") or die("Unable to install python3-pip for Kolibri.")
    sudo("pip3 install --upgrade pip") or die("Unable to upgrade pip for Kolibri.")
    sudo("pip3 install kolibri") or die("Unable to install Kolibri.")

    # Create a systemd service file for Kolibri
    kolibri_servicex = """
[Unit]
Description=Kolibri offline learning platform
After=network.target

[Service]
User=www-data
Group=www-data
Environment=KOLIBRI_HOME={kolibri_content_dir}
ExecStart=/usr/local/bin/kolibri start --foreground --port=9090
Restart=always

[Install]
WantedBy=multi-user.target
""".format(kolibri_content_dir=rachel_dir+"/modules/kolibri")
    

    kolibri_service3 = """
[Unit]
Description=Kolibri offline learning platform
After=network.target

[Service]
User=www-data
Group=www-data
Environment=KOLIBRI_HOME=/var/www/modules/kolibri
ExecStart=/usr/local/bin/kolibri start --foreground --port=9090
Restart=always

[Install]
WantedBy=multi-user.target
"""
    kolibri_port = "9090"
    kolibri_service = """
[Unit]
Description=Kolibri offline learning platform
After=network.target

[Service]
User=www-data
Group=www-data
ExecStart=/usr/local/bin/kolibri start --foreground --port=9090
Restart=always

[Install]
WantedBy=multi-user.target
"""
    
    print("Writing Kolibri Service...")
    with open("/tmp/kolibri.service", "w") as f:
        f.write(kolibri_service)
    sudo("mv /tmp/kolibri.service /etc/systemd/system/kolibri.service") or die("Unable to install Kolibri systemd service")
    sudo("systemctl daemon-reload")
    sudo("systemctl enable kolibri") or die("Unable to enable Kolibri service.")
    sudo("systemctl start kolibri") or die("Unable to start Kolibri service.")

    print("Kolibri installation complete. Access it at http://<device-ip>:"+kolibri_port+"/")
    sudo("sh -c 'echo 0.18.1 >/etc/kolibri-version'") or die("Unable to record kolibri version.")
    print("Kolibri Installed Successfully.")
    return True
    


def install_kiwix2():
    import platform

    sudo("mkdir -p /var/kiwix/bin") or die("Unable to create kiwix directories")
    # Download latest ARMv7 kiwix-serve binary (adjust version as needed)
    kiwix_url = "https://download.kiwix.org/release/kiwix-tools/kiwix-tools_linux-armhf.tar.gz"
    kiwix_tar = "/tmp/kiwix-tools_linux-armhf.tar.gz"
    sudo(f"wget -O {kiwix_tar} {kiwix_url}") or die("Unable to download kiwix-serve")
    sudo(f"tar -xzf {kiwix_tar} -C /var/kiwix/bin --strip-components=1") or die("Unable to extract kiwix-serve")
    sudo("rm -f {kiwix_tar}")  # Clean up

    # Copy sample ZIM and library files
    cp("files/kiwix-sample.zim", "/var/kiwix/sample.zim") or die("Unable to install kiwix sample zim")
    cp("files/kiwix-sample-library.xml", "/var/kiwix/sample-library.xml") or die("Unable to install kiwix sample library")
    cp("files/rachel-kiwix-start.pl", "/var/kiwix/bin/rachel-kiwix-start.pl") or die("Unable to copy rachel-kiwix-start wrapper")
    sudo("chmod +x /var/kiwix/bin/rachel-kiwix-start.pl") or die("Unable to set permissions on rachel-kiwix-start wrapper")

    # Install systemd service for kiwix-serve
    kiwix_service = """
[Unit]
Description=Kiwix-serve
After=network.target

[Service]
ExecStart=/var/kiwix/bin/kiwix-serve --port=8080 --library /var/kiwix/sample-library.xml
User=www-data
Restart=always

[Install]
WantedBy=multi-user.target
"""
    with open("/tmp/kiwix.service", "w") as f:
        f.write(kiwix_service)
    sudo("mv /tmp/kiwix.service /etc/systemd/system/kiwix.service") or die("Unable to install kiwix systemd service")
    sudo("systemctl daemon-reload")
    sudo("systemctl enable kiwix")
    sudo("systemctl start kiwix") or die("Unable to start the kiwix service.")

    sudo("sh -c 'echo latest >/etc/kiwix-version'") or die("Unable to record kiwix version.")
    return True




def exists(p):
    return os.path.isfile(p) or os.path.isdir(p)

def cmd(c):
    result = subprocess.Popen(c, shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
    try:
        result.communicate()
    except KeyboardInterrupt:
        pass
    return (result.returncode == 0)

def sudo(s):
    return cmd("sudo DEBIAN_FRONTEND=noninteractive %s" % s)

def die(d):
    print("Error: " + str(d))
    sys.exit(1)

def is_vagrant():
    return os.path.isfile("/etc/is_vagrant_vm")

def wifi_present():
    if is_vagrant():
        return False
    # Orange Pi Zero 3 usually uses wlan0 for WiFi
    return exists("/sys/class/net/wlan0")

def basedir():
    bindir = os.path.dirname(sys.argv[0])
    if not bindir:
        bindir = "."
    if exists(bindir + "/files"):
        return bindir
    else:
        return "/tmp/rachel_installer"
    
def cp(s, d):
    return sudo("cp %s/%s %s" % (basedir(), s, d))


#Expand Files System MANUAL THIS
sudo("apt-get install -y cloud-guest-utils") or die("Unable to install cloud-guest-utils for growpart and resize2fs.")
#print("Expanding filesystem...")
#sudo("sudo growpart /dev/mmcblk1 1")
#sudo("sudo resize2fs /dev/mmcblk1p1") or die("Unable to resize filesystem.")
#print("Expanding filesystem complete...")

########sudo("apt-get update -y") or die("Unable to update.")
print("Installing Git...")
sudo("apt-get install -y git") or die("Unable to install Git.")
print("Installing net-tools...")
sudo("apt-get install -y net-tools") or die("Unable to install net-tools for ifconfig.")



# Clone the repo.
if basedir() == "/tmp/rachel_installer":
    print("Cloning repo https://github.com/june23rd1987/rachelpiOS.git...")
    sudo("rm -fr /tmp/rachel_installer")
    sudo("git clone --depth 1 https://github.com/june23rd1987/rachelpiOS.git /tmp/rachel_installer") or die("Unable to clone RACHEL installer repository.")
    print("Cloning done.")



if is_vagrant():
    sudo("mv /vagrant/sources.list /etc/apt/sources.list")
    


# Update and upgrade OS
#########sudo("apt-get update -y") or die("Unable to update.")
#sudo("apt-get dist-upgrade -y") or die("Unable to upgrade OS.")

# Remove Raspberry Pi firmware update
# if not is_vagrant():
#     sudo("yes | sudo rpi-update") or die("Unable to upgrade Raspberry Pi firmware")

# Setup wifi hotspot
#if wifi_present() and args.install_wifi:
    #sudo("apt-get -y install hostapd udhcpd") or die("Unable install hostapd and udhcpd.")
    #cp("files/udhcpd.conf", "/etc/udhcpd.conf") or die("Unable to copy UDHCPd configuration (udhcpd.conf)")
    #cp("files/udhcpd", "/etc/default/udhcpd") or die("Unable to copy UDHCPd configuration (udhcpd)")
    #cp("files/hostapd", "/etc/default/hostapd") or die("Unable to copy hostapd configuration (hostapd)")
    #cp("files/hostapd.conf", "/etc/hostapd/hostapd.conf") or die("Unable to copy hostapd configuration (hostapd.conf)")
    #sudo("sh -c 'echo 1 > /proc/sys/net/ipv4/ip_forward'") or die("Unable to set ipv4 forwarding")
    #cp("files/sysctl.conf", "/etc/sysctl.conf") or die("Unable to copy sysctl configuration (sysctl.conf)")
    #sudo("iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE") or die("Unable to set iptables MASQUERADE on eth0.")
    #sudo("iptables -A FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT") or die("Unable to forward wlan0 to eth0.")
    #sudo("iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT") or die("Unable to forward wlan0 to eth0.")
    #sudo("sh -c 'iptables-save > /etc/iptables.ipv4.nat'") or die("Unable to save iptables configuration.")
    #sudo("ifconfig wlan0 10.10.10.10") or die("Unable to set wlan0 IP address (10.10.10.10)")
    #sudo("service hostapd start") or die("Unable to start hostapd service.")
    #sudo("service udhcpd start") or die("Unable to start udhcpd service.")
    #sudo("update-rc.d hostapd enable") or die("Unable to enable hostapd on boot.")
    #sudo("update-rc.d udhcpd enable") or die("Unable to enable UDHCPd on boot.")
    #sudo("sh -c 'sed -i \"s/^exit 0//\" /etc/rc.local'") or die("Unable to remove exit from end of /etc/rc.local")
    #sudo("sh -c 'echo ifconfig wlan0 10.10.10.10 >> /etc/rc.local; echo service udhcpd restart >> /etc/rc.local;'") or die("Unable to setup udhcpd reset at boot.")
    #sudo("sh -c 'echo exit 0 >> /etc/rc.local'") or die("Unable to replace exit to end of /etc/rc.local")
  
if wifi_present() and args.install_wifi:
    # Add Wifi Hotspot
    sudo("systemctl disable system-resolved.service")
    sudo("systemctl stop systemd-resolved") or die("Unable to stop systemd-resolved")
    sudo("systemctl status systemd-resolved")
    sudo("apt install procps iproute2 dnsmasq iptables hostapd iw -y") or die("Unable to install procps iproute2 dnsmasq iptables hostapd iw -y")
    sudo("wget -O /opt/0.7.6.tar.gz https://github.com/june23rd1987/rachelpiOS/raw/refs/heads/master/0.7.6.tar.gz") or die("Unable to wget linux-router")
    sudo("tar -xvf /opt/0.7.6.tar.gz -C  /opt/") or die("Unable to tar -xvf 0.7.6.tar.gz")
    sudo("mv /opt/linux-router-0.7.6 /opt/linux-router")
    #sudo("/opt/linux-router/lnxrouter --ap wlan0 DreamCube -p DreamCube -g 10.10.10.10 --no-virt --daemon") or die("Failed on lnxrouter")
    
    print("Removing redundant hotspot data from crontab...")
    file_path = "/etc/crontab"
    with open(file_path, "r+") as f:
        lines = [line for line in f if line.strip() != "@reboot root /opt/linux-router/lnxrouter --ap wlan0 DreamCube -p DreamCube -g 10.10.10.10 --no-virt --daemon"]
        f.seek(0)
        f.writelines(lines)
        f.truncate()
    print("Removing done.")
    sudo("sh -c 'echo \"@reboot root /opt/linux-router/lnxrouter --ap wlan0 DreamCube -p DreamCube -g 10.10.10.10 --no-virt --daemon\" >> /etc/crontab'") or die("Failed to write lnxrouter_cron to /etc/crontab")
    print("Add Wifi Hotspot Success")



# Setup LAN
#if not is_vagrant():
#    cp("files/interfaces", "/etc/network/interfaces") or die("Unable to copy network interface configuration (interfaces)")

# Install web platform
php_version = "8.1"
print("Installing web platform...")
sudo("echo mysql-server mysql-server/root_password password rachel | sudo debconf-set-selections") or die("Unable to set default MySQL password.")
sudo("echo mysql-server mysql-server/root_password_again password rachel | sudo debconf-set-selections") or die("Unable to set default MySQL password (again).")


sudo("apt-get -y install apache2 libxml2-dev \
     php libapache2-mod-php php-cgi php-dev php-pear \
     mysql-server mysql-client php-mysql sqlite3 php-sqlite3") or die("Unable to install web platform.")
#######sudo("a2enmod proxy_html") or die("Unable to a2enmod proxy_html")
########sudo("yes '' | sudo pecl install -f stem") or die("Unable to install php stemmer1")
sudo("cd /tmp && rm -rf /tmp/php-stemmer && git clone https://github.com/hthetiot/php-stemmer.git && cd php-stemmer && phpize && /tmp/php-stemmer/configure && make -C libstemmer_c && make && make install")


#######sudo("sh -c 'echo \"extension=stem.so\" >> /etc/php/7.4/cli/php.ini'") or die("Unable to install stemmer CLI config 7.4")
sudo("sh -c 'echo \"extension=stemmer\" >> /etc/php/"+php_version+"/cli/php.ini'") or die("Unable to install stemmer CLI config "+php_version+"")
#######sudo("sh -c 'echo \"extension=stem.so\" >> /etc/php/7.4/apache2/php.ini'") or die("Unable to install stemmer Apache config 7.4")
sudo("sh -c 'echo \"extension=stemmer\" >> /etc/php/"+php_version+"/apache2/php.ini'") or die("Unable to install stemmer Apache config "+php_version+"")



#######sudo("sh -c 'sed -i \"s/upload_max_filesize *= *.*/upload_max_filesize = 512M/\" /etc/php/7.4/apache2/php.ini'") or die("Unable to increase upload_max_filesize in apache2/php.ini")
sudo("sh -c 'sed -i \"s/upload_max_filesize *= *.*/upload_max_filesize = 99999999/\" /etc/php/"+php_version+"/apache2/php.ini'") or die("Unable to increase upload_max_filesize in apache2/php.ini "+php_version+"1")
#######sudo("sh -c 'sed -i \"s/post_max_size *= *.*/post_max_size = 512M/\" /etc/php/7.4/apache2/php.ini'") or die("Unable to increase post_max_size in apache2/php.ini")
sudo("sh -c 'sed -i \"s/post_max_size *= *.*/post_max_size = 99999999/\" /etc/php/"+php_version+"/apache2/php.ini'") or die("Unable to increase post_max_size in apache2/php.ini "+php_version+"")
sudo("service apache2 stop") or die("Unable to stop Apache2.")
#####cp("files/default", "/etc/apache2/sites-available/contentshell.conf") or die("Unable to set default Apache site.")
sudo("curl -o /etc/apache2/sites-available/contentshell.conf https://raw.githubusercontent.com/june23rd1987/rachelpiOS/refs/heads/master/contentshell.conf")
#####sudo("sed -i 's|/var/www|/media/usb/rachel|g' /etc/apache2/sites-available/contentshell.conf") or die("Unable to set contentshell.conf to use /media/usb/rachel as the web root.")
sudo("a2dissite 000-default") or die("Unable to disable default Apache site.")
sudo("a2ensite contentshell.conf") or die("Unable to enable contentshell Apache site.")
cp("files/my.cnf", "/etc/mysql/my.cnf") or die("Unable to copy MySQL server configuration.")
sudo("curl -o /etc/mysql/mysql.cnf https://raw.githubusercontent.com/june23rd1987/rachelpiOS/refs/heads/master/mysql.cnf") or die("Unable to copy MySQL /etc/mysql/mysql.cnf.")
#####sudo("a2enmod php7.4 proxy proxy_html rewrite") or die("Unable to enable Apache2 dependency modules2.")
sudo("a2enmod proxy proxy_html rewrite") or die("Unable to enable Apache2 dependency modules2.")
if exists("/etc/apache2/mods-available/xml2enc.load"):
    sudo("a2enmod xml2enc") or die("Unable to enable Apache2 xml2enc module.")
sudo("service apache2 restart") or die("Unable to restart Apache2.")
print("Installing web platform done.")




if exists("/srv/rachel/www"):
    print("RACHEL directory found at /srv/rachel/www, using that as the base directory.")
    rachel_dir = "/srv/rachel/www"
elif exists("/media/RACHEL/rachel"):
    print("RACHEL directory found at /media/RACHEL/rachel, using that as the base directory.")
    rachel_dir = "/media/RACHEL/rachel"
elif exists("/var/www"):
    print("RACHEL directory found at /var/www, using that as the base directory.")
    rachel_dir = "/var/www"
else:
    print("No RACHEL directory found, using /var/www as the base directory.")
    rachel_dir = "/var/www"

rachelTempDir = "/tmp/rachel_temp"

# Install web frontend
print("Checking if RACHEL contentshell is already installed...")
admin_db_path = f"{rachel_dir}/admin/admin.sqlite"
if not exists(admin_db_path) or (os.path.isfile(admin_db_path) and os.path.getsize(admin_db_path) == 0):
    print("RACHEL "+rachel_dir+"/admin/admin.sqlite not found, installing...")
    print("Deleting existing default web application ("+rachel_dir+")...")
    #sudo("rm -fr "+rachel_dir+"") or die("Unable to delete existing default web application ("+rachel_dir+").")
    print("Unmounting existing USB modules directory ("+rachel_dir+"/modules)...")
    sudo("umount "+rachel_dir+"/modules")
    sudo("rm -rf "+rachel_dir+"")
    #sudo("rm -rf "+rachelTempDir+"") or die("Unable to delete existing temporary RACHEL web application directory ("+rachelTempDir+").")
    sudo("git clone --depth 1 https://github.com/rachelproject/contentshell "+rachel_dir+"") or die("Unable to download RACHEL web application to "+rachel_dir+".")




#add mount USB  
print("Creating "+rachel_dir+"/modules directory...")
#sudo("mkdir -p "+rachel_dir+"/modules")
sudo("mkdir -p "+rachel_dir+"/modules/kolibri/content")
print("Removing /usr/bin/mount /dev/sda1 "+rachel_dir+"/modules  crontab...")
file_path = "/etc/crontab"
with open(file_path, "r+") as f:
    lines = [line for line in f if line.strip() != "@reboot root /usr/bin/mount /dev/sda1 "+rachel_dir+"/modules"]
    f.seek(0)
    f.writelines(lines)
    f.truncate()
print("Removing done.")
sudo("sh -c 'echo \"@reboot root /usr/bin/mount /dev/sda1 "+rachel_dir+"/modules\" >> /etc/crontab'") or die("Failed to write mount to /etc/crontab")
print("Add mount USB to crontab Success")
#print("Trying to mount /dev/sda1 to "+rachel_dir+"/modules...")
#sudo("mount /dev/sda1 "+rachel_dir+"/modules")


# update PHP files for orangepi port
sudo("chmod -R 0777 "+rachel_dir+"/art/") or die("Unable to chmod "+rachel_dir+"/art/ folder")
sudo("curl -o "+rachel_dir+"/admin/common.php https://raw.githubusercontent.com/june23rd1987/rachelpiOS/refs/heads/master/common.php") or die("Unable to update common.php")
sudo("curl -o "+rachel_dir+"/admin/do_tasks.php https://raw.githubusercontent.com/june23rd1987/rachelpiOS/refs/heads/master/do_tasks.php") or die("Unable to update do_tasks.php")
sudo("curl -o "+rachel_dir+"/admin/version.php https://raw.githubusercontent.com/june23rd1987/rachelpiOS/refs/heads/master/version.php") or die("Unable to update version.php")
sudo("curl -o "+rachel_dir+"/art/rachel_banner2.jpg https://raw.githubusercontent.com/june23rd1987/rachelpiOS/34c01206d631e285cbbd2e53ce27768a2c8ecf43/rachel_banner.jpg") or die("Unable to rachel_banner.jpg")
sudo("curl -o "+rachel_dir+"/art/rachel_banner1.jpg https://github.com/june23rd1987/rachelpiOS/blob/master/rachel_banner.jpg?raw=true") or die("Unable to rachel_banner.jpg")
sudo("curl -o "+rachel_dir+"/art/global_hope.png https://raw.githubusercontent.com/june23rd1987/rachelpiOS/refs/heads/master/globalhope2020_logo_green.png")
sudo("curl -o "+rachel_dir+"/favicon.ico https://raw.githubusercontent.com/june23rd1987/rachelpiOS/refs/heads/master/favicon.ico")
sudo("curl -o "+rachel_dir+"/scripts/library.xml https://raw.githubusercontent.com/june23rd1987/rachelpiOS/refs/heads/master/library.xml") or die("Unable to library.xml")
sudo("curl -o "+rachel_dir+"/scripts/empty.zim https://raw.githubusercontent.com/june23rd1987/rachelpiOS/refs/heads/master/empty.zim") or die("Unable to empty.zim")
sudo("curl -o "+rachel_dir+"/index.php https://raw.githubusercontent.com/june23rd1987/rachelpiOS/refs/heads/master/main-index.php") or die("Unable to empty.zim")
sudo("curl -o "+rachel_dir+"/index.php https://raw.githubusercontent.com/june23rd1987/rachelpiOS/refs/heads/master/main-index.php") or die("Unable to empty.zim")
sudo("curl -o "+rachel_dir+"/css/style.css https://raw.githubusercontent.com/june23rd1987/rachelpiOS/refs/heads/master/style.css") or die("Unable to style.css")

sudo("curl -o "+rachel_dir+"/scripts/rachelKiwixStart.sh https://raw.githubusercontent.com/june23rd1987/rachelpiOS/refs/heads/master/rachelKiwixStart.sh") or die("Unable to download rachelKiwixStart.sh")
sudo("curl -o "+rachel_dir+"/scripts/automount.sh https://raw.githubusercontent.com/june23rd1987/rachelpiOS/refs/heads/master/automount.sh") or die("Unable to download automount.sh")
sudo("curl -o "+rachel_dir+"/scripts/startkiwix.sh https://raw.githubusercontent.com/june23rd1987/rachelpiOS/refs/heads/master/startkiwix.sh") or die("Unable to download startkiwix.sh")
sudo("chmod -R +x "+rachel_dir+"/scripts/") or die("Unable to chmod "+rachel_dir+"/scripts/ folder")
print("Removing redundant kiwix data from crontab...")
file_path = "/etc/crontab"
with open(file_path, "r+") as f:
    lines = [line for line in f if line.strip() != "@reboot root /bin/sh "+rachel_dir+"/scripts/startkiwix.sh"] #rachelKiwixStart.sh
    f.seek(0)
    f.writelines(lines)
    f.truncate()
print("Removing done.")
sudo("sh -c 'echo \"@reboot root /bin/sh "+rachel_dir+"/scripts/startkiwix.sh\" >> /etc/crontab'") or die("Failed to write startkiwix-cron to /etc/crontab")
print("Add Kiwix Success")
kiwix_version = "3.2.0"
sudo("sh -c 'echo "+kiwix_version+" >/etc/kiwix-version'") or die("Unable to record kiwix version.")


# Install RACHEL content library
#print("Kill existing kiwix-serve process if running...") - already in rachelKiwixStart.sh
#sudo("killall /usr/bin/kiwix-serve") or die("Unable to kill existing kiwix-serve process.") - already in rachelKiwixStart.sh
print("Starting kiwix-serve daemon via "+rachel_dir+"/scripts/rachelKiwixStart.sh")
sudo("nohup "+rachel_dir+"/scripts/rachelKiwixStart.sh > /dev/null 2>&1 &") or die("Unable to start kiwix-serve daemon via rachelKiwixStart.sh script.")
print("Done: nohup "+rachel_dir+"/scripts/rachelKiwixStart.sh > /dev/null 2>&1 &")


sudo("mkdir -p "+rachel_dir+"/modules") or die("Unable to create directory ("+rachel_dir+"/modules).")
sudo("chmod -R 0777 "+rachel_dir+"/modules/") or die("Unable to chmod "+rachel_dir+"/art/ folder")


sudo("chown -R www-data.www-data "+rachel_dir+"") or die("Unable to set permissions on RACHEL web application ("+rachel_dir+").")
sudo("sh -c \"umask 0227; echo 'www-data ALL=(ALL) NOPASSWD: /sbin/shutdown' >> /etc/sudoers.d/www-shutdown\"") or die("Unable to add www-data to sudoers for web shutdown")
sudo("usermod -a -G adm www-data") or die("Unable to add www-data to adm group (so stats.php can read logs)")





# Extra wifi driver configuration
#if wifi_present() and args.install_wifi:
#    sudo("cd /tmp/rachel_installer")
#    sudo("ls -lt files/hostapd_RTL8188CUS")
#    cp("files/hostapd_RTL8188CUS", "/etc/hostapd/hostapd.conf.RTL8188CUS") or die("Unable to copy RTL8188CUS hostapd configuration.")
#    cp("files/hostapd_realtek.conf", "/etc/hostapd/hostapd.conf.realtek") or die("Unable to copy realtek hostapd configuration.")

#if args.khan_academy == "ka-lite":
#    install_kalite() or die("Unable to install KA-Lite.")

# install the kiwix server (but not content)
install_kiwix2025()

# install the kiwix server (but not content)
install_kolibri()

# Remove Raspberry Pi user password change
# if not is_vagrant():
#     sudo("sh -c 'echo pi:rachel | chpasswd'") or die("Unable to change 'pi' password.")

# Update hostname (LAST!)
#if not is_vagrant():
#    cp("files/hosts", "/etc/hosts") or die("Unable to copy hosts file.")
#    cp("files/hostname", "/etc/hostname") or die("Unable to copy hostname file.")
#    sudo("hostnamectl set-hostname $(cat /etc/hostname)") or die("Unable to set hostname.")





# record the version of the installer we're using - this must be manually
# updated when you tag a new installer
sudo("sh -c 'echo OrangePi-2025.06.25 > /etc/rachelinstaller-version'") or die("Unable to record rachelpiOS version.")

print("RACHEL has been successfully installed. It can be accessed at: http://10.10.10.10/")

print("END of script") 
