# Node hints

## Node debugging
- `sudo npm i -g chrome-remote-interface`
- `nvm use 12.3.1` - или любую версию начиная с 10
- `export NODE_PATH=/usr/lib/node_modules && node --experimental-repl-await`
- `NODE_OPTIONS=--inspect-brk=0 npm run test` - выведется порт, его даём в cri
- `connection1 = await cri({ port: 43637 })`
- `await connection1.Runtime.runIfWaitingForDebugger()`

## Memory
```
# increasing node memory limit (default is 512mb)
export NODE_OPTIONS=--max-old-space-size=2048
```
- добавить в .bashrc, чтобы дать ноде больше памяти (или запускать вот так: node --max-old-space-size=2048 file.js

## forever
- `forever start index.js` - starts index.js in daemon mode
- `forever list` - list all running scripts
- `forever stop [script|id|pid]` - stop script
