# unconditional.py
# Block statement should have a full colon at the end of the line i.e :
# then following lines has to have an indent or space 
# once you are done with the block statement.
# remove the space in the next lines and continue with the code.
# If statements check if a certain condition is true and perform some task.
# indentation is the allignment.
# If Else statement is used to check for only 2 conditions
# what if there are more than 2 conditions? 
# we use elif else

var="john is here"
if var.count("john") >0:
    print("john is in the sentence")

elif var.count("mark") :
    print("mark is in the sentence")

elif var.count("amina")  :
    print("amina is here")   

else:
    print("no name in the sentence")  

  # when the first one is true it gets picked and everything else is ignored. 
  # 


x=2
y=10
if x!=y:
    print("your cond is TRUE")
    print("this runs because the cond is TRUE")
    print("this one too")

else:
    print("your condition is false")
    print("this is false")
    
if 67<80:
    # random computations
        y=67
        z=80
        total=z+y
        print(total)

else:
    print("the expression is false")
    print("change it to something true")
   

print("this will show either way")
z=78+20
print(z)
    
    
 # 1.Syntax error
# 2. logical error

# if one expression fail the whole condition fails.
# an and statement
# an or statement
print(34!=67 and 78>89 and 45==45)

print(34==67 or 45<9 or 9>8 or 8<9)


    





