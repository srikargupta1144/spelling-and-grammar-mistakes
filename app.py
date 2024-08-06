# we are using language_tool_python for this project, it except 500 words

# first we take input from user and detect grammar & spelling mistakes, then we will use the output of language_tool_python to correct the mistakes

import streamlit as st
import language_tool_python 

# text correcting functions
def text_correction(text):
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)
    corrected_text = language_tool_python.utils.correct(text, matches)
    return corrected_text

def main():
    st.header('Spelling & Grammar Mistakes Correction App')

    # Input text from user
    user_input = st.text_area("Enter text (up to 500 words):", height=200)

    # Check if the input is within the 500-word limit
    if len(user_input.split()) > 500:
        st.error("The text exceeds the 500-word limit. Please shorten it.")
    else:
        if st.button('Correct Mistakes'):
            result = text_correction(user_input)
            st.write("Corrected Text:")
            st.write(result)

if __name__ == '__main__':
    main()
