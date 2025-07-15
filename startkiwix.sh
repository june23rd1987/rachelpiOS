#!/bin/bash
#-------------------------------------------
# This script is used to refresh the kiwix library upon restart to
# include everything in the rachel modules directory. It is used
# as part of rachelStartup.sh and various scripts in contentshell
#
# Authors: Sam Kinch <sam@hackersforcharity.org>     (bash version)
#          Jonathan Field <jfield@worldpossible.org> (original perl version)
#                                                    (& bash version tweaks)
#          James Kainer <james@worldpossible.org>    (Updates for 3.1.2)
# Date: 2021-07-07
#-------------------------------------------

# Restart Kiwix
killall /usr/bin/kiwix-serve
/usr/bin/kiwix-serve --daemon --port=81 --library /var/www/scripts/library.xml > /dev/null
