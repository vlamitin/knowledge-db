# Pacman short man
(all should be run as root)
1. pacman -S <package>
2. pacman -Suy (like apt update && apt upgrade) - download and update all packages
2.1. `yay -Suy --devel` - updates -git packages too
2.2 `pacman -S package` - update package. Still, this will not work, if package was installed fron AUR.
2.3 `yay -S package` - update package. Properly works for all (AUR too) packages.
3. pacman -Ss <package or regexp to search> - search for package (example: pacman -Ss ^emacs - searches packages that start with emacs)
4. pacman -Rns <package> - remove package with its dependencies (s) and dot-config files (n)
5. pacman -Q - queries for installed packages
5. pacman -Q package - show package along with version
5. pacman -Q --info package - show package full info (with packages, that requires this package)
5. pacman -Qi pachage - show package and its info: dependencies, size, licence etc
5. pacman -Qo /path/to/file - which package owns a file
6. pacman -Qe - only installed by user (not dependencies or system packages) packages
7. pacman -Qdt - orphaned (not used) dependencies - progs that you can uninstall
8. pacman -Sc - clear old packages from cache (locally installed old versions of packages) (cleans /var/cache/pacman/pkg)
8.1 it is better to use yay -Sc - it also cleans aur packages in ~/.cache/yay

/etc/pacman.conf
you probably want to decomment these:
Color - coloredd formatted output
CheckSpace - check disk space before install a package

/etc/pacman.d/mirrorlist
you probably want to change the order of urls (more avalable and those with less ping to the top)

## Errors when upgrading
1. error: failed to commit transaction (conflicting files)
example: python-pygments: /usr/bin/pygmentize exists in filesystem

https://forum.manjaro.org/t/package-installation-says-filename-exists-in-filesystem-failed-to-commit-transaction-conflicting-files/4382
(tl; dr: check pacman -Qo who owns file (or google it like this 'linux "/usr/bin/wheel"' to find page like this https://www.archlinux.org/packages/community/any/python-wheel/files/ - if this is the package then update it manually like this sudo pacman -S python-wheel --overwrite /usr/bin/wheel)

## Broken package, downgrade to version (example with ttf-inconsolata font)
1. Downgrade `ttf-inconsolata` to older version
sudo pacman -U https://archive.archlinux.org/packages/t/ttf-inconsolata/ttf-inconsolata-1%3A2.0.0.1-3-any.pkg.tar.xz
sudo pacman -U /var/cache/pacman/pkg/firefox-79.....pkg.tar.zst

2. Tell pacman to ignore auto-upgrading ttf-inconsolata in the future.
add "IgnorePkg = ttf-inconsolata" /etc/pacman.conf (TO 'options' section!)

## Pacman cache
- https://wiki.archlinux.org/index.php/pacman#Cleaning_the_package_cache
- td dr: install pacman-contrib  and run `paccache -r`

## MOre
- [archwiki_Tips](https://wiki.archlinux.org/index.php/Pacman/Tips_and_tricks)
