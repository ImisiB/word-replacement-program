print()
print("      statement:  I am person1.")
print()
print("TO REPLACE A WORD TYPE 1")
print("TO CONTINUE PRESS 0")

replace = input()

def replace_word():
    if replace == "1":
        string = "I am person1."
        print()
        word_to_replace = input("Enter a word to replace: ")
        word_replacement = input("Enter the word replacement: ")
        print()
    if replace == "0":
        print()
        print(str("I am person1."))
    elif word_to_replace in string:    
        print(string.replace(word_to_replace,word_replacement))
    elif word_to_replace not in string:
        print("       unknown word", string, "does not include", word_to_replace)

replace_word()