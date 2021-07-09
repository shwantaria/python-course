a=[5,10,15,20,25]
x=[a[0],a[-1]]
print(x)

y=[]
y.append(a[0])
y.append(a[-1])
print(y)


num=5
mod=num%2
if mod>0:
    print("you picked an odd number." )   
else:    
    print("you picked an even number.")  


b=("1","2","3","4","5","6","7","8","9","10")
print(b[0:-5])
print(b[5:10])


username=input("anisa@gmail.com")
input.split(username)
print(input.split)


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











