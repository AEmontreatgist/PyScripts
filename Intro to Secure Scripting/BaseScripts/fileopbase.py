# Open the file in read mode
file = open("example.txt", "r")

# Read the contents of the file and print them to the console
contents = file.read()
print("Contents of the file:")
print(contents)

# Close the file
file.close()

# Open the file in write mode
file = open("example.txt", "w")

# Write a new line to the file
file.write("\nThis is a new line added to the file.")

# Close the file
file.close()

# Open the file in append mode (adds on to the file instead of writting over it)
file = open("example.txt", "a")

# Write a new line to the file
file.write("\nThis is a new line added to the end of the file.")

# Close the file
file.close()

