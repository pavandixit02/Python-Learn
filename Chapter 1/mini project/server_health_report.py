# Phase 1 Final Mini Project
# Ab ek project banayenge jo tumhare ab tak ke Python fundamentals ko combine karega.


# Project: Server Information & Health Report
# Beginner level
# Python se server ki information aur manually entered metrics ka formatted report generate karna.


## Project requirements
# File ka naam rakho:
# server_health_report.py

## Step 1 — User se input lo
# - Server name
# - Server IP
# - Operating system
# - CPU usage
# - Memory usage
# - Disk usage
# - Server status

## Step 2 — Data process karo
# - Server name ko uppercase mein display karo.
# - Server IP ko strip karo.
# - Operating system ko strip karo.
# - Server status ko lowercase mein normalize karo.
# - Unwanted spaces remove karo.
# - CPU, memory aur disk ko integer mein convert karo.
# - Server name aur IP ki length display karo.

## Step 3 — Report generate karo
# Expected output ka example: ##
# ========================================
#         SERVER HEALTH REPORT
# ========================================

# Server Name : WEB01
# Server IP   : 192.168.1.10
# OS          : Ubuntu
# Status      : running

# CPU Usage   : 75%
# Memory Usage: 60%
# Disk Usage  : 85%

# Server Name Length : 5
# IP Length          : 12

# ========================================




## Solve The Problem

server_name = input("Enter Server Name : ")
server_ip = input("Enter Server IP : ")
server_os = input("Enter Server OS : ")
cpu_usage = input("Enter CPU Usage : ")
memory_usage = input("Enter Memory Usage : ")
disk_usage = input("Enter Disk Usage : ")
server_status = input("Enter Server Status : ")

print("===============================")
print("      SERVER HEALTH REPORT     ")
print("===============================\n")
print(f"Server Name     : {server_name.upper()}")
print(f"Server IP       : {server_ip.strip()}")
print(f"Server OS       : {server_os.strip()}")
print(f"Server Status   : {server_status.strip().lower()}")


print(f"\nCPU Usage       : {int(cpu_usage)}%")
print(f"Memory Usage    : {int(memory_usage)}%")
print(f"Disk Usage      : {int(disk_usage)}%")



print(f"\nServer Name Length   : {len(server_name)}")
print(f"Server IP Length     : {len(server_ip)}")
print("\n===============================")