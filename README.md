# college-cpp-stuff
A repository for stuff I do for college in C++.

## Usage

### With `make` (recommended)
In order to run examples in the repo, you will need a C++ compiler (like `g++` or `clang++`), together with `make`.

By default, the `Makefile` will use `clang++` as the compiler, but you can change this by setting the `CXX` variable to the compiler you want to use, just make sure that it supports `g++`'s command line arguments.

**Example:**
```sh
make hello_world.cpp
```

Running this (while the current working directory is this repo) will build the
target file hello_world.cpp and run it, displaying the output wherever it was called.

**Output:**
```
Hello, world!
```

### With `python3`
If you don't have `make` installed, but have `python3` installed, you can use the `build.py` script in the same way as `make`:
```sh
python3 build.py hello_world.cpp
```
It should produce the same results, building the target file and running it.

## License
The examples are licensed under the MIT License - see the [LICENSE](LICENSE) file for more details.