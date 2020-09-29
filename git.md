# Git tips

## Config
- `git config --global credential.helper "cache --timeout=14400" --replace-all` - сохранит креды на 4 часа

## Cherry-pick
- `git cherry-pick <commit>` - moves commit to current branch

## Remotes
1. In github you can't fork from any commit - only from current commit of master
However, you can easily rollback to any commit in already forked repo:
- fork master
- `git clone`
- `git reset --hard <commit>`
- `git push -f origin master`

2. Change remote
```
git remote -v
git remote set-url origin https://github.com/USERNAME/REPOSITORY.git
```

## Tools
1. Meld - out of the box nice gui for watching diffs, merge and so on

## Revert
- !!! git revert работает не так, как ты ожидаешь
### Если ещё не запушил, и надо "перекоммитить" последний коммит:
```
(подробнее - https://stackoverflow.com/questions/927358/how-do-i-undo-the-most-recent-local-commits-in-git)
- git reset HEAD~
- git add
- git commit -c ORIG_HEAD
```
### Универсальный вариант
- `git checkout <последний нормальный коммит>`
- `git chechout -b <new branch>`
- `git cherry-pick -n <commit>` - по одному черри-пикать коммиты (начиная с самого раннего). -n - это значит не коммитить. Можно будет закоммитить "как надо"

## .gitignore
- set `*` to ignore all, then explicitly add files with `!.gitngnore` and so on
- hint! to add dotfolders you need to type `.i3` in root .gitignore, and add .i3/.gitignore with `!*` content

## See also
- https://jonas.github.io/tig/doc/manual.html - very nice TUI for git

## credential-helper
- ``
- `echo -ne 'username=username\nprotocol=https\nhost=github.com\n' | git credential-cache get` - prints saved creds (when `git config --global credential.helper "cache --timeout=3600"` is used)
- `git credential-cache exit` - forgets all saved passwords before to expires (new passwords will be saved)


## mics
- you can use token as password when git fetch
