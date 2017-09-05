#! /usr/bin/env python

import sys, argparse
import os


def todo_list(f):
    """ shows the content of the to-do file named f """
    os.system('cat %s' % f)


def edit(f):
    os.system('$EDITOR %s' % f)


def add(f, item):
    """appends item in the last line of the file f """
    with open(f, 'r') as outFile:
        num_lines = sum(1 for file in outFile)
    pk = str(num_lines - 2)
    with open(f, 'a') as outFile:
        outFile.write("%2s. [ ] %s\n" % (pk, item))
    todo_list(f)


def check(f, pk):
    """checks/unchecks to-do item of number pk """
    numline = pk + 2

    with open(f, 'r') as readFile:
        lines = readFile.readlines()
        l = list(lines[numline])

    if lines[numline][5].isspace():
        l[5] = 'X'
    else:
        l[5] = ' '

    lines[numline] = "".join(l)

    with open(f, 'w') as outFile:
        outFile.writelines([item for item in lines])

    todo_list(f)


def delete(f, pk):
    """ deletes item of number pk and renumber them """
    numline = pk + 2
    out = []
    i = 3

    with open(f, 'r') as readFile:
        lines = readFile.readlines()
    out_bkp = lines
    lines.pop(numline)

    [out.append(item) for item in lines[:3]]

    for e in lines[3:]:
        out.append("%2d. %s" % (i-2, e[4:]))
        i += 1

    with open(f, 'w') as outFile:
        outFile.writelines([item for item in out])

    todo_list(f)


def new(f, name):
    """ creates file with a header of string name """
    with open(f, 'w') as outFile:
        outFile.write("="*len(name) + "\n")
        outFile.write(name + "\n")
        outFile.write("="*len(name) + "\n")
    todo_list(f)


def main():
    """
    f           # file name
    args.delete # task to be deleted id
    args.check  # task to be checked id
    args.add    # task message
    args.new    # title of to-do list
    args.sub    # subtask number
    """

    parser = argparse.ArgumentParser(description="Simple command line script to\
                                    create and manage tasks and to-do lists.")

    parser.add_argument("file", metavar="FILE", action='store', default="todo.txt",
                        nargs='?', help="to-do list file (default 'todo.txt'")

    parser.add_argument("-v", "--version", action='version', 
                        version="%(prog)s.py 0.2  -  cli to-do list manager")
    parser.add_argument("-l", "--list", action='store_true',
                        help="list the tasks in the to-do list")

    parser.add_argument("-n", "--new", default="TO-DO LIST", metavar="NAME",action='store',
                        help="create new to-do list with title NAME")
    parser.add_argument("-a", "--add", metavar="TASK",action='store',
                        help="add TASK to the to-do list")
    parser.add_argument("-d", "--delete", metavar="TASK", type=int, action='store',
                        help="delete TASK from the to-do list")
    parser.add_argument("-x", "--check", metavar="N", type=int,action='store',
                        help="chek/uncheck task number N")
    parser.add_argument("-e", "--edit", action='store_true', 
                        help="edit to-do list with default editor")

    args = parser.parse_args()
    f = args.file

    if args.list:
        todo_list(f)
        sys.exit()

    elif args.check  and os.path.isfile(f):
        check(f, args.check)
        sys.exit()

    elif args.add and os.path.isfile(f):
        add(f, args.add)
        sys.exit()

    elif args.delete and os.path.isfile(f):
        delete(f, args.delete)
        sys.exit()

    elif args.edit:
        edit(f)
        sys.exit()

    elif args.new:
        assert not(os.path.isfile(f)), "%s already exists. Choose another file name." % f
        new(f, args.new)
        sys.exit()

    else:
        pass


if __name__ == "__main__":
    main()
