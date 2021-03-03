# Idea Hints

- All config is placed in ~/.IntelliJIdea2018.2
- wrong encoding in .properties files (flex) [utf-8 to win-1251](resources/screenshots/Screenshot%20from%202019-06-05%2017-25-53.png)

## shortcuts
- not `close active tab`, but `close`!
- `Shift + Shift` - search everywhere (classes, files, recent files, actions, run configurations etc)
- `Ctrl + E` - recent files
- `Shift + E` - recentty edited files
- `SET UP!` - navigate backward and forward (without tabs!)
* Tip! Do not use tabs! Use "Recent files"
- `ctrl + N` - create!
- create file -> `folder1/folder2/file.txt`
- `Shift + Ctrl + F12` - toggle giding all panels
- `Shift + Ctrl + left/right` - resize project view panel
- `Shift + Ctrl + V` - clipboard history
- `Ctrl + Alt + I` - auto-indent selected
- `Alt + Enter` - quich actions (open code style options for selected code, check RegExp, reformat and so on)
- `Ctrl + Shift + A` - menu of actions (type "main menu" to show main menu, if hide it in view -> appearance)
- `Ctrl + Alt + S` - settings
- `Ctrl + F2` - stop current run or debug proces

## JS
- disable `__dirname/node_modules` library (in languages - js - libraries) caused unabling to go to definition of library function in new idea versions (2020.1). So, I enabled it
- https://www.jetbrains.com/help/idea/typescript-support.html#

## gradle setttings for java project
- gradle user-wide: `echo "org.gradle.jvmargs=-Xmx4g -Xms2g -XX:MaxPermSize=256m -XX:+HeapDumpOnOutOfMemoryError -Dfile.encoding=UTF-8" > ~/.gradle/gradle.properties`
- gradle project-wide: idea -> settings -> gradle -> xmx 4096m
- idea: `vim idea/idea-IU-191.6707.61/bin/idea64.vmoptions`: `-Xmx4g -Xms2g`
