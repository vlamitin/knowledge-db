# ssh, ssgfs, scp and others

## sshfs
- `sshfs user@server:dir /mnt/server`

## ssh
- `ssh -i /path/to/id_rsa user@ip` - with non-default keys location (нужно chmod 400 сделать)

## ssh-agent (to cache ssh passwords)
- `eval $(ssh-agent)` - start agent
- `ssh-add /path/to/id_rsa` - add key
- [more](https://wiki.archlinux.org/index.php/SSH_keys#SSH_agents)

## ssh key to github
- [instruction](https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
- to use custom key location `vim ~/.ssh/config` -> 
```
Host github.com
 IdentityFile ~/myPublicKeyFolder/myGitHubFile
```

## scp
- работает tab для автодополнения даже remote путей!
- `scp user@ip:/remote/path/from /local/path/to`
- `scp  /local/path/from user@ip:/remote/path/to`


## rsync
Copies only files missing in dir
#### TODO !!! https://github.com/kaihendry/media-organisation/blob/master/v2/2_sync-mysrctree.sh
```
# Suppose we have two directories: d, with one file, and s, with two files:

[me@mycomp]$ ls && ls ../s
f0
f0  f1

# Sync the directories (copying only missing data) with rsync:

[me@mycomp]$ rsync -av ../s/* .
[me@mycomp]$ ls
f0  f1
```
rsync can be performed over ssh as well:
```
[me@mycomp]$ ls

[me@mycomp]$ rsync -avz -e "ssh -p 22" root@137.xxx.xxx.79:~/s/* .
[me@mycomp]$ ls
f0  f1
```
## simplest file sharing
- `python2 -m SimpleHttpServer` or `python3 -m http.server` in dir to share and open xxx.xxx.xxx.xxx:8000 in browser

## netcat
- Computer A: `nc -l -p 1234 > filename.txt`
- Computer B: `nc {ip-of-computer-a} 1234 < filename.txt`

## NFS
- https://wiki.archlinux.org/index.php/NFS
- https://help.ubuntu.ru/wiki/nfs

### Server
- `yay nfs-utils`
- `mkdir -p /srv/nfs`
- `mount --bind /home/<username>/projects /srv/nfs`
```
# /etc/exports
/srv/nfs 192.168.1.62/24(rw,sync,nohide,all_squash,subtree_check,anonuid=1000,anongid=998)

# 192.168.1.62/24 - ip of client
# anonuid=1000,anongid=998 - нужно, чтобы пользователь совпадал, чекнуть можно в /etc/passwd TODO проверить!
```
- `exportfs -arv`
- `systemctl start nfs-server.service`

- `systemctl stop nfs-server.service`
- `umount /srv/nfs`

### Client
- `sudo apt install nfs-kernel-server nfs-common` - попробовать только nfs-common
- `showmount -e <server-ip>`
- `sudo mount -t nfs -o vers=3 <server-ip>:/srv/nfs /mouunting/point/on/client`

- `sudo umount /mouunting/point/on/client`

### troubleshooting
```
#/etc/nfs.conf, TODO я не понял, понадобилось это или нет
[nfsd]
host=<server-ip>
# Alternatively, use the hostname.
# host=myhostname (see in /etc/hostname)
```

## Samba
[nice article](https://lampjs.wordpress.com/2018/08/10/setting-up-samba-sharing-server-on-arch-linux/)

### Server

#### Setting up
- `yay samba`
```
# /etc/samba/smb.conf (create if not present)

[global]
   server min protocol = NT1
   server max protocol = SMB3
   
   workgroup = CUSTOMGROUPNAME

   server string = Samba Custom Server

   server role = standalone server

   log file = /var/log/samba/%m.log

   max log size = 50

   dns proxy = no 

[printers]
   comment = All Printers
   path = /usr/spool/samba
   browseable = no

   guest ok = no
   writable = no
   printable = yes

[myshare]
   comment = Username's stuff
   path = /srv/smb
   valid users = username
   public = no
   writable = yes
   printable = no
   create mask = 0765
```
- `smbpasswd -a username` - !!!! create samba user (should be one of system users) with its own password
- `groupadd sambashare`
- `usermod -aG sambashare username`
- `mkdir /srv/smb`
- `chown -R username:sambashare /srv/smb/`
#### Start
- `mount --bind share/ /srv/smb/`
- `systemctl start smb.service`
- `systemctl start nmb.service`
#### Stop
- `systemctl stop nfs-server.service`
- `umount /srv/nfs`

### Client
- `smbclient -L 192.168.1.118` - list shares (prompts smb passwd)
- `smbtree -b -N` - same, but broadcast
- `mount -t cifs //192.168.1.118/myshare /home/myusername/sambaserver -o username=username,workgroup=CUSTOMGROUPNAME,iocharset=utf8,uid=myusername,gid=sambashare` (you may need cifs-utils to be installed)

## FTP
- [curlftpfs](https://wiki.archlinux.org/index.php/CurlFtpFS)
- tl;dr - `curlftpfs ftp.example.com /mnt/ftp/ -o user=username:password`

# ngrok
- `ngrok http -auth "manager:password324012" 3000`
- `curl -H "Authorization: Basic bWFuYWdlcjpwYXNzd29yZDMyNDAxMg==" http://0bf217d2.ngrok.io/email/send -X POST`
or even
- `curl -X POST -H "Authorization: Bearer bWFuYWdlcjpwYXNzd29yZDMyNDAxMg" -H "Content-Type: application/json" -d '{"field1":"Test1","field2":"adada"}' http://0bf217d2.ngrok.io/email/send`

# check if host is available
- `ping {host}`

# check if host and port are available
- `echo >/dev/tcp/{host}/{port}`
- `echo >/dev/udp/{host}/{port}`

# simple socks5 proxy via other machine, to which you have ssh
- `ssh -N -D 9090 [USER]@[SERVER_IP]` - sets up tunnel. Now you can use localhost:9090 as local tunnel entry
- in firefox  network settings -> connection settings -> manual socks5 proxy -> localhost:9090

# tunnel remote port to local port
- `ssh -L 0.0.0.0:9000:server_ip:9222 [USER]@[SERVER_IP]` - sets up tunnel. Now you can use localhost:9090 to access server_ip:9222

# proxy local port to remote port
- (on remote machine) `ssh -L 0.0.0.0:8090:172.29.16.208:8090 localhost -N` - now when go on <remote-machine-ip>:8090 you'll be proxied to 172.29.16.208:8090
- you can also proxy one local port on another local port `ssh -L 0.0.0.0:9223:localhost:9222 localhost -N`  - now when go on <remote-machine-ip>:9223 you'll be proxied to <remote-machine-ip>:9222
 
## curl examples
- `curl -L -o file.txt http://server.com/some-file.txt` - download file with custom name. Warn! always pass -L when download files! (means to follow redirects)
- `curl -L -O http://server.com/some-file.txt` - download file with same name
- `curl -X POST -H "Authorization: Bearer bWFuYWdlcjpwYXNzd29yZDMyNDAxMg=" -H "Content-Type: application/json" -d '{"field1":"Test1","field2":"adada"}' ip:port`
- `curl -u 'your_username:your_password' -d @/tmp/request_data.json http://ip:port`
- `curl "https://music.mp3-download.best/UFUHW:ZjzZZ" -o song.mp3`

## proxying your outcoming traffic
- `docker run --rm -it -p 8080:8080 -p 127.0.0.1:8081:8081 mitmproxy/mitmproxy mitmweb --web-host 0.0.0.0` start mitmproxy with web interface localhost:8081
- `http_proxy=http://localhost:8080/ curl http://example.com/` or `https_proxy=http://localhost:8080/ curl -k https://example.com/` - to curl with proxy
- or set up firefox to use proxy https://docs.mitmproxy.org/stable/tute-clientreplay/#2-point-your-browser-at-the-mitmdump-instance

## nmap
- `nmap 192.168.1.0/24 -sP` - show hosts in local net

## nslookup
- `nslookup ya.ru 8.8.8.8` - second argument is the nameserver to use
- `nslookup ya.ru 192.168.1.1` - you can use your gateway's nameserver
- `nslookup ya.ru` - if omit ns server arg - the default will be used (first from resolv.conf)

