rachelpiOS
---------------

*NOTE: This install is tested to work with [`2016-05-27-raspbian-jessie`](https://www.armbian.com/orange-pi-zero-3/)

Orange Pi Zero 3 has problems with SD card corruption
use an external SDA device to byspass this problem

Creating USB /var/www/modules mountable storage

`lsblk` - know the sda address

`sudo umount /dev/sda1` - Unmount, just to be sure it is

If error occurs:
umount: /var/www: target is busy.

`systemctl stop apache2 && systemctl stop kolibri`

``

***SKIP THIS IF USB IS CLONED***

`sudo mkfs.ext4 -L media /dev/sda1` - this will take long

``

`sudo mkdir -p /var/www/modules`

`sudo mount /dev/sda1 /var/www/modules`

`reboot`

`lsblk` - confirm if the sda has been mounted





paste in the following command after reboot.

Update Repositories
`apt-get update -y`
`apt update -y`

Expand your microSD card partition

`sudo apt install cloud-guest-utils` - Install growpart

`df -h`

`sudo lsblk` - Know your blocks

`sudo growpart /dev/mmcblk1 1` - change blk1 depending on the main storage

`sudo resize2fs /dev/mmcblk1p1`


`rm -rf /tmp/rachel_installer && curl -fsS https://raw.githubusercontent.com/june23rd1987/rachelpiOS/master/installer.py | python3`

Please note that this will change the 'pi' user's password to: rachel

All default username and passwords will be rachel/rachel unless noted differently.




***FREEZE OS***
1.	Install overlayroot (tiny Canonical helper).

`sudo apt install overlayroot -y     # ~30 kB`

2.	Edit the config.

`echo 'overlayroot="tmpfs:swap=1"' | sudo tee /etc/overlayroot.local.conf`

`sudo update-initramfs -u`

`sudo reboot`
3.	Verify after reboot:

`mount | grep ' / '`


Additional Details
---------------
Please check out the Wiki: https://github.com/rachelproject/rachelpiOS/wiki
