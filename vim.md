- `zt`, `zz`, `zb` -  scrolls the screen so that the line you're in to the top/middle/bottom
- `f(` - goes to '(' in line
- `t(` - goes to position 1 SYMBOL BEFORE '(' in line
- `r` for sigle replace character
- `R` for replace mode
- `;` - repeats `f` command
- `vi(` - selects inside '()'
- `vap` - selects all(with spaces or extra lines) paragraph
- `ctrl + v` - selects square block of text.
- Userful to paste smth to start of line (like `#` to comment in script) (`ctrl + v` + `jjjjj` + `I` + `# ` + `Esc`) (same but `jjjjjl` + `d` to delete)
- To paste to end of every line: `ctrl + v` + `jjjj` + `$` + `A` + `some text` + `esc`
- also works with " and ', but even better - you shouldn't be inside them to make it work; 
- another way - do it on the first line (`I# <Esc>`), then `ctrl + v` and select some lines, then type `:` = you'll see than `:'<,'>` is already typed, so just change in to `:'<,'>norm .` to repeat that to every line. Or `:'<,'>norm I #`
- `%` - go to matching parenthesis
- `ciw` - changes inside (without spaces) word
- so, diw and daw are delete inside word (without spaces) and delete around word (with spaces). 
- `.` - repeat last action
- `V` - selects current line
- `o` - starts new paragr and brings you to insert mode (same as `A<Enter>`); `O` - same, but goes to prev line
- `ctrl + v` - selects block (multiplies caret!)
- `}` - forward 1 paragraph
- `u` - undo
- `ctrl + r` - redo
- `M` - middle of screen
- `H` - top of the screen
- `ctrl + d` - page down
- `ctrl + u` - page up
- `D` - same as d$
- `$` for end (like in regex) and `^` or `0` for start of line
- `{` and `}` for prev and next paragraph (\n\n)
- `:earlier 5m` - возвращает документ (и cursorPosition)  к состоянию 5 минут назад. `:later 15m`
- `:sort`
- `:s/old/new/g` - like sed - replaces `old` with `new` in one line;
- `:%s/old/new/g` - whole file;
- `%s/old/new/gc` - whole file, ask every occurence 
(https://vim.fandom.com/wiki/Inserting_text_in_multiple_lines)
- `:s/^/new text /g`  Insert "new text " at the beginning of each line
- `:s/$/ new text/`  Append " new text" to the end of the line.
- `:s/green/bright &/g` - Replace each "green" with "bright green" in the line.
- [more on replacing in visual mode](https://vim.fandom.com/wiki/Search_and_replace_in_a_visual_selection)
- `:set paste` to turn off adding spaces when pasting
 
- maps replace command to `S`
```
nnoremap S :%s//g<Left><Left>
```
- `:!ls` - just executed this command and prints result (document is not edited)
- `:r!ls` - prints the output of command under the line you're in
- 

In insert mode (https://vim.fandom.com/wiki/Making_Parenthesis_And_Brackets_Handling_Easier) when type ( pastes () and goes inside; when ctrl + j = esc + A

```
:inoremap ( ():let leavechar=")"<CR>i
:inoremap [ []:let leavechar="]"<CR>i
:inoremap { {}:let leavechar="}"<CR>i
:imap  :exec "normal f" . leavechar<CR>a
```

- `:set hlsearch` - sets mode, where every searched occurence is highlighted; there're many such modes (`:set ic` to ignore case when search). You can set them from editor in editor console (like so `:set ic`, `:set noic` and completion works!!!) or in you .vimrc file (like so `set ic`)
