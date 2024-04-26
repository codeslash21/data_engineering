
# Intro to Shell
`Shell` is command line interface for running programs on your computer. Bash Shell is one of the most popular UNIX-style shell. For windows we can use `Git Bash`. Terminal is just the interface to the Shell and to other command line program running inside it. 

![image](https://github.com/codeslash21/data_engineering/assets/32652085/0b8d7d9b-9ee9-4617-81dd-e275bb007ba1)

This is `shell prompt`, it displays some information about the computer you logged into. If you type something in at the Shell prompt and hit enter, the shell will try to run whatever you typed as a command.  

## Shell Command
- `echo` to print some message. `echo hello` will print `hello`. We can also put the message within the `''`
- `ls` list the files in the current working directory. With `ls` we can give folder name/path also. We can also use flag with `ls`. If we want to list all the files with particular file extension, then we can use `*` for that. For example `ls -l *.pdf`, here `-l` is a flag to give more details about each file apart from just the file name.
- `cd` to change the directory
- `pwd` print current working directory
  - `.` means current working directory
  - `..` means parent directory of current working directory
  - `~` means my home directory
- `mkdir` to create a new directory
- `mv` to move file from one directory to another directory.
- `curl` to download a file/page from web.
  - `curl -L 'http://google.com'` we can see the actual source code of the site in our shell.
  - `curl -o google.html -L 'http://google.com'` to get the source code of the site to this file `google.html` instead of in the terminal.
- `cat` to show the entire content of the file in the terminal. For example, `cat demo.txt`
- `less` will show one screefull file content at the same time.
  - you have to press space to scroll down or we can use arrow keys
  - We can use `B` to go back or scroll up.
  - `/` to search particular word in the content showed in the terminal.
  - `Q` to quit
- `rm` to remove file. `rm` will not move the folder to recycle bin, it will delete the permanently. If you want to get confirmation message before deletion then use `i` flag, like `rm -i demo.txt`
- `rmdir` to remove folder
- `grep` will print all the line which match a specified pattern. `grep word demo.txt` grep will read the file line by line and print all the line which contain `word`
  - If there are more lines that we cant see at once then we can pass the output of `grep` command to `less` command using pipe `|` character, so the output of the `grep` will not go to the terminal directly, instead it will go the `less` command which displays those lines of the terminal one page at a time.
  - Similarly we can pass the output of `curl` command to `grep` command using `|` character. `curl -L http://tinyurl.com | grep fish`
  - We can count the number of words those matched with the specified word by using `c` flag. `grep -c word demo.txt`
- `wc` to count word. We can pass the output of `grep` to `wc` also. `grep word demo.txt | wc -l`
- We can create variable like `num='one'` and to print the value of variable `echo $num`. There are two types of variables in the shell.
  - One of them is `shell variable`. `LINES` and `COLUMNS` are these kind of variable. `echo $LINES * $COLUMNS` These type of variable are just internal to the shell program itself.
  - Other type is called `environment variable` Environment variables are shared with programs that you run from within the shell. One of this type is `PATH` variable, that tells your system where your program files are. So, when you type a command such as `ls` it can find the program to run it. Directories in the path variables are separated by the `:`. Shell search them starting with the first one and then proceeding to right until it finds the command that you entered. Thats how shell able to find the `ls` command when we run that. To add new path from terminal we do `PATH=$PATH:/then/new/dir`, but if we do llike this at the shell prompt that change will only last until you close the shell.
- If we want to make environment variable created at shell prompt permanent we have to add that to `.bash_profile`, which is shell configuration file. Whenever you open a shell terminal it will run all the commands in the `.bash_profile` file, for MAC and Windows, but for Linux system `.bash_profile` will only run for some shell session like log-in session, non log-in shell session run a file called `.bashrc`. So, if we want to use same configuration for different operating system then one popular solution is to put a statement into the `.bash_profile` file to tell if `.bashrc` file exists run that file

![image](https://github.com/codeslash21/data_engineering/assets/32652085/1a33ebab-bcac-40d9-9d0f-0aab2916a32c)

- We can change the shell prompt like `export PS1='Soumya@'`. If we want to change to something different then `PS1='Soumya$ '`. But, this change will only last until you close the window. We can use `bashrcgenerator` to create colourful customized shell prompt. Space around `=` is not allowed.
- Using `alias` we can shorten our command like `alias ll='ls -la'`. If you want to see all the alias command just type `alias` command to the prompt. To you want your alias to be there every time you start, then put that alias into the `.bash_profile` file. 
