# Open a file for writing
file = open("death.txt", "w")

# Write some data to the file
file.write("I'm sorry, " +"you have not survived :(\n")
file.write("Thanks for playing my ame.")

# Close the file
file.close()

# Open the file for reading
file = open("death.txt", "r")

# Read the contents of the file
file_contents = file.read()

# Close the file
file.close()

# Print the contents of the file
print(file_contents)
