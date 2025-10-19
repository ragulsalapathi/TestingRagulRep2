# Testlist=["Michael",1900,"jackie","Michael",1900,15.5]
# TestSet=set(Testlist)
# print("List : ",Testlist)
# print("Sets : ",TestSet)
# a={'Michael', 1900, 'jackie', 15.5}
# # a.add(1900)
# # a.remove('Michael')
# # print(a)
# # print("jackiee" in a)
# b={'Michael', 1900, 'jackie'}
# # print(a.union(b))
# # print(a.intersection(b))
# # print(a.issubset(b))
# # c=a.difference(b)
# c=set(a).issuperset(b)
# print(c)
# dict={"Name":"Ragul","Age":"25"}
# newdict=dict.copy()
# dict['Name']="sandhiya"
# del dict['Age']
# dict.update({"age":"23"})
# if "Name" in dict:
#     print("name is present")    
# print(dict)
# print(newdict)
# print(set(dict.keys()))
# print(list(dict.values()))
# print(list(dict.items()))
# print(set(dict.items()))
s={1,2}
s.add('janu')
# s.clear()
scopy=s.copy()
scopy.discard('janu')
print(s)
print(scopy)