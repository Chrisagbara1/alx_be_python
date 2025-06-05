# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process task using match-case
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unknown priority level. Please verify your input."

# Add time-sensitivity logic
if time_bound == "yes" and "priority" in message:
    message += " that requires immediate attention today!"
elif time_bound == "no" and "Note:" in message:
    message += " Consider completing it when you have free time."
elif time_bound == "no" and "Reminder:" in message:
    message += " but it is not time-sensitive."

# Output the final message
print("\n" + message)