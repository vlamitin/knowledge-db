# Arch after install

Пример установки LARBS и последующей настройки
И некоторый troubleshooting 

1. Собственно, установка
`cd /tmp`
`curl -L0 https://raw.githubusercontent.com/vlamitin/LARBS/master/larbs.sh >> larbs.sh`
`sh larbs.sh`

2. В /etc/passwd он изменил home directory root пользователя на свою. Это надо убрать 3. Он сделал так, что если команда требует sudo, то sudo подставляется автоматически. Это надо убрать.

4. Добавить в prompt текущую git директорию

5. придумать как правильно линкать установленные локально проги (idea, tg) - через ln-s, или через path, смотреть чтобы в dmenu прокидывалось
   pridumal - symlink v .scripts (ne zabivaem polnii put)
6. synclient - add tap events, add them to i3 config exec-always
```
install xf86-input-synaptics
cp /usr/share/X11/xorg.conf.d/70-synaptics.conf /etc/X11/xorg.conf.d/
toucheventson
modprobe -v psmouse (if synclient fails with "no driver found")
```

8. edit apps font size in ~/.gtk ... 2.0 or 3.0 - did't understand yet how they're work
!!! some apps use fonts not from gtk configs, but from ~/.config/fontconfig
10. posmotri s larbs spisok prog. tam ssilka ta st build luka. v nem popravit config.h i peresobrat
   `make`
   `sudo make clean install`
   i perelogin
	{ MODKEY,            	XK_k,  		zoom,      	{.f = +2} },
	{ MODKEY,            	XK_j,   	zoom,		{.f = -2} },

11. change gtk theme to arc (see in asus 555) [see](https://wiki.archlinux.org/index.php/GTK+)
12. adjust time and brightness settigns according to asus 555
this may help with the time: (problem when dual booting with win). This need login to win =(

To fix it, just hit Start and type regedit.exe in the search box. Hit Enter and navigate to HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\TimeZoneInformation. Right click anywhere in the right pane and hit New > QWORD (64bit) or DWORD (32-bit) Value - depending on your win10 distro. Name it RealTimeIsUniversal, then double click on it and give it a value of 1. You can also change it via cmd:
```
Reg add HKLM\SYSTEM\CurrentControlSet\Control\TimeZoneInformation /v RealTimeIsUniversal /t REG_QWORD /d 1
```
## brightness xbacklight problem (keyboard brightness controls don't work)
- download this [package](https://gitlab.com/wavexx/acpilight)
- `sudo make install`
it replaces xbacklight with its own implementation (xbacklight interface for changing brightness stays the same)
(you may need to usermod -a -G video {user} to get this work)

13. sdkman needs vpn to be installed (oh yes, baby), so set up you vpn first (it is a package manager for java, groovy, gradle, spring and so on
https://github.com/sdkman/sdkman-cli - look also at another possibilities (such as docker)
1. install docker

15. Fonts
download this [font](https://github.com/supermarin/YosemiteSanFranciscoFont)
copy *.ttf to ~/.fonts/
set them in cfi:
`font pango: "System San Francisco Display 13"`

16. transmission - you can add proxy to ~/.config/transmission/settings.json
```
proxy-port: Number (default = 80)
proxy-server: String
proxy-server-enabled: Boolean (default = 0)
proxy-type: Number (0 = HTTP, 1 = SOCKS4, 2 = SOCKS5, default = 0)
```
1. [fzf - tool for searching](https://www.youtube.com/watch?v=vt33Hp-4RXg)
2. To turn on your mic:
	1. install alsa-utils
	2. run alsamixer
	3. To enable your microphone, switch to the Capture tab with F4 and enable a channel with Space
$ arecord --duration=5 --format=dat test-mic.wav
$ aplay test-mic.wav


17. cisco anyconnect
yay openconnect
openconnect vpn.crystals.ru
that's it

19. translate & clipboard:
 node ~/projects/grown-up-english-vocabulary-learning/build/src/cli-view/index.js translate --text 'that is it' | xargs -0 -t notify-send

xclip -i
xclip -o

20. Provider substitutes sertificate
this is because you use their dns server
you need to change dns server
via NetworkManager
- create /etc/NetworkManager/conf.d/dns.conf with content:
```
[main]
dns=none
```
(because NetworkManager rewrites resolv.conf by himself)
- add your nameservers to resolv.conf, like here:
```
nameserver 8.8.4.4
nameserver 8.8.8.8
```
- `systemctl restart NetworkManager.service`

21. create user
- `useradd -G adm,cdrom,wheel -s /bin/bash -m -d /home/username username` - создать пользователя username c home dir, bash и 3 группами
- `passwd username`
- ` usermod -a -G sambashare username`
- ` usermod -a -G sudo username`
- (hack - `su - $USER` - to use group withoud relogging)


## nomachine
- `yay nomachine`
- через gui конфигурим: 4004 порт, server not to accept connections, не стартовать при автозапуске
- `usr/NX/bin/nxplayer` – start client to connect to server
- `/usr/NX/bin/nxclient --admin` – open server and client settings

## redshift
- `redshift -l 59.934280:30.335098 -o` - to start without flickering

## clipmenu (спорной полезности утилита)
- `yay clipmenu`
- `yay clipnotify`
- https://github.com/cdown/clipmenu/blob/develop/init/clipmenud.service - copy to /etc/systemd/system/
- `systemctl --user enable clipmenud.service` - enable on user-level
- `systemctl --user start clipmenud.service` - start on user-level

- `systemctl --user edit clipmenud.service` - override some env variables
```
[Service]
Environment=CM_DIR=%h/.cache/
```
add script clipmenuhelper
```
#!/bin/bash
export CM_LAUNCHER=rofi
export CM_DIR=~/.cache
export CM_HISTLENGTH=12

case "$1" in
	show)7. adding rus locale and kb layout as described [here](https://wiki.archlinux.org/index.php/Xorg/Keyboard_configuration#Using_setxkbmap)
`setxkbmap -layout us,ru -variant -option grp:alt_shift_toggle` - this command sets 2 layouts in x (but in cli this not works)

		clipmenu ;;
	clean)
		clipdel -d ".*" \
		&& notify-send "Clipboard Content deleted" -u low \
		|| notify-send "Errors occurred while Clean Up"	;;
esac
```
- add shortcuts
- [see here](https://bbs.archlinux.org/viewtopic.php?pid=1827834#p1827834)

## st
- [download](https://github.com/LukeSmithxyz/st)
- edit config.h (e.g increase pointsize for font)
- `sudo make install`

## locale
- adding rus locale and kb layout as described [here](https://wiki.archlinux.org/index.php/Xorg/Keyboard_configuration#Using_setxkbmap)
`setxkbmap -layout us,ru -variant -option grp:alt_shift_toggle` - this command sets 2 layouts in x (but in cli this not works)
- `setxkbmap -model pc104 -layout us,ru -variant -option grp:caps_toggle` - на минте помогло установить model
- to make rus work in console i added /etc/locale.conf with output of `locale`, except all `C` I replaced with `en_US.utf8` and reboot
- TURN OFF CAPS!
```
To turn off caps lock key, enter:
$ setxkbmap -option ctrl:nocaps

To reset caps lock. enter:
$ setxkbmap -option
```

## xargs
- pipe to vim `fzf | xargs bash -c '</dev/tty vim "$@"' zero` - search to see why it is used (smth about /dev/tty and /dev/null)
- `printf "1\n2\n3\n" | xargs touch` - creates files 1, 2, and 3
- `printf "1\n2\n3\n" | xargs -i touch {}.txt` - creates files 1.txt, 2.txt, and 3.txt
- `find . -maxdepth 1 -name "*.png" | xargs tar -czvf pngs.tar.gz` - creates 1 archive from files
- `echo {1..9} | xargs -n 3` - prints 1-9 in 3 rows
- `touch file{1..9}.txt` - creates 9 files
- `seq 4 | xargs echo "hello"` - hello 1 2 3 4
- `seq 4 | xargs -n 1 echo "hello"` - prints hello 1, hello 2 and so on
- `ls -1 | xargs -I{} -n 1 echo hi {} hi` - prints hi file1 hi and so on
- `date | xargs -I{} notify-send "date is" "{}"`

## tar
- `tar czvf tarball.tar.gz files` - create
- `tar -ztvf tarball.tar.gz` - list files inside
- `tar xf tarball.tar.gz` - extract

## entr
(runs some command every time file/files change)
- [it's pretty straightforwart to install and use](http://eradman.com/entrproject)

## tsp
(tasks spooler - it queues commands)
- `taskid=$(tsp curl ...)` - sets curl task and writes its id to taskid var
- `tsp -D "$taskid" notify-send ...` - executes command after taskid task is resolved

## df, du, ncdu
- `df -h` - prints free space in discs
- `du -h --max-depth=1` - dirs and files size
- `ncdu` - cli with interface to show disc usage by files and dirs
 
 ## printenv
- `printenv` - prints all ENV vars

## source
It is almosh save as `sh` - it just executes commands in file

## for
`for i in {1..5}; do echo hello $i; done`

## whereis, which, whatis
- `whereis npm` - prints "useful" files connected to npm command (bin, man, etc)
- `which` - finds bin
- `whatis npm` - prints 1 line info from man

## wget, curl
- `wget http://...ubuntu.iso` - downloads file here
- `curl http://...ubuntu.iso --output ubuntu.iso` - same with curl

## cron
- install `cronie` if not installed
- `systemctl enable cronie`
- `systemctl start cronie`
- `crontab -l` - list crontab
- `crontab -e` - edti crontab
```
# crontab format

# Field    Description    Allowed Value
# MIN      Minute field    0 to 59
# HOUR     Hour field      0 to 23
# DOM      Day of Month    1-31
# MON      Month field     1-12
# DOW      Day Of Week     0-6
# CMD      Command         Any command to be executed.

# Keyword    Equivalent
# @yearly    0 0 1 1 *
# @daily     0 0 * * *
# @hourly    0 * * * *
# @reboot    Run at startup.

# Examples:
*/3 08-13 10 06 * ~/crontest.sh # every 3 mins when on 10th of june at 8-13 o'clock
@reboot /usr/bin/say-hello.sh
```
- https://crontab.guru
## Bash parallel vs queue
- `time $(sleep 2; sleep 2)` - 4 seconds
- `time $(sleep 2 & sleep 2)` - 2 seconds

## sync time with inet
- `ntpd -qg` - sync (sometimes it does not work - try `ntpd -s -d`)
- `hwclock --systohc` - write os time to hardware clock

## netstat
- `netstat -tulpn | grep LISTEN` - you may need sudo to list ALL processes

## vim
- forget to sudo before editing
`:w !sudo tee %` - saves
`q!` - it was succesfully saved at prev step, now u can leave

## Default applications
- create .desktop file, e.g /usr/share/applications/firefox.desktop
```
[Desktop Entry]
Encoding=UTF-8
Type=Application
Terminal=false
Exec=/home/sean/Development/firefox/firefox %U
Name=Firefox Developer Edition
Comment=The COOL Browser from Mozilla
Icon=/home/sean/Development/firefox/browser/icons/mozicon128.png
```
- install it as default 
  - `xdg-mime default feh.desktop image/jpeg`
  - `xdg-settings set default-web-browser firefox.desktop` - https://wiki.archlinux.org/index.php/Xdg-utils#xdg-settings

## bash jobs
- you can send running command to daemon with CTRL + Z
- `jobs` to list all such jobs
- `fg %1` - to move process from daemon to foreground

## kick user from machine
- `pkill -KILL -u username`

## Fonts
1. yay fontpreview удобная cli утилита 
2. fc-match mono - show default mono font
3. fc-match : file - show font files

## st emoji crash
https://github.com/LukeSmithxyz/st/issues/162#issuecomment-597646558

## chrome casting to tv
chrome://flags/ -> Mirroring Service -> enable -> restart (мне не помогло)

## user-level systemd
- create unit file like here https://wiki.archlinux.org/index.php/Systemd/User#Example
- `systemctl --user daemon-reload` - for changes to work
- `systemctl start youservivce.service --user`

## pdf to png
- install imagemagick
- edit /etc/ImageMagick-6/policy.xml: там где pattern="PDF" - заменяем rights c "none" на "read|write"
- convert -density 150 input.pdf[0] -quality 90 first-page.pdf
- convert -density 150 input.pdf[7] -quality 90 eights-page.pdf
- convert -density 150 input.pdf -quality 90 all-document.pdf

## esc + v в консоли, чтобы редачить комманду в vim

## tee
`echo 1 | tee -a file.txt` - prints 1 and also writes 1 to file.txt (it  creates file.txt if it does not exist)

## imagemagick
- `convert -strip -interlace Plane -gaussian-blur 0.05 -quality 85% source.jpg result.jpg` - save with lower quality

## если нет vim
```
$ cat <<EOF > print.sh
#!/bin/bash
echo \$PWD
echo $PWD
EOF
```

## nmtui, nmcli (tools to manage NetworkManager)
- `nmcli connection show`
- `nmcli connection up <SSID>`
- `nmcli device wifi connect <SSID> password <password>` - another way to connect to wifi
- `nmcli device wifi list`
- `nmcli device wifi hotspot` - TODO проверить
- `nmcli wifi rescan`
- `nmcli radio wifi off` - turns wifi off
- `nmcli --show-secrets connection show "<SSID>" | grep wireless-security.psk` - show connection info with plain password (802-11-wireless-security.psk:)
- `nmcli dev show wlp0s2 | grep IP4.DNS` - see dns addresses, assigned via dhcp
- see man nmcli, examples section for more

## WPA2 enterprise nets (like WeWork) wifi connection
When using `nmcli device wifi connect 'WeWorkWiFi' password '...'`, you'll get something like:
```
Error: Failed to add/activate new connection: Failed to determine AP security information
```
To actually use it, you need to create a connection first and configure it:

```
nmcli connection add type wifi ifname <INTERFACE> con-name WeWorkWiFi ssid WeWorkWiFi
nmcli connection edit WeWorkWiFi
nmcli> set 802-1x.eap peap
nmcli> set 802-1x.phase2-auth mschapv2
nmcli> set 802-1x.identity <USERNAME>
nmcli> set 802-1x.password <PASSWORD>
nmcli> set wifi-sec.key-mgmt wpa-eap
nmcli> save
nmcli> activate
Ctrl + D
```

Then it will be connected.

## NetworkManager dns
## Settings
- `vim /etc/NetworkManager/system-connections/<connection>.nmconnection` - тут можно посмотреть пароли к wifi, например

### Changing dns to unmanaged
Default NetworkManager dns manage way is systemd-resolve, which has significant cons [1](https://cdnnow.ru/blog/dnslocal/) [2](https://moss.sh/name-resolution-issue-systemd-resolved/)
Best way is to change in to unmanaged [see](https://wiki.archlinux.org/index.php/NetworkManager#Unmanaged_/etc/resolv.conf)
1.
```
# /etc/NetworkManager/conf.d/dns.conf
[main]
dns=none
```
2. 
```
# /etc/NetworkManager/conf.d/no-systemd-resolved.conf
[main]
systemd-resolved=false
```
3. `sudo systemctl disable systemd-resolved.service`
4. `sudo rm /etc/resolv.conf` - it was a symlink to some systemd file
5. `sudo touch /etc/resolv.conf`
6. `sudo apt purge openresolv resolvconf` - removes openresonv and resolvconf
7. (optional) - fill /etc/resolv.conf with:
```
# /etc/resolv.conf
nameserver 1.1.1.1
nameserver 8.8.8.8
nameserver 8.8.4.4
```

## local dnsmasq
- `yay dnsmasq`
- in /etc/dnsmasq.conf
```
# /etc/dnsmasq.conf
server=1.1.1.1
server=2606:4700:4700::1111
listen-address=127.0.0.1
cache-size=10000
no-negcache
no-resolv
bind-interfaces
```
- /etc/resolv.conf
```
# /etc/resolv.conf
nameserver 127.0.0.1
```
- `sudo systemctl enable dnsmasq.service && sudo systemctl start dnsmasq.service`

## openresolv, resolvconf.conf
- `man resolvconf 8` - 8 is needed! man resolvconf opens man for resolvectl!
- openresolv package gives the resolvconf binary
- resolvconf is configured via /etc/resolvconf.conf
```
# /etc/resolvconf.conf
resolv_conf=/etc/resolv.conf
name_servers="1.1.1.1 8.8.8.8"
resolv_conf_options="timeout:1"
```
- `resolvconf -u` - force updates /etc/resolv.conf according to current config and state
- `echo -n "nameserver 1.1.1.1" | resolvconf -x -a tun0` - adds exclusive nameserver for a tun ip interface
- `resolvconf -d` - resets previously added nameservers

## brigtness
- `xrandr -q | grep ' connected' | head -n 1 | cut -d ' ' -f1` - prints your display (eDP-1 e.g)
- `xrandr --output eDP-1 --brightness 0.9`

## sort
- `ls -la -r --sort=time`
- `ls -la | sort -k2M -k3n -k4`

## bash range
- `echo {1..5}` - prints 1 2 3 4 5
- `echo {5..1..-1}` - prints 5 4 3 2 1
- `seq 1 5 | wc -l` - prints 5
- `seq 5 -1 1 | wc -l` - prints 5
- `seq 5 -1 1 | xargs -I {} touch file_{}` - creates file_1, file_2, ...
- `echo {a..z}`
- `seq -w 01 10` - prints 01\n02\n...
- `seq -s = 3` - prints 1=2=3
- `seq -f "%g/04/2018" 10`

## running in background
- `sleep 50` - run continuous job
- ctrl + z - to background job
- `sleep 50&` - to background job; all jobs will be killed with the end of terminal session
- `jobs` - list jobs
- `fg %1` - job #1 to foreground
- `nohup sleep 50&` - with nohup jobs and daemons will not be killed with the end of terminal session
- `less nohup.out` - echo output

## time
- время работы программы - это user + sys 

## Docker login via script (python)
```
proc = Popen(["docker", "login", "--password-stdin"], stdin=PIPE)
out, err = proc.communicate(my_password + "\n")
```

## Removing user from linux
- `who` - list if there is someone else on the server
- [optional] `sudo tar cfjv eric-20200820.tar.bz /home/eric` - archive user dir
- `sudo ls -lh /var/spool/cron/crontabs/eric` - list if there are cronjobs by eric
- `sudo crontab -r -u eric` - remove them
- `lprm -U eric` - remove pring jobs by eric
- `sudo userdel --remove eric` - for non-debian systems better to use this command (--remove removes home folder)
- `sudo deluser --remove-home eric` - for debian systems better to use this command

## chmod, umask
- `chmod +x .` - add execute for user
- `chmod g+wr file.txt` add write and execute for group
- `chmod g+s .` - add sticky bit for group (all new files and dirs in this dir will be created with group of . instead of with group of user)
- `umask 0002` - all new files will be created with 664 permissions (666 - 002), all new dirs will be created with 775 permissions (777 - 002)
- `find retail/ -type d -exec chown :shared {} \;` - change groups in all dirs inside retail to shared
- `sudo chown -R user:wheel .` - recursive chown inside current dir
- `find retail/ -type f -exec chmod g+x {} \;` - change permissions in all files inside retail - add execute to group

## thinkpad t14 no sound output problem
- tl;dr - create file and reboot
```
# /etc/modprobe.d/disable-dmic.conf
options snd_hda_intel dmic_detect=0
```
- links: [#1](https://bbs.archlinux.org/viewtopic.php?pid=1888464#p1888464) [#2] (https://bbs.archlinux.org/viewtopic.php?pid=1887925#p1887925) [#3](https://bbs.archlinux.org/viewtopic.php?pid=1888046#p1888046)

## anki server
- anki connect https://ankiweb.net/shared/info/2055492159

## cp
- `cp -r` - does not copy hidden files and dirs!
- `cp -r source/{.,}* destination/` - include hidden files and dirs
- `cp -rfT source destination` - same (include hidden files and dirs)

## cryptsetup, open encrypted disk when booted from other disk
- `sudo cryptsetup luksOpen /dev/sda4 crypthome1`
- `sudo mount /dev/mapper/crypthome1 /mnt`
- `sudo umount /mnt`
- `sudo cryptsetup close crypthome1`

## diff
- `diff file1 file2`
- `diff -q dir1 dir2`

## check which program is using port
- cat /etc/services | grep 3000
- netstat -tulpn (net-tools package needs to be installed)
- sudo lsof -i -P -n | grep LISTEN 
- sudo netstat -tulpn | grep LISTEN
- sudo ss -tulpn | grep LISTEN

## gzip
- `gzip -dk file.txt.gz` - ungzips file to file.txt

## sort
- `echo -n "file_bla_1213\nfile_bla_231" | sort -t _ -k3 -n -r` - `-t _` means divider, `-k3` means 3rd column in divided, `-n` means to treat strings as numbers, `-r` means reverse

## keyring
- https://wiki.archlinux.org/title/GNOME/Keyring#Installation
- install seahorse - gui app to manage keyring
- they're placed in ~/.local/share/keyrings

## bluetooth
- `modinfo btusb` (if module is loaded it shows something, if not - run `modprobe btusb`)
- yay bluez
- yay bluez-utils
- yay blueman
- start and enable bluetooth.service
- run blueman-manager

# wifi connectivity drops
- sudo pacman -S wireless_tools
- iwconfig wlp3s0 (power management is on? switch to off)
- sudo vim /etc/NetworkManager/conf.d/default-wifi-powersave-on.conf
```
[connection]
wifi.powersave = 2

```
- sudo systemctl restart NetworkManager
- https://bugzilla.kernel.org/show_bug.cgi?id=203709
-

# sync time automatically
- `sudo timedatectl set-ntp true`

# combine pdf
- yay pdfarranger

# zip
- pacman -S extra/zip
- zip -r folder.zip ./folder

# video cropping
- pacman -S extra/avidemux-qt
- video -> filters -> crop https://linuxhint.com/crop_videos_linux

# ch, jp, korean, etc fonts
- install these packages
```
adobe-source-han-sans-cn-fonts
adobe-source-han-sans-jp-fonts
adobe-source-han-sans-kr-fonts
adobe-source-han-serif-cn-fonts
adobe-source-han-serif-jp-fonts
adobe-source-han-serif-kr-fonts
aur/adobe-source-han-mono-cn-fonts
aur/adobe-source-han-mono-jp-fonts
aur/adobe-source-han-mono-kr-fonts
```

# create bootable windows usb
- https://kb.adamsdesk.com/operating_system/create_a_bootable_windows_10_usb_using_linux

