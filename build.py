import os
import subprocess
import sys

from argparse import ArgumentParser
import shutil

if os.name == 'nt':
    TARGET_BIN_FILENAME = 'target.exe'
else:
    TARGET_BIN_FILENAME = 'target.out'

# alternative (changing default settings, store in local repo cache):
# $> py build.py --settings -c g++ -a "-Wall"
# $> py build.py --settings -c clang++ -a "-Wall -std=c++20" 

# TODO: Add support for custom compiler arguments

# -- argparse boilerplate --

parser = ArgumentParser(
    prog=sys.argv[0],
    description='Build script for college-cpp-stuff',
    epilog='If any issues with this script are found, the user is at ' 
           'liberty to open an issue thread on the GitHub repository. '
           'https://github.com/MakotoMiyamoto/college-cpp-stuff '
           'NOTE: Multi-word filepaths are not currently supported.'
)
parser.add_argument('file', nargs='?', help='driver file of the program (where main() is defined). Parent folder specified by --file-dir')
parser.add_argument('-c', '--cxx', help='path to compiler to call (default: clang++)', default='clang++', type=str, nargs=None)
parser.add_argument('-f', '--file-dir', help='directory of source folder', default='./examples/')
parser.add_argument('-b', '--build-dir', help='build directory', default='./debug/')
parser.add_argument('-n', '--build-only', help='compile without running target', action='store_true')

parser.add_argument('--clean', help='clean target build directory', action='store_true')

# --

# -- Program Logic --

args = parser.parse_args()

build_dir: str = str(os.path.abspath(args.build_dir))
file_dir: str = str(os.path.abspath(args.file_dir))
file_src: str = args.file
cxx: str = args.cxx

proceed_clean: bool = args.clean
build_only: bool = args.build_only

if proceed_clean:
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
    else:
        print("Folder tree is already clean.")
    exit(0)

print(args, build_dir)

if file_src is None:
    print('Error: Missing target source file.')
    parser.print_help()
    exit(1)

source_filepath = os.path.join(file_dir, file_src)
target_filepath = os.path.join(build_dir, TARGET_BIN_FILENAME)

if not os.path.exists(build_dir):
    os.mkdir(build_dir)

# NOTE: Only works with g++ and clang++, I don't plan on adding support for other compilers.
compiler_args = f'{cxx} -Wall -std=c++20 -o {target_filepath} {source_filepath}'

subprocess.run(compiler_args.split())

if not build_only:
    subprocess.run(target_filepath)
