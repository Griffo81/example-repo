''' Task 11 - String Handling '''

# Ask the user to input a string.
user_input = input("Please enter a string: ")

# Convert alternating characters to uppercase and lowercase.
RESULT = ""
for i, char in enumerate(user_input):
    if i % 2 == 0:
        RESULT += char.upper()  # Convert to uppercase for even indices
    else:
        RESULT += char.lower()  # Convert to lowercase for odd indices

# Print the resulting string.
print("Resulting string:", RESULT)

# Using the same string, make alternating words uppercase and lowercase.
words = user_input.split()
result_words = []
for i, word in enumerate(words):
    if i % 2 == 0:
        # Convert to uppercase for even indices
        result_words.append(word.upper())
    else:
        # Convert to lowercase for odd indices
        result_words.append(word.lower())

# Join the words back into a single string.
RESULT_WORDS_STRING = ' '.join(result_words)

# Print the resulting words string.
print("Resulting words string:", RESULT_WORDS_STRING)
