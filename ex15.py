from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Write the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

# extra-credit 8
txt.close()
txt_again.close()
