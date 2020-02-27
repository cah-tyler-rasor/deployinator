## what's this??

so, I'm tired of `scp`-ing scripts over to the pi... plus we're going to want the deployinator code to just start when the box is turned on

here's what we did on both pis:
* gen deploy keys on both pis for git access (following [this guide](https://help.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key))
* ^^ did that as `root` because `systemd` doesn't run startup scripts as `pi`
* put the `deployinator.service` file in `/lib/systemd/system/`
* enabled the service: `sudo systemctl enable deployinator.service`

now, when they boot it will do a git pull on this repo and we can manage the boot/run process via git
 