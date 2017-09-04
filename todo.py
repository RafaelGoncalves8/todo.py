#! /usr/bin/env python

import sys, getopt
import os


def todo_list(f):
    """ shows the content of the todo file named f """
    os.system('cat %s' % f)


def add(f, item):
    """ appends item in the last line of the file f """
    with open(f, 'r') as outFile:
        num_lines = sum(1 for file in outFile)
    pk = str(num_lines - 2)
    with open(f, 'a') as outFile:
        outFile.write("%2s. [ ] %s\n" % (pk, item))
    todo_list(f)


def check(f, pk):
    """ checks/unchecks todo item of number pk """
    numline = int(pk) + 2

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
    numline = int(pk) + 2
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


def todo(argv):
    """ argv is the list of command line arguments """
    f = ""
    id_item = ""
    item=""
    title=""

    try:
        opts, args = getopt.getopt(argv,"hvf:ln:a:d:x:", ["help","version", "file=","new=","add=","delete","check="])
    except getopt.GetoptError:
        print('usage: todo.py -f <file> [command] <arg>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('Usage: todo.py -f file [options] arg\n')
            print('Options:')
            print('-n, --new    Creates the todo named <file> with the header <arg>')
            print('-l, --list   List items in todo <file>')
            print('-a, --add    Add the string arg in the <file>')
            print('-d, --delete Deletes todo item named <arg>')
            print('-x, --check  Check/uncheck the item number <arg> in file <file>')
            sys.exit()

        elif opt in ("-v", "--version"):
            print("todo.py version 0.1")
            sys.exit()

        elif opt in ("-f", "--file"):
            f = arg

        elif opt in ("-x", "--check") and os.path.isfile(f):
            id_item = arg
            check(f, id_item)
            sys.exit()

        elif opt in ("-a", "--add") and os.path.isfile(f):
            item = arg
            add(f, item)
            sys.exit()

        elif opt in ("-d", "--delete") and os.path.isfile(f):
            id_item = arg
            delete(f, id_item)
            sys.exit()

        elif opt in ("-l", "--list") and os.path.isfile(f):
            todo_list(f)
            sys.exit()

        elif opt in ("-n", "--new") and (not os.path.isfile(f)):
            title = arg
            new(f, title)
            sys.exit()

        else:
            pass

    print('usage: todo.py -f <file> [command] <arg>')


if __name__ == "__main__":
    todo(sys.argv[1:])
