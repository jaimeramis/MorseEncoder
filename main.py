# Import de JSON module.
import json

class MorseCodeEncoder:
    def __init__(self, data_file):
        # Load the data from the provided file.
        with open(data_file, 'r') as file:
            self.data = json.load(file)
    
    def validation(self, user):
        # Validate the user input by removing any invalid characters.
        valid_characters = self.data.keys()
        clean_user = "".join([char for char in user if char in valid_characters])
        return clean_user

    def encode(self, user):
        # Encode the validated user input into Morse code.
        answer = ""
        for u in self.validation(user):
            answer += self.data[u]
        return answer

    def run_app(self):
        # Main method to run the app.
        print("\n")
        title = "Morse Code Encoder\n"
        print(title.upper())
        user = input("Put a word or a phrase: ").upper()
        print(f"Morse code: {self.encode(user)}")

    def reset(self):
        # Reset the program (for demonstration, it just reruns the app).
        print("\n")
        print("Press R to Reset the program")
        print("Press E to Exit the program")
        result = input("What are you going to do?: ").upper()
        if result == "E":
            print("\nExiting the program. Goodbye!\n")
            return False  # Exit the loop.
        elif result == "R":
            self.run_app()
            return True  # Continue the loop.
        else:
            print("\nThat's not a valid answer. Try again...\n")
            return True  # Continue the loop.

# Usage of the class
if __name__ == "__main__":
    encoder = MorseCodeEncoder("data.json")  # Initialize the class with your data file.
    encoder.run_app()  # Run the app once.

    reset = True
    while reset:
        reset = encoder.reset()  # Handle the reset or exit logic.
