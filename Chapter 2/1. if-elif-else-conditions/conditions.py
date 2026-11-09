# Conditions in Python
print("Welcome to the conditions in Python !")
print("\nConditions :- Situation base Decision.")

# if condition
print("\nif condition :- if condition use for check specific condition.")
cpu_usage = 95

if cpu_usage > 90:
    print("\nCPU usage is Critical!")

# if-else condition
print("\nelse condition :- else condition use for take action when if condition is false.")
cpu_usage = 70
if cpu_usage > 90:
    print("\nCPU usage is Critical!")
else:
    print("\nCPU usage is Normal.")

# if-elif-else condition
print("\nelif condition :- elif condition use for check multiple condition and take action.")
cpu_usage = 85

if cpu_usage > 90:
    print("\nCPU usage is Critical!")
elif cpu_usage > 80:
    print("\nCPU Warnning!")
else:
    print("\nCPU usage is Normal.")