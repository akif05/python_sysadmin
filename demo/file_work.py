import sys, os

def process_file(f):
    for line in f:
        # do something with the line
        # if don't want to do anything use pass
        # end='' supresses new line at the end withou it we see two new lins
        print (line, end='')
        #pass

# Start here
if (len(sys.argv)) == 1:
    process_file(sys.stdin)
else:
    for path in sys.argv[1:]:
        try:
            file = open(path, "r")
        ## Nex will catch all excatpion
        except Exception as e:
            print ("%s" % e, file=sys.stderr)
            continue
        process_file(file)
        close(file)
