# break and continue in python -- 


# break statement -- 
# The break statement enables a program to skip over a part of the code. A break statement terminates the very loop it lies within.

for i in range(1,101,1):
    print(i ,end=" ")
    if(i==50):
        break
    else:
        print("Mississippi")
print("Thank you")

# Continue Statement -- 
# The continue statement skips the rest of the loop statements and causes the next iteration to occur.

for i in [2,3,4,6,8,0]:
    if (i%2!=0):
        continue
    print(i)