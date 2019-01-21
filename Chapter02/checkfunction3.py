globalval=6

def checkglobalvalue():
    return globalval

def localvariablevalue():
    globalval=8
    return globalval

print ("This is global value",checkglobalvalue())
print ("This is global value",globalval)
print ("This is local value",localvariablevalue())
print ("This is global value",globalval)
