### --- OOP Email Simulator --- ###

# --- Email Class --- #
class Email:

    # Declare the class variable, with default value, for emails. 
    has_been_read = False

    # Initialise an empty list to store the email objects.
    inbox = []

     # Initialise the instance variables for emails.
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
    
    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True

# --- Functions --- #
def populate_inbox():
    # Create 3 sample emails and add them to the Inbox list.
    sample_emails = [
        {
            'email_address': 'bestie@sample1.com',
            'subject_line': 'Hi! Coffee?',
            'email_content': 'Hi, how are you? Going for a coffee tomorrow?'
        },
        {
            'email_address': 'manager.work@sample2.com',
            'subject_line': 'Weekly Rota',
            'email_content': 'Please see below the weekly rota...'
        },
        {
            'email_address': 'hyperion@sample3.com',
            'subject_line': 'Almost...',
            'email_content': 'You almost finish your tasks. You can do it!'
        }
    ]
    for email in sample_emails:
        email_object = Email(email['email_address'], email['subject_line'], email['email_content'])
        Email.inbox.append(email_object)

# Create a function which prints the email’s subject_line, along with a corresponding number.
def list_emails():
    print("\nInbox:")
    # Print the list of emails and their status (read or unread).
    for index, email in enumerate(Email.inbox, start = 1):
        status = "Read" if email.has_been_read else "Unread"
        print(f"{index}. {status} - {email.subject_line}")

# Display the selected email's details and mark it as read.
def read_email(index):
    if 1 <= index <= len(Email.inbox):
        selected_email = Email.inbox[index - 1]
        print("\nEmail Details:")
        print(f"From: {selected_email.email_address}")
        print(f"Subject: {selected_email.subject_line}")
        print(f"\nContent: {selected_email.email_content}")
        selected_email.mark_as_read()
        print(f"\nEmail from {selected_email.email_address} has been marked as read.")
    else:
        print("Invalid email number. Please try again.")

# --- Email Program --- #
# Populate the inbox with sample email objects.
populate_inbox()

menu = True

while menu:
    try:
        # Display the menu options and prompt the user to make a choice
        user_choice = int(input('''\nWould you like to:
        
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))

        if user_choice == 1:
            # If the user chooses to read an email, display the list of emails and prompt them to select one from the list.
            list_emails()

            while True:
                    index = int(input("\nEnter the email number you want to read: "))
                    
                    if 1 <= index <= len(Email.inbox):
                        read_email(index)
                        break
                    
                    else:
                        print("Oops - incorrect input. Please try again.")
               

        elif user_choice == 2:
        # If the user chooses to view unread emails, display only the unread emails and their subject lines.
            print("\nUnread Emails:\n")
            unread_emails_count = 0
        
            for index, email in enumerate(Email.inbox, start = 1):
                if not email.has_been_read:
                    print(f"{index}. {email.subject_line}")
                    unread_emails_count += 1

            if unread_emails_count == 0:
                print("You have no more unread emails.")

        elif user_choice == 3:
            # If the user chooses to quit the application, print a goodbye message and exit the loop.
            print("Thank you for using the Email Simulator. Goodbye!")
            menu = False

        else:
            print("Oops - incorrect input. Please try again.")

    # Exception handling in case the user enter characters 
    except ValueError:
        print ("Invalid character. Please try again.")