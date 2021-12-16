print("Welcome to Mischa's QUIZ-SHOW!")
q1=input("Question 1: Who was the german ruler in the 1st World war?")
count=0
if q1=="Wilhelm II":
    print("Correct! Good job!")
    count+=1
else:
    print("That is in correct! Out you go!")
q2=input("How much is 12*5:10?")
if q2=="6":
    print("Very good! Correct answer!")
    count+=1
else:
    print("Incorrect! You're out!")
q3=input("What is the capital of Australia?")
if q3=="Canberra":
    print("Good job, you are on the way to victory!")
    count+=1
else:
    print("Incorrect!")
q4=input("Who was Johann Wolfgang von Goethe?")
if q4=="a poet":
    print("You are so close to victory, hang in there! cOrrect answer")
    count+=1
else:
    print("No he wasn't! You're out!")
q5=input("Last question! Who directed and is the official maker of Star Wars?")
if q5=="George Lucas":
    print("YES!!! You've done it! You have answered all of my questions correctly so you're the winner! Great job!")
    count+=1
else:
    print("No, I'm sorry the answer was George Lucas. Still good job answering 4 question. Good bye!")

print(count)