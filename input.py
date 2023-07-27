#the datatype of input in output is default string and have to explicity define the 
#data type
def know():
    print(myValue)
    print(type(myValue))
    print(str(myValue) + "ïs the data type of "+ str(type(myValue)))

myValue = input()
know()

myValue = int(input())
know()

myValue = float(input())
know()

myValue = complex(input())
know()

myValue = bool(input())
know()

myValue = str(input())
know()

