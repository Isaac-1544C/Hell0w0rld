questions = ("What's the teacher's name", 
             "What's the name of head of dp", 
             "What's the name of head of academic", 
             "What's the name of head of studentlife", 
             "What's the name of head of school")

options = (("A. David", "B. Ciara", "C. Kurt", "D. Mark"), 
           ("A. David", "B. Christopher", "C. Kurt", "D. Mark"), 
           ("A. David", "B. Ciara", "C. Kate", "D. Mark"), 
           ("A. David", "B. Ciara", "C. Kurt", "D. Simon Ma"), 
           ("A. Simon Head", "B. Ciara", "C. Kurt", "D. Mark"))

answers = ("A", "B", "C", "D", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    #make sure it's capital
    guesses.append(guess)
    #store the answers for each round
    if guess == answers[question_num]:
        score += 1
        print("correct")
    else:
        print("incorrect")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("results:")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
#percentage
print(f"Your score is: {score}%")