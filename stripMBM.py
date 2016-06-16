import re

string = str(raw_input('Enter a string: '))

def stripStr(string, c=' '):
    regex = '(^[' + c + ']*)(.*?)([' + c + ']*$)'
    strRegex = re.compile(regex)
    print strRegex.findall(string)[0][1]

stripStr(string)
