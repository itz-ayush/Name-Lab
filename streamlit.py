import streamlit as st
from main import generate_names
# Set the title of the Streamlit app
st.title("Name Labs")

# Add a descriptive text below the title
st.write("Tired of finding names for your business, YouTube channel, or startup? You are at the right place.")

# Ask the user what they are searching a name for
search_for = st.text_input("What are you searching names for?")

# Ask the user about the genre or what the business is about
genre = st.text_input("What is the genre or what is the business about?")

# Ask if the user wants a specific keyword in the name (optional)
keyword = st.text_input("Do you want a specific keyword in the name? (Optional)")

# Add a button to generate answers
if st.button("Generate Names"):
    with st.spinner("Generating names..."):
        if search_for and genre:
            response = generate_names(search_for, genre, keyword)
            st.write("Here are some name suggestions:")
            names = [name.strip() for name in response.split(",") if name.strip()]
            st.write("\n".join(f"- {name}" for name in names))
        else:
            st.write("Please enter the information about what you are searching names for and the genre or business.")
