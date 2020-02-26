### BEGIN INIT INFO
# Provides:          auto_start.sh
# Required-Start:    $all
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: start all deployinator-related things at boot
# Description:       ^^ what that says
### END INIT INFO

#!/usr/bin/env bash

cd /git/deployinator
git pull

mv ./startup_scripts/auto_start.sh /etc/init.d/auto_start.sh

./startup_scripts/deployinator.sh
