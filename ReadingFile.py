example1 = "Testing.txt"
file1 = open(example1, "r")
print(file1.name)   #for Name 
print(file1.mode)   #for Mode
print(file1.read()) #for Read full 
print(type(file1.read())) #for type
file1.close()

# A Better way to open a file 
with open("Testing.txt", "r") as file1:
        print("first line: " + file1.readline(20))
        print("Full Content :",file1.read(4))
        print("Full Content :",file1.read(6))
        print("Full Content :",file1.read(8))
        print("Full Content :",file1.read(12))

print(file1.closed) # To Verify whether the file is closed

# using loop
with open("Testing.txt","r") as files:
        i=0
        for line in files:
                print("Iteration :",str(i),line)
                i=i+1
            

# Read all lines and save as a list
with open("Testing.txt", "r") as file1:
    FileasList = file1.readlines()
    print(FileasList)
    print(FileasList[0]) #print the first line
    print(FileasList[1])
    