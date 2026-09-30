# Project-6 : File Operator

import os
from datetime import datetime


class JournalManager:
    """Handles all journal operations."""

    def __init__(self, filename="journal.txt"):
        self.filename = filename

    def read_entries(self):

        with open(self.filename, "r") as file:
            content = file.read()

        if content == "":
            return []

        return content.split("\n\n")

    def add_entry(self):
        text = input("\nEnter your journal entry (press Enter to finish) :\n")

        if text.strip() == "":
            print("Entry cannot be empty.")
            return

        # Timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            with open(self.filename, "a") as file:
                file.write(f"Timestamp : [{timestamp}]\n{text}\n\n")
            print("\nEntry added successfully!")
        except Exception as error:
            print(f"Error: Something went wrong ({error}).")

    def view_entries(self):
        try:
            entries = self.read_entries()

            if len(entries) == 0:
                print("\nNo journal entries found. Start by adding a new entry!")
                return

            print("\nYour Journal Entries :")
            print("-" * 33)
            for entry in entries:
                print(entry)
                print()
        except FileNotFoundError:
            print("\nNo journal entries found. Start by adding a new entry!")
        except Exception as error:
            print(f"\nError: Something went wrong ({error}).")

    def search_entries(self):
        keyword = input("\nEnter a keyword or date to search : ")

        if keyword.strip() == "":
            print("Search text cannot be empty.")
            return

        try:
            entries = self.read_entries()

            matches = []
            for entry in entries:
                if keyword.lower() in entry.lower():
                    matches.append(entry)

            if len(matches) == 0:
                print(f"\nNo entries were found for the keyword : {keyword}.")
                return

            print("\nMatching Entries :")
            print("-" * 33)
            for entry in matches:
                print(entry)
                print()
        except FileNotFoundError:
            print("\nError: The journal file does not exist. Please add a new entry first.")
        except Exception as error:
            print(f"\nError: Something went wrong ({error}).")

    def delete_entries(self):
        confirm = input("\nAre you sure you want to delete all entries? (y/n) : ")

        if confirm.strip().lower() != "y":
            print("Delete cancelled. Your entries are safe.")
            return

        try:
            # Deleting the file
            os.remove(self.filename)
            print("\nAll journal entries have been deleted.")
        except FileNotFoundError:
            print("\nNo journal entries to delete.")
        except Exception as error:
            print(f"\nError: Something went wrong ({error}).")


# ---------- Main program ----------
journal = JournalManager()

print("\nWelcome to Personal Journal Manager!")

while True:
    print("Please select an option:\n")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    choice = input("\nEnter your choice : ")

    match choice:
        case "1":
            journal.add_entry()
        case "2":
            journal.view_entries()
        case "3":
            journal.search_entries()
        case "4":
            journal.delete_entries()
        case "5":
            print("\nThank you for using Personal Journal Manager. Goodbye!")
            break
        case _:
            print("\nInvalid option. Please select a valid option from the menu.")