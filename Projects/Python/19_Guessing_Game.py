# program using statements and loops
# 24/01/23
secret_word = "Chris"
guess = input("Welcome to 'Guess That Word!' What is your first guess? ")
i = 4
if guess == secret_word:
    print("Congratulations! First try!")
while guess != "Chris" and i > 0:
    print("Incorrect! You have " + str(i) + " guesses left.")
    guess = input("What is your next guess? ")
    i -= 1
    if guess == secret_word:
        print("Congratulations! You guessed correctly.")
        i = 0
    elif i == 0:
        print(
            "Hard luck! You couldn't guess the answer. The secret word was " + secret_word + ". Better luck next time.")
