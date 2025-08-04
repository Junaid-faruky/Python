questions = {
    "Capital of France?": "Paris",
    "2+2": "4",
    "Python keyword to define a function?": "def"
}
score = 0
for q, ans in questions.items():
    response = input(q + " ")
    if response.strip().lower() == ans.lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong. Answer:", ans)
print(f"Final score: {score}/{len(questions)}")
