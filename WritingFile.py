# with open('Testing.txt', 'r+') as file1:    
#     file1.write("This is first line A\n")
#     file1.write("This is second B\n")

# with open('Testing.txt', 'r+') as Bfile:   
#    print("Before Change : ",Bfile.read())

# lines=["Hi Buddy","Today is one of the worst day","Its Ok tomorrow will be yours..","Beleive in yourself da"]
# with open("Testing.txt","w") as file1:
#    for i in lines:
#       file1.write(i+"\n")

# with open('Testing.txt', 'r+') as Afile:   
#    print("After Change : ",Afile.read())

# newdata="This is a new line...which im importing or appending now...."
# with open("Testing.txt","a") as Afile:
#    Afile.write(newdata)

# with open('Testing.txt', 'r+') as Afile:   
#    print("After second Change : ",Afile.read())
with open("TestingNew.txt","r") as original:
    print("Before the Change: ",original.read())

with open("Testing.txt","r") as readfile:
    with open("TestingNew.txt","w") as writefile:
        for i in readfile:
            writefile.write(i)
            
with open("TestingNew.txt","r") as original:
    print("After change :",original.read())