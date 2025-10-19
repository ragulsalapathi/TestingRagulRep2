import matplotlib.pyplot as plt
# class Rectangle(object):
    
#     # Constructor
#     def __init__(self, width=2, height=3, color='r'):
#         self.height = height 
#         self.width = width
#         self.color = color
    
#     # Method
#     def drawRectangle(self):
#         plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
#         plt.axis('scaled')
#         plt.show()
    
# rect = Rectangle(width=2,height=3,color='green')
# rect.drawRectangle()
        
# class circle(object):
#     def __init__(self,radius='5',color='red'):
#         self.radius=radius
#         self.color=color
    
#     def drawcircle(self):
#         plt.gca().add_patch(plt.Circle((0,0),self.radius,fc=self.color))
#         plt.axis('scaled')
#         plt.show()

# circ= circle(radius=5,color='yellow')
# circ.drawcircle()

# Text Analysis
givenstring="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."
class TextAnalyzer(object):
    def __init__(self,text):
        formattedtext = text.replace('.','').replace('!','').replace('?','').replace(',','')
        formattedtext = formattedtext.lower()
        
        self.fmttext = formattedtext

    def freqAll(self):
        freqDict = {}
        wordlist = self.fmttext.split(' ')
        print(wordlist)
        for word in set(wordlist):
            freqDict[word] = wordlist.count(word)

        return freqDict
    
    def findFreq(self,search):
        freqDict = self.freqAll()


        if search in freqDict:
            return freqDict[search]
        else:
            return 0


analyzed = TextAnalyzer(givenstring)
print(analyzed.freqAll())
print("Frequency of 'diam':", analyzed.findFreq("diam"))

# list = list(range(0,5,2))
# print(list) 

# signal_state = "Red"
# if signal_state == "Green":
#     print("Walk")
# else:
#     print("Wait")
# print("Look both ways")


total_budget = 1000 
def calculate_remaining(spent): 
    #total_budget = 500 
    return total_budget - spent 
print(calculate_remaining(200))

current_temp = 18
current_temp = current_temp > 25
print(current_temp)