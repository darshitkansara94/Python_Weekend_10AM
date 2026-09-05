# Casting :
#     Convert a data from one tyoe to another type is called as casting.
#     To convert a data there is some limitations that we need to consider like we can not convert
#     a string to an integer directly.

#     Syntax :
#         datatype(expression)
#     Example :

# string = "Darshit Kansara"
# print(type(string))

x = 10 # Integer
y = str(x) # Casting
print(type(x))
print(x)
print(type(y)) # Outout of casting

flt = float(x)
print(type(flt)) # Print type of float
print(flt) # Print value of float

a = 0
b = bool(a)
print(b)

# Return error because we can not convert string to int.
# string = "abc"
# z = int(string)
# print(type(z))