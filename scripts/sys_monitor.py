import os
import datetime

def get_stats():
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    load = os.getloadavg()[0] # System load
    mem = os.popen('free -m').readlines()[1].split()[2] # Used RAM in MB
    
    log_entry = f"[{time}] Load: {load} | Used RAM: {mem}MB\n"
    
    with open("system_log.txt", "a") as f:
        f.write(log_entry)
    print(f"Logged: {log_entry.strip()}")

if __name__ == "__main__":
    get_stats()
