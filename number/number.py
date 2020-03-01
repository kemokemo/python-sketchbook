import random
answer = random.randint(1,100)

while True:
    user_guess = int(input("What is your guess? "))

    if user_guess == answer:
        print(f"Right! The answer is {user_guess}")
        break

    elif user_guess < answer:
        print(f"Your guess is {user_guess}. It's too low.")

    elif user_guess > answer:
        print(f"Your guess is {user_guess}. It's too high.")
