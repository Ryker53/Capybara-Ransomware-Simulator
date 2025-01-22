Capybara Ransomware Simulator: An Educational Cybersecurity Project

Overview

The Capybara Ransomware Simulator is a Python-based project designed to simulate the behavior of ransomware for educational purposes. This project demonstrates key concepts in cybersecurity, such as file encryption, user interaction with ransom demands, and ethical considerations for malware research. Featuring a humorous Capybara-themed GUI, this project is both technically complex and creatively engaging.

Objectives

Educational Purpose: To gain hands-on experience with encryption, GUI design, and multithreading while simulating a real-world cybersecurity scenario.

Demonstrate Technical Skills: Showcase Python programming skills and understanding of ransomware behavior in a controlled and ethical manner.

Research and Documentation: Provide a detailed exploration of how ransomware operates and how technical concepts can be implemented responsibly.

Features

1. File Encryption

Utilizes the cryptography library to implement AES encryption for simulating file encryption.

Files in a target directory are encrypted sequentially, with updates displayed dynamically.

2. Capybara-Themed GUI Lock Screen

Designed with tkinter, the lock screen features:

A full-screen window with a Capybara image as the background.

A countdown timer (5 minutes) to create urgency.

Real-time updates on encryption progress.

Ransom note text displayed prominently.

3. Multithreading

Leverages Python’s threading library to run the lock screen and encryption process concurrently, simulating real-world ransomware behavior.

4. Payment Confirmation Mechanism

Unlocks the system when a file named PAYMENT_CONFIRMED.TXT is detected in the working directory.

Provides flexibility for users to "pay the ransom" and stop the encryption process.

5. Ethical Considerations

Designed and tested in an isolated virtual environment to prevent unintended harm.

Clear documentation and safeguards ensure it cannot be misused maliciously.

Automatic termination when the timer expires to avoid forcing a system restart.

Implementation Details

File Encryption

Encryption Algorithm: AES encryption using a randomly generated key.

Process:

A ransom note is generated with the encryption key and saved in the target directory.

Files in the directory are encrypted sequentially.

Lock Screen

GUI Framework: tkinter

Visual Elements:

Full-screen Capybara-themed background image.

Dynamic text displaying file encryption progress.

Countdown timer that triggers program termination upon expiration.

Payment Detection:

Periodically checks for a PAYMENT_CONFIRMED.TXT file.

Unlocks the system and stops encryption if payment is confirmed.

Multithreading

Separate threads are used to:

Run the lock screen GUI.

Execute the encryption process in the background.

Technical Challenges

Synchronizing GUI and Background Processes

Implementing multithreading to allow the GUI to update dynamically while files are encrypted required careful synchronization.

Ethical Safeguards

Ensuring the project could not be misused involved adding features like safe program termination, requiring controlled testing environments such as virtual machines, and including clear disclaimers about its educational intent. These safeguards aim to prevent misuse while promoting responsible learning and exploration.

Timer and Termination

Automatically closing the program upon timer expiration involved integrating clean-up routines for threads and GUI processes. The program utilized Python’s threading library to ensure the GUI and encryption processes terminated gracefully without leaving orphan threads. Testing involved running the simulator in isolated virtual environments to confirm that all processes stopped correctly upon timer expiration and no additional user intervention was required.

Results

Functional Outcomes

Successfully simulated ransomware behavior in a controlled environment.

Demonstrated real-time file encryption by encrypting files in a target directory sequentially using the cryptography library. The encryption key was dynamically generated and included in the ransom note for simulation purposes.

Displayed visual feedback via a full-screen GUI lock screen built with tkinter. The GUI included:

A dynamic countdown timer to simulate urgency.

Real-time updates showing the progress of file encryption.

Enabled a payment confirmation mechanism where creating a specific file (PAYMENT_CONFIRMED.TXT) would stop the encryption process and unlock the system.

Provided an engaging and educational experience by combining technical cybersecurity concepts with creative, themed design.

Successfully simulated ransomware behavior in a controlled environment.

Demonstrated real-time file encryption with visual feedback via the GUI.

Provided an engaging and educational experience for understanding ransomware mechanics.

