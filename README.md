rachelpiOS
---------------

*NOTE: This install is tested to work with `2016-05-27-raspbian-jessie` and is known to have problems with newer versions*

To install is easy:

Expand your microSD card partition

`df -h`
`sudo lsblk` - Know your blocks
`sudo growpart /dev/mmcblk1 1` - change blk1 depending on the main storage
`sudo resize2fs /dev/mmcblk1p1`


NOTE: for WIFI to ever work on the unit, you must have the WIFI USB dongle inserted
during installation so that the install script can configure it properly.

paste in the following command after reboot.

`apt-get update -y`

`rm -rf /tmp/rachel_installer && curl -fsS https://raw.githubusercontent.com/june23rd1987/rachelpiOS/master/installer.py | python3`

Please note that this will change the 'pi' user's password to: rachel

All default username and passwords will be rachel/rachel unless noted differently.

Additional Details
---------------
Please check out the Wiki: https://github.com/rachelproject/rachelpiOS/wiki
