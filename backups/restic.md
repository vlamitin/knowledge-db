# restic cli

## docs
[aws example](https://restic.readthedocs.io/en/stable/080_examples.html#setting-up-restic-with-amazon-s3)

## cli
### Bootstrapping
- `useradd -m restic`
- `passwd restic`
- `mkdir /home/restic/bin`
- `curl -L https://github.com/restic/restic/releases/download/v0.9.1/restic_0.9.1_linux_amd64.bz2 | bunzip2 > /home/restic/bin/restic`
- `chown root:restic /home/restic/bin/restic`
- `chmod 750 /home/restic/bin/restic`
- `setcap cap_dac_read_search=+ep /home/restic/bin/restic`

#### Init aws restic repo
- `su restic`
```
$ export RESTIC_REPOSITORY="s3:s3.amazonaws.com/restic-demo"
$ export AWS_ACCESS_KEY_ID="blabla"
$ export AWS_SECRET_ACCESS_KEY="blabla"
$ export RESTIC_PASSWORD="blabla"
```
- `/home/restic/bin/restic init`

#### Init local (or sshfs) repo
- `su restic`
- `/home/restic/bin/restic init -r /home/restic/mnt/my_backup` !WARN add /home/restic/mnt to restic-excludes.txt!

### Backing up
#### To aws
- `su restic`
```
$ export RESTIC_REPOSITORY="s3:s3.amazonaws.com/restic-demo"
$ export AWS_ACCESS_KEY_ID="blabla"
$ export AWS_SECRET_ACCESS_KEY="blabla"
$ export RESTIC_PASSWORD="blabla"
```
- `/home/restic/bin/restic backup / --exclude-file=restic-excludes.txt`

#### To local (or sshfs) dir
- `/home/restic/bin/restic backup -r /home/restic/mnt/my_backup / --exclude-file=restic-excludes.txt`  !WARN add /home/restic/mnt to restic-excludes.txt!
