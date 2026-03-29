stoic_questions = [
    "Wake up early",
    "Train the body",
    "Practice self-command",
    "Journal and examine the mind",
    "Read and learn with purpose",
    "Walk and reflect",
    "Make time for deep work",
    "Visualize and prepare for difficulty",
    "Life is short; act with urgency",
    "Review the day at night"
]

answers = []

print("Stoic Discipline Tracker")
print("-" * 30)

for index, question in enumerate(stoic_questions, start=1):
    while True:
        user_answer = input(f"{index}. {question} (yes/no): ").strip().lower()

        if user_answer in ["yes", "no"]:
            answers.append(user_answer)
            break
        else:
            print("Invalid input. Type yes or no.")

total_score = answers.count("yes")
successful_day = "yes" if total_score >= 8 else "no"

print("\nDaily Entry Summary")
print("-" * 30)

for index, (question, answer) in enumerate(zip(stoic_questions, answers), start=1):
    print(f"{index}. {question}: {answer}")

print("\nDaily Score")
print("-" * 30)
print(f"Total yes answers: {total_score}/10")
print(f"Successful day: {successful_day}")
