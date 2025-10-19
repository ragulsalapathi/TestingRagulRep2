# d={"thirleer":123,"black beard":456}
# print(d)
# print(d["thirleer"])
# d[(0,1)]
# Create a sample dictionary

Moviesdict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973"}
# print(Moviesdict)
# print(Moviesdict.keys())
# print(Moviesdict.values())
Moviesdict["Graduation"]="2020"
print(Moviesdict)
del(Moviesdict["Thriller"])
print(Moviesdict)
print('The Dark Sideof the Moon' in Moviesdict)