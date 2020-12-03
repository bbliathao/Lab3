""" 
Create a list to store 5 number (float)
capture user's input 5 times for their grades
each time we capture a user's input, we append the number to the list
sort the list ascending, then splice the item starting at index 2
once we have three highest number in the list, we sum them up and divide by 3
output a message to the users
end
"""

"""
create list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list
sort the list, then splice out the two lowest number
print message to user
"""

grades = []

grade = input ("enter the 1st grade")
grades. append(float(grade))

grade = input ("enter the 1st grade")
grades. append(float(grade))

grade = input ("enter the 1st grade")
grades. append(float(grade))

grade = input ("enter the 1st grade")
grades. append(float(grade))

grade = input ("enter the 1st grade")
grades. append(float(grade))

grades.sort()

grades = grades[2:]
grades = sum(grades)

results = grades / 3

print("Average Grade{0:.2}".format(result))
print(grades, 'results', results)
2103
