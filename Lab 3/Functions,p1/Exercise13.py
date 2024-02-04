import random
def play():
    name = input("Hello! What is your name?\n")
    print()
    counter = 1
    ans = int(input(("Well, {}, I am thinking of a number between 1 and 20.\nTake a guess.\n").format(name)))
    print()
    r = random.randint(1,20)
    while (ans != r):
        comp = "low" if ans < r else "high"
        ans = int(input("Your guess is too {}\n".format(comp)))
        print()
        counter+=1
    print("Good job, {}! You guessed my number in {} guesses!".format(name,counter))