# # def add1(a):
# #     """add 1 to a"""
# #     b=a+1
# #     return b

# # s=add1(8)
# # print(s)
# def calculateadd(a,b):
#     total=a+b
#     return total

# result = calculateadd(7,9)
# print(result)

# stringlength = len("Hello,World!")
# intlength = len([1,2,3,4,5,6])
# total = sum([150,120,160,180,1000])
# maxvalue = max([150,120,160,180,1000])
# minvalue = min([150,120,160,180,1000])
# print(maxvalue,minvalue)
# print(total)
# print(stringlength,' ',intlength)
# def printnum(limit):
#     for i in range(1,limit+1):
#         print(i)

# print(printnum(6))

def calculater(a,b,method):
    if method == '+':
        total = a+b
    elif method == '-':
         if a > b:
             total = a-b
         else:
            total = b-a
    elif method =='*':
        total = a*b
    elif method == '/':
        if a > b:
          total = a/b
        else:
          total = b/a
    return total

calculate = calculater(1,2,'/')
print(calculate)