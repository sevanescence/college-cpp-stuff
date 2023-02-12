# college-cpp-stuff
Repo for stuff I do for college in C++

# How to use
In order to run examples in the repo, I wrote a build script in Python to
handle building and running, which you will obviously need Python to run.

This script also requires clang, however in the future I will add support
for more compilers and probably figure out what compilers work on your machine.

## Usage
```
py build.py hello_world.cpp
```
Running this (while the current working directory is this repo) will build the
target file hello_world.cpp and run it, displaying the output wherever it was called.

Output:
```
Hello, world!
```
