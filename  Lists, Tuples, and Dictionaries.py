def know():
    print("Working on the" + str(type(t)) + "data type")
    print("Create a"+ str(type(t)) )
    print(t)
    print(type(t))
#Accessing  by position    
    print(t[0])
    print(t[2])
    print(t[1])
    print(t,"\n")


#Defining a list
t = myFruitList = ["apple", "banana", "cherry"]
know()

#Defining a the tuple data type
t = myFinalAnswerTuple = ("apple", "banana", "pineapple")
know()

#Introducing the dictionary data type
t = myFavoriteFruitDictionary = {
  "Akua"  : "apple",
  "Saanvi" : "banana", 
  "Paulo" : "pineapple"
}
know()
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])
