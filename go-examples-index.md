# Examples and tl;dr-s with links to expanded answers

## Best resources
- [https://www.programming-idioms.org/cheatsheet/Go](https://www.programming-idioms.org/cheatsheet/Go) - common code pieces on one page
- [https://learnxinyminutes.com/docs/go/](https://learnxinyminutes.com/docs/go/) - the very basics
- http://devs.cloudimmunity.com/gotchas-and-common-mistakes-in-go-golang/index.html
- https://golang.org/doc/effective_go.html#concurrency
- https://github.com/golang/go/wiki/CodeReviewComments

## Common
- Invoking method on nil does not NPE!
```
type MyContainerType struct {
	mt *MyType
}

type MyType struct {
	name string
}

func (mt *MyType) nameLen() int {
	if mt == nil {
		return 0
	}

	return len(mt.name)
}

var mtInstance MyContainerType = MyContainerType{nil}
fmt.Printf("this shall not NPE!!, but give 0 instead - %v\n", mtInstance.mt.nameLen())
```

## CLI
- `go mod download` - like npm install
- `go mod init github.com/username/new_project` - inits modules in current dir
- `go get github.com/go-swagger/go-swagger` - install package
- `go get -u github.com/go-swagger/go-swagger` - upgrade package
- `go run cmd/app/main.go` - compile and run
- `go build cmd/app/main.go -o main` - compile and create `main` binary with GOOS and GOARCH for current machine; -o is for setting output path with name (main would be default for main.go)
- `GOOS=windows GOARCH=amd64 go build -o main.exe cmd/app/main.go` - building binary for windows [GOOS and GOARCH options](https://www.digitalocean.com/community/tutorials/how-to-build-go-executables-for-multiple-platforms-on-ubuntu-16-04#step-4-%E2%80%94-building-executables-for-different-architectures) [the newer article on cross-compiling](https://www.digitalocean.com/community/tutorials/building-go-applications-for-different-operating-systems-and-architectures)
- `BUILD_TIME="$(date +%d.%m.%YT%H:%M:%S%z)" go build -ldflags "-X main.BuildTime=$BUILD_TIME" -o "service.go_$BUILD_TIME"` - setting build variables in build time via Makefile - [](https://stackoverflow.com/questions/11354518/application-auto-build-versioning/39378759#39378759)
- `go version`
- `go -h` - common help
- `go run -h` - particular command help

## Package structure
- if multimple cmd - every should be package main and have func main(){}!

## Strings
### - Common utils (lower, title, contains, join, split, index, replace)
```
x, y := "jey", 2123
strings.ToLower(fmt.Sprintf("hey %s %d", x, y)) // warn! Tolower may not work with not English text!
strings.Index("jey", "ey") // 1 (or -1, if not found)
strings.Split("jey", "")
strings.Contains("jey", "e")
```
- [https://golang.org/pkg/strings/#ToLower](https://golang.org/pkg/strings/#ToLower)
### - Format
#### -- Printing verbs
- [https://golang.org/pkg/fmt/#hdr-Printing](https://golang.org/pkg/fmt/#hdr-Printing)
### - String conversions
- `string(10)` - WARNING !!! RETURNS ""!!!
- `strconv.Itoa(10)` - int to string
- `strconv.Atoi("10")` - string to int

## Regex
https://golang.org/pkg/regexp/#example_Regexp_ReplaceAll
```
package main

import (
	"fmt"
	"regexp"
)

func main() {
	re := regexp.MustCompile(`a(x*)b`)
	fmt.Printf("%s\n", re.ReplaceAll([]byte("-ab-axxb-"), []byte("T")))
	fmt.Printf("%s\n", re.ReplaceAll([]byte("-ab-axxb-"), []byte("$1")))
	fmt.Printf("%s\n", re.ReplaceAll([]byte("-ab-axxb-"), []byte("$1W")))
	fmt.Printf("%s\n", re.ReplaceAll([]byte("-ab-axxb-"), []byte("${1}W")))
}
```

## Enums
```
type coverImageType string
const (
   cover coverImageType = "COVER"
   portrait coverImageType = "PORTRAIT"
)
```

## Functions
### - Functions as arguments
```
func searchIndex(items []string, predicate func(item string) bool) int {
  return -1
}
```

## Dates

```
currentTime := time.Now()
fmt.Println("Current Time in String: ", currentTime.String())
fmt.Println("MM-DD-YYYY : ", currentTime.Format("01-02-2006 15:04:05"))
fmt.Println("MM-DD-YYYY : ", currentTime.Format("02-01-2006 15:04:05"))

start := time.Now()
//...
t := time.Now()
fmt.Printf("elapsed: %dns\n", t.Sub(start))
```

## CSV
### - Write
```
file, err := os.Create("result.csv")
checkError("Cannot create file", err)
defer file.Close()

writer := csv.NewWriter(file)
defer writer.Flush()

for _, value := range data {
  err := writer.Write(value)
  checkError("Cannot write to file", err)
}

func checkError(message string, err error) {
    if err != nil {
        log.Fatal(message, err)
    }
}
```

## CLI options parsing

```
// flags.go
wordPtr := flag.String("word", "foo", "a string")
numbPtr := flag.Int("numb", 42, "an int")
boolPtr := flag.Bool("fork", false, "a bool")

var svar string
flag.StringVar(&svar, "svar", "bar", "a string var")

flag.Parse()

fmt.Println("word:", *wordPtr)
fmt.Println("numb:", *numbPtr)
fmt.Println("fork:", *boolPtr)
fmt.Println("svar:", svar)
fmt.Println("tail:", flag.Args())
----
$ go run flags.go -word=opt -numb=7 -fork -svar=flag
word: opt
numb: 7
fork: true
svar: flag
tail: []
```
- flag package [https://gobyexample.com/command-line-flags](https://gobyexample.com/command-line-flags)

## Files, dirs
- `file, err := os.Open('./file.txt')` - don't forget to defer file.Close()!
- `fileDataBytes, err := ioutil.ReadAll(file, 512)`
- `fileDataBytes, err := ioutil.ReadFile('./file.txt')` - closes file after read
- `fileInfo := file.Stat()`
- `fileInfos, err := ioutil.ReadDir('.')`
- `err := ioutil.WriteFile('./file.txt', []byte("hello world"), os.O_WRONLY|os.O_CREATE|os.O_TRUNC)`

## Troubleshooting
- `git config --global url."ssh://git@github.com/".insteadOf "https://github.com/"` - https://tip.golang.org/doc/faq#git_https - if "unknown revision ..." errors during `go mod download`
