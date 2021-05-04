def full(fn, ln):
    try:
        if(fn.isalpha() == True) and (ln.isalpha() == True):
            return fn + " " + ln
    except:
        return None

#fn = "Mingx"
#ln = "Li"
#name = full(fn, ln)
#print("name: ", name)