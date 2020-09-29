# Virtualbox hints

vbox additions for debian
https://www.linuxbabe.com/desktop-linux/how-to-install-virtualbox-guest-additions-on-debian-step-by-step

включить shared clipboard и другие плюшки можно на включенной машине через tab devices

## Nat network
- ping host from guest: `ping 10.0.2.2`
- ping guest from host: `ping 10.0.2.15`
- (https://bertvv.github.io/notes-to-self/2015/09/29/virtualbox-networking-an-overview/)

## Vmware
[install](https://wiki.archlinux.org/index.php/VMware#Package_build_for_x86_64)

## Vagrant building and starting
- Полезные команды: `vagrant up`, `vagrant global-status`, `vagrant port`, `vagrant reload`, `vagrant destroy`
- прописать в Vagrantfile `config.vm.network "forwarded_port", guest: 8090, host: 8090`, если не форварднётся по дефолту и сделать `vagrant reload <id>`
