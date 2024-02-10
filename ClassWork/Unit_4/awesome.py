# awesome_module.py

import random

class AwesomeModule:
    def __init__(self):
        self.inspirational_quotes = [
            "Believe you can and you're halfway there. -Theodore Roosevelt",
            "The only way to do great work is to love what you do. -Steve Jobs",
            "Don't watch the clock; do what it does. Keep going. -Sam Levenson",
            "Success is not final, failure is not fatal: It is the courage to continue that counts. -Winston Churchill",
            "The only limit to our realization of tomorrow will be our doubts of today. -Franklin D. Roosevelt",
            "Strive not to be a success, but rather to be of value. -Albert Einstein",
            "Your time is limited, don't waste it living someone else's life. -Steve Jobs",
            "The future belongs to those who believe in the beauty of their dreams. -Eleanor Roosevelt",
        ]

    def get_inspirational_quote(self):
        return random.choice(self.inspirational_quotes)

# Example usage:
if __name__ == "__main__":
    awesome_instance = AwesomeModule()
    quote = awesome_instance.get_inspirational_quote()
    print("Awesome Quote:", quote)
