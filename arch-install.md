# Arch install c шифрованием на комп с UEFI на весь физический диск

## Интернет
- Если воткнулись через провод, то инет уже должен быть как в режиме с iso, так и сразу после установки
- Если через wi-fi, то wifi-menu, дальше следуем командам, там все просто. Но после установки инета не будет. Так что нужно преднастроить его, пока сидим с iso.
## Шрифты покрупнее - так будет комфортнее
- `pacman -Sy terminus-font`
- `setfont /usr/share/kbd/consolefonts/ter-v??.gz` - выбираем какой-нить шрифт покрупнее
## Запись образа на флешку
- (Чтобы понять какой из /dev/sdX - наша флешка) - `ls -1 /dev/sd?` -> вставили диск -> повторили. USB - это новая (пусть sdc)
- `dd if=Downloads/arch<...>.img of=/dev/sdc status=progress bs=16M`
## Подготовка диска
### Удаляем все с диска
- Если на диске есть партишны, то удаляем их утилитой gdisk (gdisk /dev/sdX -> d -> 1 -> d -> 2 -> d -> w)
- [Полный гайд](https://wiki.archlinux.org/index.php/Dm-crypt/Drive_preparation#Secure_erasure_of_the_hard_disk_drive) всё с диска (открыть для контроля, вдруг там апдейт)
- `cryptsetup open --type plain -d /dev/urandom /dev/sdX to_be_wiped` - создаст ВРЕМЕННЫЙ криптконейтер для удаления в корневом partition sdX, смапленный на сам sdX
- `lsblk` - смотрим, должен создасться 'to_be_wiped' как ребенок sdX
- `dd if=/dev/zero of=/dev/mapper/to_be_wiped status=progress bs=2038` - заполняем весь диск нулями
- `cryptsetup close to_be_wiped` - закрываем криптконтейнер

### устанавливаем точное время
`timedatectl set-ntp true`

### Готовим партишны
- lsblk или fdisk -l, смотрим на какой диск (sda / sdb / ...) мы хотим установить arch.
- gdisk /dev/sdX, далее следуем командам
- Что мы хотим от gdisk? Сначала создать таблицу (`o`), затем `n` для каждого нового partiton, `p` можно юзать чтоб узнать текущий статус, `w` в конце все запишет)
- понадобятся коды для каждой из систем - можно посмотреть через L, потом вводим в поиск (EFI, swap, root, home)
создаём вот так:
```
/dev/sda/sdX1 - efi - 512MB
/dev/sda/sdX2 - swap - 100-150% от RAM, например 12G
/dev/sda/sdX3 - root - 20-50G (30 достаточно)
/dev/sda/sdX4 - home - всё остальное
```
## Шифруем диски
### Шифруем root
- [Полный гайд](https://wiki.archlinux.org/index.php/Dm-crypt/Encrypting_an_entire_system#LUKS_on_a_partition)
- `cryptsetup -y -v luksFormat /dev/sdX3` - создаём защищенный раздел и устанавливаем пароль на partition, куда будем маунтить /
- `cryptsetup open /dev/sdX3 cryptroot` - открываем созданный раздел и маппим его на /dev/mapper, после этого на partition обращаемся не напрямую (/dev/sdX3), а через маппер (/dev/mapper/cryptroot)
- `mkfs.ext4 /dev/mapper/cryptroot` - форматируем root в ext4
- `mount /dev/mapper/cryptroot /mnt` - монтируем его в /mnt

Можно проверить, что маппинг работает:

- `umount /mnt` - размонтирываем
- `cryptsetup close cryptroot` - закрываем раздел 
- `cryptsetup open /dev/sdX3 cryptroot` - открываем заново, но теперь по mapping-имени
- `mount /dev/mapper/cryptroot /mnt` - монтируем root в /mnt

### Шифруем home
- [Полный гайд](https://wiki.archlinux.org/index.php/Dm-crypt/Encrypting_a_non-root_file_system#Partition)
- `cryptsetup -y -v luksFormat /dev/sdX4` - создаём защищенный раздел и устанавливаем пароль на partition, куда будем маунтить /home
- `cryptsetup open /dev/sdX4 crypthome` - открываем созданный раздел и маппим его на /dev/mapper
- `mkfs.ext4 /dev/mapper/crypthome` - форматируем home в ext4
- `mkdir /mnt/home && mount /dev/mapper/crypthome /mnt/home` - монтируем его в /mnt

### Маунтим руками boot
- `mkfs.fat -F32 /dev/sdX1`
- `mkdir /mnt/boot`
- `mount /dev/sdX1 /mnt/boot`
#### Делаем swap и включаем его
- `mkswap /dev/sdX2`
- `swapon /dev/sdX2`
### Устанавливаем arch
- `pacstrap /mnt base linux linux-lts linux-firmware base-devel vim` - установит нужные пакеты из packages base, base-devel, а также vim
### Генерим fstab на основании /mnt
- `genfstab -U /mnt >> /mnt/etc/fstab`
### чрут
- `arch chroot /mnt /bin/bash` - чрутимся из загрузочной флешки в arch, установленный в /mnt (выйти назад можно через ctrl + d)
### Добавляем в ядро поддержку шифрования
- в файл /etc/mkinticpio.conf добавляем encrypt в HOOKS [возможно, нужны и другие хуки](https://wiki.archlinux.org/index.php/Dm-crypt/Encrypting_an_entire_system#Configuring_mkinitcpio) - приводим к виду HOOKS=(base udev autodetect keyboard keymap consolefont modconf block encrypt filesystems fsck)
### Устанавливаем и настраиваем boot manager
- `bootctl install` - установит boot manager (говорят он лучше глючного grub)
- после можно проверить ls /boot, что там initramfs и vmlinuz
- редактируем /boot/loader/loader.conf, туда руками пишем
```
default  arch
timeout  4
```

- и редактируем /boot/loader/entries/arch.conf, туда руками пишем
```
title   Arch
linux   /vmlinuz-linux
initrd  /initramfs-linux.img
options rw cryptdevice=UUID={UUID`*`}:cryptroot root=/dev/mapper/cryptroot
# * - сюда вставляем UUID, полученный через :r!blkid нашего /dev/sdX3 (который root) см https://wiki.archlinux.org/index.php/Dm-crypt/Encrypting_an_entire_system#Configuring_the_boot_loader
```
- потом добавляем ещё одно для lts ядра /boot/loader/entries/arch-lts.conf
```
title   Arch-lts
linux   /vmlinuz-linux-lts
initrd  /initramfs-linux-lts.img
options rw cryptdevice=UUID={UUID`*`}:cryptroot root=/dev/mapper/cryptroot
# * - сюда вставляем UUID, полученный через :r!blkid нашего /dev/sdX3 (который root) см https://wiki.archlinux.org/index.php/Dm-crypt/Encrypting_an_entire_system#Configuring_the_boot_loader
```

- `mkinitcpio -p linux` - пересобираем ядро


## locale and localtime and networkmanager
- edit /etc/locale.gen, раскомменчиваем en-US UTF-8 и ru-RU UTF-8
- `locale-gen`
- set LANG in locale.conf
```
/etc/locale.conf
LANG=en_US.UTF-8
```

- `ln -sf /usr/share/zoneinfo/Europe/Moscow /etc/localtime`
- `hwclock --systohc`

- `echo arch-pc >> /etc/hostname`
- `echo "127.0.1.1 localhost.localdomain arch-pc" >> /etc/hosts`
- `echo "127.0.1.1 localhost" >> /etc/hosts`

- `pacman -S networkmanager`
- `systemctl enable NetworkManager`

- `passwd` - задаст пароль для root пользователя
## Добавляем home в crypttab
- edit /etc/crypttab
```
crypthome UUID={*} none luks
# * :r!blkid /dev/sdX (home)
```

## exit to usb, umount, shutdown
- umount -R /mnt
- вытаскиваем флешку и включаем
## После перезугрузки включить wifi можно через nmcli (включена в поставку networkmanager)
- `nmcli device wifi list` - список
- `nmcli device wifi connect {SSID} password`


## Полезные ссылки:
- [Оф гайд](https://wiki.archlinux.org/index.php/installation_guide)
- [Johe news](https://www.youtube.com/watch?v=jF_24AUqyKU)
- [Luke Smith](https://www.youtube.com/watch?v=4PBqpX0_UOc)
- [7 min Kai Hendry](https://www.youtube.com/watch?v=DfC5hgdtbWY)
- [Avg linux user](https://www.youtube.com/watch?v=dOXYZ8hKdmc)


## TODO!
- [нужно как-то найти способ настроить UEFI SecureBoot без майкрософтовской подписи](https://habr.com/ru/post/457542)
