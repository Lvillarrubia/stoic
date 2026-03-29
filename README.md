# Stoic Discipline Tracker

A simple Python terminal app that tracks daily discipline through 10 Stoic-based practices.

## Purpose

This project was built to create a practical system for daily self-observation, consistency, and weekly review.

The app allows the user to:

- answer 10 daily Stoic practice questions with yes or no
- calculate a daily score out of 10
- define whether the day was successful
- save the entry automatically by date
- update the same day's entry if needed
- review weekly consistency and success
- show a practice breakdown on Sunday only

## Daily Rules

- Each `yes` = 1 point
- Each `no` = 0 points
- A successful day = 8 or more yes answers

## The 10 Daily Practices

1. Wake up early
2. Train the body
3. Practice self-command
4. Journal and examine the mind
5. Read and learn with purpose
6. Walk and reflect
7. Make time for deep work
8. Visualize and prepare for difficulty
9. Life is short; act with urgency
10. Review the day at night

## Weekly Logic

### Monday to Saturday
The app shows:

- Weekly Summary
- Days logged
- Successful days
- Consistency rate
- Success rate

### Sunday
The app shows:

- Weekly Summary
- Practice Breakdown

## File Structure

```text
stoic/
├── app.py
├── executed_log.csv
├── README.md
├── .gitignore
└── screenshots/