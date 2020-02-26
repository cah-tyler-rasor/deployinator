## what's this??

so, I'm tired of `scp`-ing scripts over to the pi... plus we're going to want the deployinator code to just start when the box is turned on

here's what we did on both pis:
* add the `auto_start.sh` script to `/etc/init.d`
* then `sudo update-rc.d auto_start.sh defaults` to run on boot
* gen deploy keys on both pis for git access

now, when they boot it will do a git pull on this repo and we can manage the boot/run process via git
 