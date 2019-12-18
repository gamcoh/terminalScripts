# terminalScripts
Scripts that automates certain tasks in the terminal


## getUntrackedFiles
### Usage
Create a symbolic link in `/usr/local/bin/` or any other directory that is in your `$PATH` variable
```
ln -s ~/terminalScripts/getUntrackedFilesGit.py /usr/local/bin/ugf
```

Get all unstaged files in a git repository
```
ugf
```

Get specific files
```
ugf 0
ugf N
ugf 3:6
ugf -1
ugf ::-1
```

Delete a specific file
```
rm $(ugf 4)
```
