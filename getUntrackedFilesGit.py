#!/bin/env python

import git
import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', default=':', type=str, dest='slice')
parser.add_argument('--ignore', default='', type=str, dest='file_ignored')
args = parser.parse_args()

repo = git.Repo(os.getcwd())

changedFiles = [ item.a_path for item in repo.index.diff(None) ] + repo.untracked_files

def is_int(val):
    try:
        _ = int(val)
        return _ >= 0
    except:
        return False

if not is_int(args.slice):
    s = slice(*[{True: lambda n: None, False: int}[x == ''](x) for x in (args.slice.split(':') + ['', '', ''])[:3]])
else:
    s = slice(int(args.slice), int(args.slice) + 1, None)

files = changedFiles[s]

GLOBAL_IGNORES = {
    'VIMIGNORE': ['.gitignore']
}
file_ignored = args.file_ignored.split(' ')
for key, values in GLOBAL_IGNORES.items():
    if key in file_ignored:
        file_ignored.append(*values)

files = [f for f in files if f not in file_ignored]

if len(files) > 0:
    print(' '.join(files))
else:
    sys.exit(1)
