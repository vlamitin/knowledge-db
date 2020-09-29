# How to make a site on domain with https

## Domain
- In your domain register account find domain dns settings and make A record to point to ip with your running web-server

## Https (letsencrypt)
- NB! run these commands on a machine, that is A record in domain dns settings 
- `yay certbot` - on arch
```
# on debian
apt install software-properties-common
add-apt-repository ppa:certbot/certbot
apt update
apt install certbot
```
```
# this will generate these certs to /etc/letsencrypt/live/mydomain.com:
# README  cert.pem  chain.pem  fullchain.pem  privkey.pem
# fullchain.pem is your pubkey, privkey.pem is your priv key
# NB! backup them!!!!
# and you can now use them in your web server

# on a running webserver on 80 port (let's say you don't want to stop it)
sudo certbot certonly --webroot -w /path/to/running/web-server -d mydomain.com -d www.mydomain.com

# without running webserver (80 port should not be occupied!
sudo certbot certonly --standalone -d mydomain.com -d www.mydomain.com
```

## updating expired keys
- `sudo certbot renew -d mydomain.com -d www.mydomain.com`
- `certbot certificates` - show info about certs (including expiration date)
- TODO see /etc/letsencrypt/live/mydomain.com/README

## using keys in your webserver
```
// in express like this:
const app = express();
app.use(express.static(__dirname + '/index.html'));
http.createServer(app).listen(80);
https.createServer({
   key: fs.readFileSync(__dirname + '/privkey.pem', 'utf8'),
   cert: fs.readFileSync(__dirname + '/fullchain.pem', 'utf8')
}, app).listen(443);
```
