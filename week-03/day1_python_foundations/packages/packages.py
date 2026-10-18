#Use the math module to calculate the square root, power, and area of a circle with a given radius.
import math
print(math.sqrt(2))
print(math.pow(2,4))
radius=10
area=2*3.14*radius
print(area)

#Use the random module to pick a random item from a list and generate 5 random numbers between 1 and 100.
import random
fruits=["mango","apple","banana"]
choice=random.choice(fruits)
print(choice)


#Use the datetime module to print today’s date and calculate how many days are left until the end of the year.
from datetime import date
today = date.today()
end_of_year = date(today.year, 12, 31)
days_left = (end_of_year - today).days
print(f"Today's date: {today}")
print(f"Days left until the end of the year: {days_left}")

#Create your own file helpers.py with two functions (e.g., add and greet), then import and use them in main.py

import helpers
sum=helpers.add(3,4)
greet=helpers.greet("lena")
print(sum)
print(greet)

#Install a package with pip (e.g., requests or numpy), import it, and use one feature from it.
import pandas as pd
data=[{
    "name":["lena","ringu"],
    "age":[21,20],
    "gender":["female","female"]
}]
result=pd.DataFrame(data)
print(result)

