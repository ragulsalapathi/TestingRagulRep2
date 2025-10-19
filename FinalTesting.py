source="FinalTesting.txt"

# # Writing a line in a file
with open(source,"w") as writefile:
   writefile.write("This is the Firstline")

# # Read a file
with open(source,"r") as readfile:
   print("Before Multiple Line :",readfile.read())

# # Writing  Multiple line in a file
with open(source,"w") as multiplefile:
   multiplefile.write("This is Line No 1\n")
   multiplefile.write("This is Line No 2\n")

# # Read a file
with open(source,"r") as readfile:
   print("After Multiple Line : ",readfile.read())

#With List
Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
with open(source,"w") as file:
   for l in Lines:
      print(l)
      file.write(l)

#  w+ : Writing and reading. Truncates the file  

with open(source,"w+") as fileappend:
    fileappend.write("This is example for mine1")
    print(fileappend.read())

# r+ : Reading and writing. Cannot truncate the file. 

with open(source,"r+") as fileappend:
    fileappend.write("This is example for mine3")
    print(fileappend.read())

# a+ : Appending and Reading. Creates a new file, if none exists.
with open('Example2.txt', 'a+') as testwritefile:
    testwritefile.write("This is line E\n")
    print(testwritefile.read())