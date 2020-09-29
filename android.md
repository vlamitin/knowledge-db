# Android tips

## adb common
- `adb tcpip 5555` - switches adb instance to tcp mode
- `adb connect DEVICE_IP:5555`
- `adb usb`- switches adb instance to usb mode

## adb shell
- https://developer.android.com/studio/command-line/adb#shellcommands
- `adb -s 192.168.1.33:5555 shell am start -a android.intent.action.CALL -d tel:+79999999999` - call from desktop
- `adb -s device:asebe shell am start -a android.intent.action.CALL -d tel:+79999999999` - same, but using device id instead (`adb devices -l`)
- `watch -n 15 <command>` - execute command every 15s
- `for i in {1..10}; do echo -n "This is a test in loop $i "; date ; sleep 5; done`
- `adb -s device:asebe disconnect`
- `adb -s 192.168.1.33:5555 disconnect`

## scrcpy
- `scrcpy` - starts (you may need to press "ok" on android device)
- [also works wirelessly](https://www.genymotion.com/blog/open-source-project-scrcpy-now-works-wirelessly/)
- 
