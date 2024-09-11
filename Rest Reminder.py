import tkinter as tk
import random
import pyttsx3
import time

# Initialize the TTS engine
engine = pyttsx3.init()

# Function to speak the reminder
def speak_reminder():
    engine.say("Hi Rizvi, please rest for 5 minutes")
    engine.runAndWait()

# Function to show the notification and change background colors for 5 minutes
def show_notification():
    # Create the main window
    root = tk.Tk()

    # Get screen dimensions to center the window
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Set window size (300x150) and position to center
    window_width = 400
    window_height = 200
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    # Set the title and message
    root.title("Rest Reminder")

    # Message to display "Hi Rizvi" and "Please rest for 5 minutes"
    message_hi = tk.Label(root, text='@ "Muhammad Abdullh Rizvi"', font=("Verdana", 16), fg="blue")
    message_rest = tk.Label(root, text="Please rest for 5 minutes", font=("Helvetica", 16))

    # Pack the messages to the window
    message_hi.pack(pady=10)
    message_rest.pack(pady=10)

    # Speak the reminder
    speak_reminder()

    # Function to change the background color randomly
    def change_background_color():
        colors = ["red", "green", "blue", "yellow", "purple", "orange", "pink"]
        root.configure(bg=random.choice(colors))
        # Schedule the next color change after 1000 milliseconds (1 second)
        root.after(1000, change_background_color)

    # Start changing the background color every second
    change_background_color()

    # Set a timer to close the window after 5 minutes (300 seconds)
    root.after(300000, root.destroy)  # 300000 milliseconds = 5 minutes

    # Start the Tkinter main loop to keep the window active
    root.mainloop()

# Main function to wait for 1.5 hours and show notification
def main():
    while True:
        print("Waiting for 1.5 hours...")
        time.sleep(5400)  # Wait for 1.5 hours (5400 seconds)
        show_notification()

# Run the main loop
if __name__ == "__main__":
    main()
