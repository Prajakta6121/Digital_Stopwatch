import time

def format_time(seconds):
    mins = int(seconds // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 100)
    return f"{mins:02}:{secs:02}.{millis:02}"

def stopwatch():
    start_time = None
    elapsed_time = 0
    running = False

    while True:
        print("\n=== DIGITAL STOPWATCH ===")
        print("1. Start")
        print("2. Stop")
        print("3. Reset")
        print("4. Show Time")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            if not running:
                start_time = time.time() - elapsed_time
                running = True
                print("⏱️ Stopwatch started.")
            else:
                print("⚠️ Already running.")

        elif choice == "2":
            if running:
                elapsed_time = time.time() - start_time
                running = False
                print(f"⏸️ Stopwatch stopped at {format_time(elapsed_time)}.")
            else:
                print("⚠️ Stopwatch is not running.")

        elif choice == "3":
            elapsed_time = 0
            start_time = None
            running = False
            print("🔄 Stopwatch reset.")

        elif choice == "4":
            if running:
                current = time.time() - start_time
                print(f"⏳ Elapsed time: {format_time(current)}")
            else:
                print(f"🕒 Time: {format_time(elapsed_time)}")

        elif choice == "5":
            print("👋 Exiting Stopwatch.")
            break

        else:
            print("❌ Invalid option.")
if __name__ == "__main__":
    stopwatch()
    
