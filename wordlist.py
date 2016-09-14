import string

string1 = string.ascii_letters+string.digits
string2 = string.ascii_uppercase
f1=open('./wordlist.txt','w+')

for i in string1:
    for j in string1:
        for k in string1:
            for a in string1:
                for b in string1:
                    for c in string1:
                        for d in string1:
                            for e in string1:
                                f1.write("%s%s%s%s%s%s%s%s" % (i,j,k,a,b,c,d,e))
