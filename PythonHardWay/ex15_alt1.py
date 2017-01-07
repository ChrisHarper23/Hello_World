print "Type the filename again:"
filename = raw_input ('> ')

txt = open(filename)

print txt.read()
