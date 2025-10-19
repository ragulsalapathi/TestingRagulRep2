# # # result=10/0
# # # print(result)
# # # try:
# # #     result = 10/0
# # # except ZeroDivisionError:
# # #     print("Error : Cannot divide by Zero")
# # # print("outside of try and except block")
# # a=10
# # try:
# #     b=int(input("enter a number to divide a"))
# #     a=a/b
# #     print("Success : a=",a)
# # except:
# #     print("There is an error")

# a = 1

# try:
#     b = int(input("Please enter a number to divide a"))
#     a = a/b
#     print("Success a=",a)
# except ZeroDivisionError:
#     print("The number you provided cant divide 1 because it is 0")
# except ValueError:
#     print("You did not provide a number")
# except:
#     print("Something went wrong")
        

#Type your code here
def divsafe(numerator,denominator):
    try:
        result=numerator/denominator
        return(result)
    except ZeroDivisionError:
        print("The Number cannot be divide by zero")
        return None
    except ValueError:
        print("There must be a number")
        return None
    except:
        print("Something went wrong")
    # finally:
    #     print("Success with finally")
    
n=int(input("enter numerator : "))
d=int(input("enter denominator : "))
print(divsafe(n,d))