# Write a program to take name and age as input and
#       in output it should generate that in which year it will be 100

name = input("Enter Name:")
age  = int(input("Enter Current Age:"))

current_year = 2024
age_100_calculation = ((100 - (age)) + current_year)
# Integer Can not be concatenated in the string , Type cast is required
print(name + "will be turned into 100 years in " + str(age_100_calculation) + "years")
print("{} will be in 100 years old in {}".format(name, age_100_calculation))
#print(age_100_calculation)