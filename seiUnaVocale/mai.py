# Exercises/AreYouAVowel/mai.py
# This script verifies if a character entered by the user is a vowel.
character = input("Enter a character: ").lower()
vowels = "aeiou"

# Check if the character is a vowel
if character in vowels:
    print(f"The character '{character}' is a vowel")
else:
    print(f"The character '{character}' is not a vowel")