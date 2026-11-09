# Task 01 :-

print("\nTask 01 :- Print numbers from 1 to 10 using while loop.\n")
count = 1
while count <= 10:
    print(count)
    count += 1

# Task 02 :-
print("\n\nTask 02 :- Print Reverse numbers from 10 to 1 using while loop.\n")
count = 10
while count >= 1:
    print(count)
    count -= 1

# Task 03 :-
print("\n\nTask 03 :- Server Retry System using while loop. max=5, with numbering, all attempts complete\n")
print("==== SERVER RETRY MONITOR ====\n")
attempts = 1
while attempts <= 5:
    print(f"Checking server...Attempt {attempts}")
    attempts += 1
print("\nMonitoring complete. All attempts finished.\n")


# Task 04 :- user input se monitoring System
print("\nTask 04 :- User Input se Server Retry System using while loop.\n")
user_input = int(input("Enter the number of attempts for server monitoring: "))
print("\n==== SERVER RETRY MONITOR ====\n")
attempts = 1
while attempts <= user_input:
    print(f"Checking server...Attempt {attempts}")
    attempts += 1
print("\nMonitoring complete. All attempts finished.")
