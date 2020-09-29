## Firefox

### Editor keymap
- devtools.editor.keymap in about:config; select "vim", "emacs" or "sublime" (https://developer.mozilla.org/en-US/docs/Tools/Keyboard_shortcuts#Source_editor)
- vim is nice, but some keymaps does not work
- ctrl + c instead of esc to go to normal mode
- ctrl + r still reloads page

## Chrome

### Remote debugging
```
# полезно для дебага фронта киосков например
- на железке запускаем chrome с флагом --remote-debugging-port=9222
- на железке прокидываем ssh туннель коммандой " ssh -L 0.0.0.0:9223:localhost:9222 localhost -N" (нужно будет ввести пароль)
- открываем у себя <ip-железки>:9223
```
