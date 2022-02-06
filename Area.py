#Radius of a circle
pi=3.144
r=int(input("The radius of the circle:"))
area=pi*r**2
print("The area of the circle with radius",r, "is:",area)

#to accept a filename from the user and print the extension of that.
filename=input("input the filename:")
f_extns=filename.split(".")
print("The extension of the file is:","f_extns")