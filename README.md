# todo.py
Simple script to create and manage tasks and todo lists in the command line

## Usage

`todo.py [options] [FILE]`  
Where the default value for FILE is _todo.txt_  

`todo.py -h` - show the help page with usage and arguments  
`todo.py -v` - show the version  
`todo.py -n NAME [FILE]` - create a file with title NAME  
`todo.py -a TASK [FILE]` - add TASK to the todo list FILE  
`todo.py -d TASK [FILE]` - delete TASK from the todo list in FILE  
`todo.py -x N [FILE]` - check task number N (if its checked, uncheck instead)  
`todo.py -e [FILE]` - edit plain text FILE with default editor  

OBS: type `todo.py` for quickly creating a todo list named _TO-DO LIST_ in the file todo.txt  

## Example

```
   $ todo.py -v
   todo.py 0.2 - cli to-do list manager

   $ todo.py -h
   usage: todo [-h] [-v] [-l] [-n NAME] [-a TASK] [-d TASK] [-x N] [-e] [FILE]

   Simple command line script to create and manage tasks and to-do lists.

   positional arguments:
     FILE                  to-do list file (default 'todo.txt')

   optional arguments:
     -h, --help            show this help message and exit
     -v, --version         show program's version number and exit
     -l, --list            list the tasks in the to-do list
     -n NAME, --new NAME   create new to-do list with title NAME
     -a TASK, --add TASK   add TASK to the to-do list
     -d TASK, --delete TASK
                           delete TASK from the to-do list
     -x N, --check N       chek/uncheck task number N
     -e, --edit            edit to-do list with default editor

   $ todo.py
   ==========
   TO-DO LIST
   ==========

   $ todo.py -a "Watch a movie"
   ==========
   TO-DO LIST
   ========== 
    1. [ ] Watch a movie

   $ todo.py -a "Buy some food"
   ==========
   TO-DO LIST
   ==========
    1. [ ] Watch a movie
    2. [ ] Buy some food

   $ todo.py -x 2
   ==========
   TO-DO LIST
   ==========
    1. [ ] Watch a movie
    2. [X] Buy some food

   $ todo.py -d 1
   ==========
   TO-DO LIST
   ==========
    1. [X] Buy some food

   $ todo.py -x 1
   ==========
   TO-DO LIST
   ==========
    1. [ ] Buy some food

```
