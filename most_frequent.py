x=input("Please enter a string:")
def most_frequent (str):
    mylist=[]
    j=0
    for i in str:
        mylist.append(i)
    myset=set(mylist)
    mydict={i:[] for i in myset}
    for i in myset:
        for k in mylist:
            if i==k:
                j+=1        
        mydict[i].append(j)
        j=0
    my_dict=sorted(mydict.items(),key=lambda x:x[1],reverse=True)
    print(my_dict)
most_frequent(x)
