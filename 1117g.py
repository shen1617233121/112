def functionName(level)
    if level < 1:
        raise Exception("Invalild level!",level)
    print "OK"
try:
    functionName(4)
except "Inalid level!":
     print "user definde exception"
else:
     print "else....."
finally:
    print "finally always run...."
