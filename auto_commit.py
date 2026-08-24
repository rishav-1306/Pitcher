import subprocess
import datetime
import time
import os

def make_commit(index: int):
    timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    date_str = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    
    os.makedirs("logs", exist_ok=True)
    log_path = os.path.join("logs", "activity.log")
    
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"Automated contribution #{index} - {timestamp}\n")
        
    subprocess.run(["git", "add", log_path], check=True)
    subprocess.run(["git", "commit", "-m", f"chore(activity): contribution #{index} for {date_str} [skip ci]"], check=True)
    print(f"Commit #{index} generated successfully at {timestamp}")

def main():
    print("Generating 3 automated commits...")
    for i in range(1, 4):
        make_commit(i)
        time.sleep(1)
    
    print("\nPushing commits to remote repository...")
    subprocess.run(["git", "push"], check=True)
    print("Done! 3 contributions pushed successfully.")

if __name__ == "__main__":
    main()
