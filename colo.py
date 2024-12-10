import streamlit as st
import random

# Define the list of colors with their respective hex codes
colors = {
    "Red": "#FF0000",
    "Blue": "#0000FF",
    "Green": "#008000",
    "Yellow": "#FFFF00",
    "Orange": "#FFA500",
    "Purple": "#800080",
    "Pink": "#FFC0CB",
    "Brown": "#A52A2A",
    "Black": "#000000",
    "White": "#FFFFFF",
}

# Initialize session state variables
if "correct_color" not in st.session_state:
    st.session_state.correct_color = random.choice(list(colors.keys()))
if "score" not in st.session_state:
    st.session_state.score = {"correct": 0, "incorrect": 0}
if "attempts_left" not in st.session_state:
    st.session_state.attempts_left = 5

# Set up the Streamlit app
st.title("Color Guessing Game")
st.write("Guess the color I'm thinking of!")

# Display the color icons
st.write("Here are the available colors:")
for color_name, hex_code in colors.items():
    st.markdown(
        f"<span style='color:{hex_code}; font-size:20px;'>⬤</span> {color_name}",
        unsafe_allow_html=True,
    )

# Input for the user's guess
user_guess = st.text_input("Enter your guess:", value="")

# Button to submit the guess
if st.button("Submit Guess"):
    if st.session_state.attempts_left > 0:
        if user_guess.capitalize() == st.session_state.correct_color:
            st.success(f" Correct! The color was {st.session_state.correct_color}.")
            st.session_state.score["correct"] += 1
            # Reset the game
            st.session_state.correct_color = random.choice(list(colors.keys()))
            st.session_state.attempts_left = 5
            st.write("I've thought of a new color. Try again!")
        else:
            st.session_state.score["incorrect"] += 1
            st.session_state.attempts_left -= 1
            if st.session_state.attempts_left > 0:
                st.error(f" Incorrect! You have {st.session_state.attempts_left} attempts left. Try again.")
            else:
                st.error(f" Game Over! The correct color was {st.session_state.correct_color}.")
                st.session_state.correct_color = random.choice(list(colors.keys()))
                st.session_state.attempts_left = 5
                st.write("I've thought of a new color. Try again!")
    else:
        st.warning("No attempts left! Resetting the round.")
        st.session_state.correct_color = random.choice(list(colors.keys()))
        st.session_state.attempts_left = 5

# Display a hint button
if st.button("Hint"):
    hint = f"The color starts with '{st.session_state.correct_color[0]}'."
    if st.session_state.attempts_left <= 3:  # Provide an additional hint if attempts are low
        hint += f" It has {len(st.session_state.correct_color)} letters."
    st.write(hint)

# Display the current score
st.write(f"Score: {st.session_state.score['correct']} Correct, {st.session_state.score['incorrect']} Incorrect")

# Restart button to reset the game
if st.button("Restart Game"):
    st.session_state.score = {"correct": 0, "incorrect": 0}
    st.session_state.correct_color = random.choice(list(colors.keys()))
    st.session_state.attempts_left = 5
    st.write("Game reset! Let's start fresh.")

# Add a new feature: display the number of attempts left
st.write(f"Attempts left: {st.session_state.attempts_left}")

# Add a new feature: display the correct color after the game is over
if st.session_state.attempts_left == 0:
    st.write(f"The correct color was {st.session_state.correct_color}.")