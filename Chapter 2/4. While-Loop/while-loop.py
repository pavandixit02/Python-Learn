# While Loop :-
print("While Loop :- A while loop is a programming tool that repeats a block of code as long as a specific condition remains true.")

# 1. Basic Loop Structure
print("Example-1 :-")
count = 1

while count <= 5:
    print(count)
    count += 1

# 2. Server Retry System
print("\nExample-2 :-")
attempts = 1

while attempts <= 3:
    print(f"Checking server...Attempt {attempts}")
    attempts += 1


# Infinite Loop
print("\nInfinite Loop :- An infinite loop is a loop that continues to execute indefinitely because the terminating condition is never met.")
count = 1
while count <= 5:
    print(count)
    break  # This will break the loop after the first iteration to prevent an actual infinite loop. can not use {break} then you see infinite loop.


# Devops Server Retry Monitor
print("\nDevops Server Retry Monitor :- ")
attempts = 1
max_attempts = 3
while attempts <= max_attempts:
    print(f"Checking server...Attempt {attempts}")
    attempts += 1

print ("\nMonitoring complete. All attempts finished.")
