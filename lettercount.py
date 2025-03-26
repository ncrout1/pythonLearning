string= "narsing"
repeated=list(string)
unique=set(repeated)
dic={}
for i in unique:
    val=repeated.count(i)
    dic[i]=val
print(dic)
