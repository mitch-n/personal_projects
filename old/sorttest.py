from operator import itemgetter

mydict={
    "two":{
        "size":2,
        "else":"else"
        },
    "one":{
        "size":1,
        "else":"else"
        }
    }

#mydict=sorted(mydict.items(), key=itemgetter(0,1))

for k,v in sorted(mydict.items(), key=lambda x: x[1]['size']):
    print(k)

    
