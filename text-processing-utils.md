# Gnu tools for processing text

- `printf "2\n2\n1" | uniq | sort` - prints 1 and 2
- `echo "134.1444" | cut -d '.' -f2` - like in js string.split('.')[1]

## sed
- `ls | sed -n '1,2p'` - prints 1st and 2nd line
- `echo "old" | sed s/old/new/` - prints new
- `echo "/home/user" | sed s#/home#/sweethome#` - prints "/sweethome/user" (any symbol can be delimiter)
- `echo "123 abc" | sed 's/[0-9]*/12 & &/'` - prints "12 123 123 abc" (12 because it was replaced, 123 - it was found (accesible via "&"), abc - rest of the string in the end)
- `echo "abc123" | sed 's/\([a-z]*\).*/\1/'` - prints abc ("/1 is the first found group")
- `sed "s/cf/LMAO/g" .bashrc` - replaces all cf with LMAO in .bashrc (and prints result)
- `sed -i "s/cf/LMAO/g" .bashrc` - replaces all cf with LMAO in .bashrc (and WRITES TO FILE)
- `sed "s/cf/LMAO/" .bashrc` - replaces cf with LMAO ONCE PER LINE in .bashrc
- `sed "s/#.*//g" .bashrc` - replaces comments with empty line
- `sed "s/#.*//g; /cf/ q" .bashrc` - replaces comments with empty line, but when it first find cf - quit
- `sed "s/\s#.*//g; /^$/ d" .bashrc` - replaces comments with empty line (also does same with comments not at the beggining of line), and deletes empty lines


## awk
- `printf "A 10\nB 20\nC 60" | awk 'BEGIN {sum=0; count=0; OFS=" "} {sum+=$2; count++} END {print "Average:", sum/count}'` - prints "Average: 30"
- `printf "1 2\n3 4" | awk '{print $2}'` - prints 2 and 4
- `ls -la | awk '$6 ~ /^A.*r$/ { print }'` - prints all lines, where 6th word is matching given regexp (Apr)
- `ls -la | awk '$6 ~ /^A.*r$/ && $7 > 25 { print }'`
- `awk 'BEGIN { for (x=0; x <= 255; x++) {print "192.168.1."x} }'`
- `awk -F: '{print $1}' /etc/passwd` - use ":" as separator
- `echo "Hello Tom" | awk '{$2="Adam"; print $0}'` prints Hello Adam
```
# if you do not close ' and hit Enter - you can continue write in next line:
ls -la | awk 'BEGIN {print "Title"}
{print $0}
END {print "Footer"}'
```
```
Given the following log:

User bill clicked one time.
User ted clicked one time.
User james clicked one time.
User bill clicked one time.
User bill clicked one time.
User henry clicked one time.
User socrates clicked one time.
User james clicked one time.
User bill clicked one time.
User andy clicked one time.

Run the following command:

awk '{name[$2]++} END{for (each in name) {print each " clicked " name[each] " time(s)"}}' phishlog.txt 

Output:

bill clicked 4 time(s)
...
```
