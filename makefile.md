# make, makefile

## vars from shell
- `contents := $(shell cat foo)`

## PHONY
- TODO

## prev jobs will be done sequentially
```
jobs: job1 job2 job3
  echo "jobs finished"
```
