import webbrowser
import sys
from re import search
# https://www.csestack.org/code-python-to-open-url-in-browser/
source_file = r'C:\Users\gjone\Jonesys_Learning_Machines\_sklearn_pages.txt'
cmd_ops = ['options', 'opt']
lines  = list()

# get the options from the option file
with open(source_file, 'r') as file_object:
    lines = file_object.readlines()

def open_site(urlStr, browser='chrome'):
    webbrowser.open_new_tab(urlStr)

def show_options():
    for line in lines:
        print(line)
    return

if len(sys.argv) < 2  or sys.argv[1] in cmd_ops:
    print("usage: 'subject'")
    print('\t\tCurrent Options:')
    show_options()
else:
    for line in lines:
        if search(sys.argv[1], line):
            # get the url from the line:
            urlStr = line.strip().strip('\n').split(' ')[1]
            print(urlStr)
            open_site(urlStr, )
        quit(0)
    print('option: {} not found'.format(sys.argv[1]))
    show_options()
    quit(-1)


