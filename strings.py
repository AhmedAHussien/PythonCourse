myString = "Hello World"


#indexing

#grab the first character
print(myString[0])

#grab the last character
print(myString[-1])

#grab the whole string
print(myString)



#Slicing

#start at index 2 till the end
print(myString[2:])

#more examples
print(myString[2:7:2])


#to change the string
newString = myString[:6] + 'M' + myString[7:]
print(newString)

#print formatting
print("myString = {}, newString = {}".format(myString, newString))

#or
print("newString = {1}, myString = {0}".format(myString, newString))

#or
print("myString = {m}, newString = {n}".format(m=myString, n=newString))