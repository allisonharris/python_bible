# Ask user for name
name = raw_input('What is your name?: ') 

# Ask user for age
age = raw_input('What is your age?: ')

# Ask user for city
city = raw_input('What is your city?: ')

# Ask user for hobby
hobby = raw_input('What is your hobby?: ')

# Create output text
string = "Your name is {} and you are {} years old. You live in {} and you love {}"
output = string.format(name, age, city, hobby)

# Print output to screen
print(output)
