# gpg

## common commands
- `gpg --version` >= 2.2.2 is fine
- `gpg --full-generate-key` - creates pub and priv keys. Rememeber passwd you entered while creating! Remember you user id (in will be constructed from name, email and comment (better to leave empty) and displayed to u). And set expiration date (it is sets for pub key) for not more than 3 months! It is easy to proexpired key (from edit menu)
- `gpg -k` - list pub keys
- `gpg -K` - list pub keys
- `gpg -k --keyid-format=LONG` to show key ids
- `tar -cf $HOME/gnupg-backup.tar -C $HOME .gnupg` - backuping everything

## Revocation certificate
- `gpg --gen-revoke --armor --output=revocation_certificate.asc your@email.com` - this will create it

## keyserver
- `gpg --keyserver hkp://keyserver.ubuntu.com:80 --send-keys <key-id>` - send it to server (see key-id here `gpg -k --keyid-format=LONG`) 
- `gpg --search-keys "alexey mitin"` - у меня не взлетело
- `gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys <pub key-id>` - get from server 


## Import / export public key
- `gpg --armor --export your@email.com > test1.asc` - export your public key
- `gpg --import test1.asc` - import it

## Import / export public subkey
- `gpg --keyid-format long --with-fingerprint --list-key user@gmail.com`
- `gpg --export --armor --output public-subkey.asc 633DBBC0!` # for id of subkey with "!"
- `gpg --import public-subkey.asc` - import it

## Import / export private key
- `gpg --export-secret-keys <id of private key, smth like 505B17, but over 30 chars> > my-test1-private-key.gpg` - export your private key, see private key ID here `gpg -K` (you will be prompted to enter your gpg passwd)
- `gpg -a --export-secret-subkeys [subkey id]! > subkey.gpg` - export subkey (! is required!!!)
* edit-key -> trust -> 5 needed after fresh import!
- `gpg --import my-test1-private-key.gpg` - import it (you will be prompted to enter your gpg passwd)

## encrypting / decrypting 
- `gpg -r your@email.com --armor --encrypt test1.txt` - this will create test1.txt.asc
- `gpg -R your@email.com --armor --encrypt test1.txt` - this will not show user id in encrypted text
- `gpg -r 0x<key or subkey id>! -a -e test1.txt` - encrypt with key specified
- `gpg --output test1decrypted.txt --decrypt test1.txt.asc` - you will be prompted to enter you gpg password

## Verifying signature (common public key needed - see import/export)
- `gpg --output test1.txt.sig --detach-sig test1.txt` - this will create test1.txt.sig
- `gpg --verify test1.txt.sig` - test1.txt should be in same dir

## Deleting keys
- `gpg --delete-secret-keys your@email.com` - you will be prompted multiple times =)
- `gpg --delete-keys your@email.com` - you will be prompted once

## edit existing key
- `gpg --expert --edit-key your@email.com` - this will open gpg console
- `key <n>` - toggle selection of subkey
- `addkey` - add subkey (choose RSA and you can select auth, sign and encrypt capabilities)
- `expire` - change expiration date (only pub keys can expire)
- `save` - save changes and exit editing
and don't forget to send changed keys to keyserver!

## ecrypt password file
- `gpg -e -a -R <user-id> your_password_file.txt` (in a password file it is needed for 1 blank line after passwd)

## using gpg for ssh auth (it is not as simple as it might be)
- [ssh workflow here](https://www.linode.com/docs/security/authentication/gpg-key-for-ssh-authentication/)
- [or here](https://ryanlue.com/posts/2017-06-29-gpg-for-ssh-auth)
- `gpg --export-ssh-key your@email.com` (or from subkey with Auth enabled)
* as for me - it is too much complicated (better to keep ssh keys separate from this)

## Troubleshooting
- `-v --debug lookup` - show extended output
- mb try to type 'trust' to pub key (from edit menu)

## security tips
- change passwd every time you import secret key or subkey
- the less expire period - the better security

## common workflow
- https://wiki.debian.org/Subkeys

## update expired key workflow
- backup!
- edit-key
- expire
- export public key (with encryption!)
- import public key

## signing git commits with sign subkey
- `gpg --keyid-format long --with-fingerprint --list-key`
- `git config --global user.signingkey 0BASDFASFASFA\!` - note "\! at the end"
- `git commit -S -m "bla"`
- `git log --show-signature -1`
- add your public signing [S] subkey to github/gitlab to show that commits were veryfied [1](https://docs.gitlab.com/ee/user/project/repository/gpg_signed_commits/) [2](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/signing-commits) [3](https://confluence.atlassian.com/bitbucketserver/using-gpg-keys-913477014.html)

## miscellaneous
- `nc -l -p 5555 > file.txt` - start listening and receive file
- `nc <ip> 5555 < file.txt` - transfer to host
- `openssl aes-256-cbc -a -salt -in file1.txt -out file.txt.enc` - simple file encryption with password (useful for transf with nc)
- `openssl aes-256-cbc -d -a -in file.txt.enc -out file.txt.new` - decrypt
- `alias pss="pass | sed 's/├── //g' | sed 's/└── //g' | dmenu | xargs pass | xclip"` - add to .bashrc; usage: `pss` to clip to shift+inserv clipboard; `pss -sel clip` - to ctrl+v clipboard
- `openssl rand -base64 14` - рандомный хэш
- https://habr.com/en/post/479540/

# encrypt / decrypt with ssh key
- [source](https://ati.ttu.ee/wiki/e/index.php/SSH_encrypt_and_decrypt#To_encrypt)
- let's say you already have ~/.ssh/id_rsa and ~/.ssh/id_rsa_pub, and you want to use them to encrypt/decrypt messages or text files
- it's not possible to use id_rsa and id_rsa_pub as-is, so you'll need to create new pair on top of old ones:
  * `mkdir ~/.ssh-encrypt && cd ~/.ssh-encrypt`
  * `cp ~/.ssh/id_rsa ~/.ssh-encrypt/id_rsa.pem`
  * `ssh-keygen -p -m PEM -f ~/.ssh-encrypt/id_rsa.pem`
  * `ssh-keygen -f ~/.ssh/id_rsa.pub -e -m pkcs8 > ~/.ssh-encrypt/id_rsa_pub.pkcs8`
- so, you now have ~/.ssh-encrypt/id_rsa_pub.pkcs8 (public) and ~/.ssh-encrypt/id_rsa.pem (private) keys for encryption
- `cat message.txt | openssl rsautl -encrypt -pubin -inkey ~/.ssh-encrypt/id_rsa_pub.pkcs8 > message.enc` - encrypts your text file
- `cat message.enc | openssl rsautl -decrypt -inkey ~/.ssh-encrypt/id_rsa.pem > message.txt` - decrypts it
- [gist with more examples](https://gist.github.com/colinstein/de1755d2d7fbe27a0f1e)
