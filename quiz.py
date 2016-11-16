# Our quiz!

score = 0
name = ""

def quiz():
    global name

    name = input("Name: ")

    question1()
    question2()
    question3()

    replay = input("Try again (Y/N): ")
    if replay.lower() == "y":
        quiz()
    

  
def question1():
    global score
    global name

    print("So", name, "which football player won the Ballon d'Or last year?")
    answer = input("Answer: ")

    if answer.lower() in "cristiano ronaldo":
        print("Correct!")
        score = score + 1

    else:
        print("Wrong!")

    

def question2():
    global score
    global name

    print("Now", name, "which team won the Premier League last season?")
    answer = input("Answer: ")

    if answer.lower() in "leicester":
        print("Correct!")
        score = score + 1

    else:
        print("Wrong!")

   

def question3():
    global score
    global name

    print("Finally, name one of the three teams who were relegated last season", name + ":")
    answer = input("Answer: ")

    if answer.lower() in "astonvillanewcastlenorwich":
        print("Correct!")
        score = score + 1

    else:
        print("Wrong!")

    if score == 3:
        print("Congratulations! You are a football expert!")

    elif score == 2:
        print("Good job! You know your stuff!")

    elif score == 1:
        print("Not great! You should watch more!")

    else:
        print("I think you are on the wrong quiz!")



    

  





# Leave this at the bottom - it makes quiz run automatically when you
# run your code.
if __name__ == "__main__":
    quiz()
