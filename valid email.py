import re

def detect_emails(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    return emails

while True:
    # Get user input
    user_input = input("Enter some text: ")

    # Detect emails in the input
    emails = detect_emails(user_input)

    # Print the detected emails
    if emails:
        print("Detected email:")
        print(emails[0])
        break
    else:
        print("No emails detected. Try again!")

    # Ask user if they want to try again or exit
    choice = input("Do you want to try again? (1) Yes, (2) No: ")
    if choice == "2":
        break
    elif choice != "1":
        print("Invalid choice. Please enter 1 or 2.")