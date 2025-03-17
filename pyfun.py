# Create an empty list to store the strings
strings = []

# Ask the user to input five strings
for i in range(1, 6):
    user_input = input(f"Enter string {i}: ")
    strings.append(user_input)

# Calculate and display the length of each string
for i, string in enumerate(strings, 1):
    print(f"The length of string {i} ('{string}') is: {len(string.replace(" ",""))}")
