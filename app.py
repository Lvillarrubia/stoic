import csv
from datetime import date, datetime, timedelta

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


def load_rows(file_name):
    with open(file_name, "r", newline="") as file:
        reader = csv.reader(file)
        return list(reader)


def entry_already_exists(rows, target_date):
    for row in rows[1:]:
        if row[0] == target_date:
            return True
    return False


def update_entry(rows, target_date, new_row):
    updated_rows = [rows[0]]

    for row in rows[1:]:
        if row[0] == target_date:
            updated_rows.append(new_row)
        else:
            updated_rows.append(row)

    return updated_rows


def save_all_rows(file_name, rows):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)


def get_week_range(today):
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    return start_of_week, end_of_week


def get_weekly_rows(rows, start_of_week, end_of_week):
    weekly_rows = []

    for row in rows[1:]:
        row_date = datetime.strptime(row[0], "%Y-%m-%d").date()
        if start_of_week <= row_date <= end_of_week:
            weekly_rows.append(row)

    return weekly_rows


def get_quality_label(score):
    if score <= 2:
        return "Poor"
    elif score <= 4:
        return "Below Average"
    elif score <= 6:
        return "Average"
    elif score <= 8:
        return "Good"
    else:
        return "Excellent"


def show_weekly_summary(rows):
    today = date.today()
    start_of_week, end_of_week = get_week_range(today)
    weekly_rows = get_weekly_rows(rows, start_of_week, end_of_week)

    total_days_logged = len(weekly_rows)
    successful_days = sum(1 for row in weekly_rows if row[-1] == "yes")

    consistency_rate = (total_days_logged / 7) * 100
    success_rate = (successful_days / 7) * 100

    print("\nWeekly Summary")
    print("-" * 30)
    print(f"Week: {start_of_week} to {end_of_week}")
    print(f"Days logged: {total_days_logged}/7")
    print(f"Successful days: {successful_days}/7")
    print(f"Consistency rate: {consistency_rate:.1f}%")
    print(f"Success rate: {success_rate:.1f}%")

    if today.weekday() == 6:
        practice_counts = [0] * len(stoic_questions)

        for row in weekly_rows:
            for i in range(len(stoic_questions)):
                if row[i + 1] == "yes":
                    practice_counts[i] += 1

        print("\nPractice Breakdown")
        print("-" * 50)

        for question, count in zip(stoic_questions, practice_counts):
            quality_score = round((count / 7) * 10)
            quality_label = get_quality_label(quality_score)
            print(f"{question}: {quality_score} ({quality_label})")


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
entry_date = date.today().isoformat()

print("\nDaily Entry Summary")
print("-" * 30)

for index, (question, answer) in enumerate(zip(stoic_questions, answers), start=1):
    print(f"{index}. {question}: {answer}")

print("\nDaily Score")
print("-" * 30)
print(f"Total yes answers: {total_score}/10")
print(f"Successful day: {successful_day}")

new_row = [entry_date] + answers + [total_score, successful_day]
rows = load_rows("executed_log.csv")

if entry_already_exists(rows, entry_date):
    while True:
        choice = input(
            "\nAn entry for today already exists. Type update to replace it or cancel to stop: "
        ).strip().lower()

        if choice == "update":
            updated_rows = update_entry(rows, entry_date, new_row)
            save_all_rows("executed_log.csv", updated_rows)
            print("\nToday's entry was updated.")
            rows = updated_rows
            break
        elif choice == "cancel":
            print("\nNo changes were made.")
            break
        else:
            print("Invalid input. Type update or cancel.")
else:
    rows.append(new_row)
    save_all_rows("executed_log.csv", rows)
    print("\nEntry saved to executed_log.csv")

show_weekly_summary(rows)
