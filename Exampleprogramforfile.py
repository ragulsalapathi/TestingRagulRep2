from random import randint as rnd
currmem="members.txt"
oldmem="inactive.txt"
fee=('Yes','No')

def genFiles(current,old):
    with open(current,"w+") as writefile:
        writefile.write("Membership No  Date Joined  Active\n")
        data="{:^13} {:<11} {:<6}\n" # For the width according to the headline.

        for rowno in range(10):
            date= str(rnd(2025,2025))+'_'+str(rnd(1,10))+'_'+str(rnd(1,31))
            writefile.write(data.format(rnd(10000,20000),date,fee[rnd(0,1)]))

    with open(old,"w+") as writeold:
        writeold.write("Membership No  Date Joined  Active\n")
        data="{:^13} {:<11} {:<6}\n"

        for rowno in range(3):
            date=str(rnd(2025,2025))+'_'+str(rnd(1,10))+'_'+str(rnd(1,31))
            writeold.write(data.format(rnd(10000,20000),date,fee[1]))

genFiles(currmem,oldmem)