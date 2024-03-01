# Import necessary libraries
import streamlit as st
import random

# Define the SocialAnxietyAI class
class SocialAnxietyAI:
    def __init__(self):
        # Encouragement messages
        self.encouragements = [
            "You're doing great!",
            "Take deep breaths, you've got this!",
            "It's okay to feel nervous, but don't let it hold you back.",
            "You are stronger than your anxiety.",
            "Focus on the present moment, you're safe.",
            "Believe in yourself, you can handle this.",
            "You're not alone, we're here to support you.",
            "One step at a time, you're making progress.",
            "You are valued and appreciated just as you are.",
            "Don't be too hard on yourself, progress is progress no matter how small."
        ]

    def get_encouragement(self):
        """Returns a random encouragement message."""
        return random.choice(self.encouragements)

# Main function
def main():
    # Create an instance of the SocialAnxietyAI class
    social_anxiety_ai = SocialAnxietyAI()

    # Set the title and introductory text
    st.title("Social Anxiety AI App")
    st.write("If you're feeling anxious, let me offer you some support:")

    # Create a button for receiving an encouragement message
    if st.button("Get Encouragement"):
        # Call get_encouragement method to get a random message
        message = social_anxiety_ai.get_encouragement()
        # Display the message
        st.write("Social Anxiety AI:", message)

# Execute the main function
if __name__ == "__main__":
    main()
