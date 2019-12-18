#!/home/gamzer/anaconda3/bin/python

import git
import os
import sys

repo = git.Repo(os.getcwd())

changedFiles = [ item.a_path for item in repo.index.diff(None) ] + repo.untracked_files

if len(sys.argv) < 2:
    sys.argv.append(':')

if sys.argv[1] not in ['0']:
    s = slice(*[{True: lambda n: None, False: int}[x == ''](x) for x in (sys.argv[1].split(':') + ['', '', ''])[:3]])
else:
    s = slice(int(sys.argv[1]), int(sys.argv[1]) + 1, None)

files = changedFiles[s]

print(' '.join(files))
