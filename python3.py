from sys import argv

script, filename = argv

txt = open(filename)

print "Here is your %s file right now." % filename
print txt.read()

print "Do you want to erase it???"
print """
Yes = Enter
No  = Ctrl + C 
"""
raw_input("?")

txt = open(filename, 'w')

print "Say bye bye to your file Haha" 
txt.truncate()

print "Type what you want to save to file" 

txt.write(raw_input("Line: "))

print "And we are done"
#print txt.read()

txt.close()
