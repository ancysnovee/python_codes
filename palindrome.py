#palindrome

def palindrome(word):
    cleaned_word = ''.join(char for char in word if char.isalnum())
    if cleaned_word==cleaned_word[::-1]:
        print(f"the word {word} is palindrome")
    else:
        print("it is not palindrome")
    
word=input("enter the word").lower()
palindrome(word)

