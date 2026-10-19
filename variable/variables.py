# Create variables for your name, age, height, and whether youre a student. Print each with its type using type().
name="lena"
age=21.0
height="170cm"

print(type(name))
print(type(age))
print(type(height))

#Take two numbers as input, then print their sum, difference, product, division, floor division, and remainder.
a=int(input())
b=int(input())
sum= a+b
diff=a-b
product=a * b
division=a%b
floor=a//b
remainder=a/b
print("diff of 2 numbers:",diff)
print("product of 2 numbers:",product)
print("division of 2 numbers:",division)
print("floor division of 2 numbers:",floor)
print("remainder of 2 numbers:",remainder)

#Convert the string "123" to an integer and a float, then convert 45.9 to an integer. What happens to the decimal
number="123"
print(int(number))
print(float(number))
num2=45.9
print(int(num2))

#Given text = "Python for AI", print it in uppercase, lowercase, reversed, and replace “AI” with “Data”
text="Python for AI"
print("Uppercase",text.upper())
print("lowercase",text.lower())
print("reversed",text[::-1])
print("replaced",text.replace("AI","DATA"))

#Remove duplicates from [1, 2, 2, 3, 4, 4, 5] using a set, then find the common items between two sets.
numbers=[1,2,2,3,4,4,5]
number2=[3,4,5,2,6,7]
duplicates=set(numbers)
intersection=duplicates.intersection(numbers)
print(duplicates)
print(intersection)