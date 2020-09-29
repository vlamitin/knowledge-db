# Disk utils

## Formatting flash card

1. `fdisk /dev/sdc`
2. `d` for deleting old partition, `n` for creating partition (primary), `w` to write
3. `mkfs.ntfs /dev/sdc1`
4. `mount /dev/sdc1 /mnt/usb`

## Mount iso
- `sudo mount -o loop ubuntu-16.10-server-amd64.iso /mnt/iso`
