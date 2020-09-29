# Utils for text or file search

## grep
- `grep "root" /etc/passwd` - search text in file
- `grep "^export\sPS[0-9]" .bashrc` - you can use full power of regexp to find string (this one finds 'export PS1')
- `find . -maxdepth 1 -type f -exec grep "export PS1" {} \;` - the only way to use maxdepth - is combining with find (this will print found line)
- `find . -maxdepth 1 -type f -exec grep -l "export PS1" {} \;` - same as prev, but prings file path (`grep -l`)
- `ls -la | grep -E 'profile|history'` - -E is egrep - some new syntax (like here - profile of history)
- `grep -li "moment" $(find . -name "*.tsx" -exec grep -li "mobx" {} \;)` - print filepaths of all tsx files that contain 'mobx' AND 'moment'
- `grep -ril 'vladimir' projects`
- `grep -r text` - will find "text" in content of files in current folder recursively
- `zgrep weather files.tar.gz` - searches in gzipped files

## fd
Useful substitute for find - it can ignore .git, .node_modules and so on
- `fd --hidden --follow --no-ignore --exclude ".git" --exclude "node_modules" price-tags .` - searches "price-tags" pattern in ".", excluding .git, node_modules, including hidden files, following links

## fzf
`export FZF_DEFAULT_COMMAND='ifinstalled fd && fd --hidden --follow --no-ignore --exclude ".git" --exclude "node_modules"'` - add this to .bashrc to use fd (need to install) in search
- `fzf | xargs bash -c '</dev/tty vim "$@"' zero` - search and edit in vim

## find
- `find . -iname "readme.md"` - case-insensitive search
- `find / -name "foo.*" -type f` - find files by wildcards
- `find / -name bin -type d` - find dirs
- `find . -type f -iname "*.html" -not -iname "index.html"` - find html files except index.html
- `find . -type f -name "*.java" -exec grep -l StringBuffer {} \;` - find "StringBuffer" in all *.java files
- `... grep -il ...` - same, but ignore case
- `find . -type f -name "*.gz" -exec zgrep 'GET /foo' {} \;` - search for a string in gzip'd files
- `find . -name "*.json" -exec file {} \;` - find jsons and exec `file` command on them
- `find . -mtime 1` - find all files, modified in last day (24 hours)
- `find . -type f -name "*.java" | xargs tar cvf myfile.tar` - find and tar
- `find . -not -path "./node_modules/*" -type f -name "index.html"` - you cat exclude only explicitly, not by pattern. To exclude all dirs with 'node_modules' pattern in path you need to use `fd`

## See also
- https://github.com/BurntSushi/ripgrep - faster and more convenient grep

## Replace
- https://github.com/comby-tools/comby !! nice tool to replace in code
