# with open('Example2.txt', 'a+') as testwritefile:
#     print("Initial Location: {}".format(testwritefile.tell()))
    
#     data = testwritefile.read()
#     if (not data):  #check if whether after the cursor something is available
#             print('There is nothing to Read after the cursor') 
#     else: 
#             print(testwritefile.read())
            
#     testwritefile.seek(2,0) # used move cursor based on the position
    
#     print("\nNew Location : {}".format(testwritefile.tell()))
#     data = testwritefile.read()
#     if (not data): 
#             print('Read nothing') 
#     else: 
#             print(data)
    
#     print("Location after read: {}".format(testwritefile.tell()) )


# Copy file to another
with open("Example2.txt","r") as sourcefile:
    with open("exam2.txt","a+") as destinationfile:
        for i in sourcefile:
            destinationfile.write(i)