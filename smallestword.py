# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")
#Jai Mata Di
string=input("Please input your string")
words=string.split(' ')
print(words[0])
smallestWord=len(words[0])
for i in range(1,len(words)):
    if (len(words[i])<smallestWord):
        smallestWord=len(words[i])
print(smallestWord)
