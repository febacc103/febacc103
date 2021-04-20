line="hai hello hai hello hai"
#hai :3
#hello:2
#split function:word by word data
print(line)
#hai
#hello
#hai
#hello
#hai
word=line.split(" ")
print(word)
dic={}
#key #value
#hai    1+1
#hai     1
for i in word:
    if(i not in dic):
        dic[i]=1
    else:
        dic[i]+=1
print(dic)

