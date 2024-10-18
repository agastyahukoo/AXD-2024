# main.py

import sys
import threading
from tasks import task1, task2, task3, task4

# Project Information
PROJECT_NAME = "OpenCV-Drone"
VERSION = "v0.1"
DESCRIPTION = (
    "This project is developed by the AeroXperts team at MPSTME for the AeroTHON 2024.\n\n"
    "This project utilizes OpenCV for real-time computer vision processing to enhance the drone’s performance in AeroTHON 2024. "
    "The system is designed for Unmanned Aerial Competition (UAC) tasks such as object detection, tracking, and autonomous navigation.\n\n"
    "Key features include:\n"
    "- Real-time Object Detection: Implementing state-of-the-art algorithms for detecting and classifying objects using OpenCV libraries.\n"
    "- Motion Tracking: Incorporating motion tracking algorithms to follow moving objects and ensure precise aerial positioning.\n"
    "- Autonomous Navigation: Enabling the drone to navigate autonomously by interpreting camera feed and performing obstacle avoidance.\n"
    "- Hardware Integration: Seamless integration with onboard systems to process data efficiently during flight.\n"
    "- Performance Optimization: Ensuring minimal latency for real-time decision making with optimized processing techniques."
)
GITHUB_URL = "https://github.com/agastyahukoo/OpenCV-Drone"
HARDWARE_USED = (
    "Hardware Used:\n"
    "- Raspberry Pi 5 (4GB)\n"
    "- Geekworm M901 PCIe to M.2 Key-M NVMe SSD Adapter for Raspberry Pi\n"
    "- Crucial P5 Plus PCIe 4.0 M.2 2280 SSD"
)

def run_task(task_number):
    try:
        if task_number == 1:
            task1.run()
        elif task_number == 2:
            task2.run()
        elif task_number == 3:
            task3.run()
        elif task_number == 4:
            task4.run()
        else:
            print("Invalid task number.")
    except Exception as e:
        print(f"An error occurred while running Task {task_number}: {e}")

def main():
    print(f"{PROJECT_NAME} - {VERSION}\n")
    print(DESCRIPTION)
    print("\n" + HARDWARE_USED)
    print(f"\nGitHub Repository: {GITHUB_URL}\n")

    print("Select a task to execute:")
    print("1. Task 1")
    print("2. Task 2")
    print("3. Task 3")
    print("4. Task 4")
    print("Q. Quit")

    while True:
        choice = input("Enter your choice (1-4) or 'Q' to quit: ").strip().lower()
        if choice in ['1', '2', '3', '4']:
            task_number = int(choice)
            print(f"\nRunning Task {task_number}...")
            run_task(task_number)
            print(f"Task {task_number} completed.\n")
            print("Returning to main menu.\n")
            print("Select a task to execute:")
            print("1. Task 1")
            print("2. Task 2")
            print("3. Task 3")
            print("4. Task 4")
            print("Q. Quit")
        elif choice == 'q':
            print("Exiting the program.")
            sys.exit(0)
        else:
            print("Invalid input. Please enter a number between 1 and 4, or 'Q' to quit.")

if __name__ == "__main__":
    main()
