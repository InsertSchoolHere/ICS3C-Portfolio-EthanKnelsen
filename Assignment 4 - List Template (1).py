"""
Assignment 4 - List
Name:Ethan Knelsen
Date:1/13/2026
________________________________________________________________________________________________
PART A
________________________________________________________________________________________________
Prompt the user to enter positive numbers repeatedly which represent test scores. 
Continue accepting float inputs until the user enters -1.  
Value -1 will act as a sentinel to stop the input process. 
Store all positive numbers entered by the user in a list.  
After input ends, loop through the list and print each number on a new line. - This needs to be completed for a Level 4  
Bonus: Calculate the average of the test scores – One bonus mark
"""

def get_test_scores():
    scores = []
    while True:
        try:
            score = float(input("Enter a test score (-1 to stop): "))
            if score == -1:
                break
            elif 0 <= score <= 100:
                scores.append(score)
            else:
                print("Please enter a score between 0 and 100, or -1 to stop.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    return scores

def main():
    scores = get_test_scores()
    print("\nTest Scores:")
    for score in scores:
        print(score)
    if scores:
        average = sum(scores) / len(scores)
        print(f"\nAverage Test Score: {average:.2f}")

if __name__ == "__main__":
    main()





"""
________________________________________________________________________________________________
PART B
________________________________________________________________________________________________
Prompt the user to enter words repeatedly. 
Continue accepting input until the user enters "quit".  
The word "quit" will act as a stop for the input process. 
Store all words entered by the user in a list. 
After input ends, display all the words in the list. 
Ask the user if they want to check whether a specific word exists in the list: - This needs to be completed for a level 4 Level 4 
If yes, prompt them to enter a word. 
Display whether the word is found in the list.  
You may assume that the names are all lowercase including the word quit – You will lose marks for using upper(), lower() or find() 
"""

def get_user_input():
    words = []
    while True:
        word = input("Enter a word: ")
        if word.lower() == 'quit':
            break
        if not word.isalpha():
            print("Invalid input. Please enter a word without numbers.")
            continue
        words.append(word.lower())
    return words

def check_word(words):
    target_word = input("Enter a word to check: ").lower()
    if target_word in words:
        print(f"'{target_word}' is found in the list.")
    else:
        print(f"'{target_word}' is not found in the list.")

def main():
    words = get_user_input()
    print("\nYou entered the following words:")
    for word in words:
        print(word)
    check_again = input("\nDo you want to check a word? (yes/no): ").lower()
    if check_again == 'yes':
        check_word(words)

if __name__ == "__main__":
    main()

