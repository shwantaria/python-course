num=str(input("enter a phonenumber"))
if num[0:2]=="07":
    num="+254"+num[1:]
    print(num)
elif num[0:2]=="71":
    num="+254"+num[0:2]
    print(num)  
elif num[0:3]=="+254":
    print(num)  
elif num [0:2]=="01" :
    num="+254"+num [1:]
    print(num)
else:
    print("number is invalid")    











