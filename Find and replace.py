def main():
    # Step 1: Take a word as input from the user
    word_to_find = input("Enter the word to search for: ")

    # Step 2: Read the file and find the frequency of the word
    file_path = input("Enter the file name (with extension) to analyze: ")
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            word_count = content.lower().count(word_to_find.lower())
            print(f"The word '{word_to_find}' appears {word_count} time(s) in the file.")
    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")
        return

    # Step 3: Ask if the user wants to replace the word
    replace_choice = input("Do you want to replace the word? (yes/no): ").lower()
    if replace_choice == "yes":
        new_word = input("Enter the new word to replace it with: ")
        updated_content = content.replace(word_to_find, new_word)
        with open(file_path, 'w') as file:
            file.write(updated_content)
        print(f"All occurrences of '{word_to_find}' have been replaced with '{new_word}' in the file.")

# Run the program
if __name__ == "__main__":
    main()