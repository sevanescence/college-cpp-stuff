import os
import subprocess
import sys

# (proposal) example invocation:
# $> py build.py hello_world.cpp -c clang++ -a "-Wall" 
# $> py build.py stack.cpp -c g++ -a "-O3 -Wall" -std=c++20

# alternative (changing default settings, store in local repo cache):
# $> py build.py --settings -c g++ -a "-Wall"
# $> py build.py --settings -c clang++ -a "-Wall -std=c++20" 

if len(sys.argv) < 2 or sys.argv[1] == "--help":
    print(
        "This program compiles a file in the examples folder and executes it.",
        "This program uses clang++ by default, but doesn't yet support specified alternatives nor custom compiler arguments.",
        "\n"
        f"{sys.argv[0]} [--help|<src>.cpp]",
        "",
        "    --help:\t Show this help screen.",
        "    <src>.cpp:\t Compile a file in ./examples/<src>.cpp",
        "",
        "Example:",
        f"py {sys.argv[0]} hello_world.cpp",
        "",
        sep='\n'
    )
    exit(1)

DEBUG_PATH = os.path.join(os.getcwd(), 'debug')
TARGET_SRC_FILE = os.path.join(os.getcwd(), 'examples', sys.argv[1])

DEFAULT_BIN_PATH_DEBUG = os.path.join(os.getcwd(), 'debug', 'a.exe')

if not os.path.exists(DEBUG_PATH):
    os.mkdir(DEBUG_PATH)

subprocess.run([
    "clang++",
    "-o",
    DEFAULT_BIN_PATH_DEBUG,
    TARGET_SRC_FILE,
    "-Wall"
])

subprocess.run([DEFAULT_BIN_PATH_DEBUG])
