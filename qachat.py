import streamlit as st
import google.generativeai as genai

# Directly set the API key
GOOGLE_API_KEY = "AIzaSyBcTNAlCQvlasRjkesgTI5Fn1icNEq89rw"
genai.configure(api_key=GOOGLE_API_KEY)

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Initialize our Streamlit app
st.set_page_config(page_title="Q&A Demo")

st.header("Ayushmitra-BOT")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Input: ", key="input")
submit = st.button("Ask question")

if submit and input:
    response = get_gemini_response(input)
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is")
    for chunk in response:
        if (not(chunk.text)):
            st.write('Unable to fetch data !!!! Contact the specialist') 
        else:
            st.write(chunk.text)
        

        st.session_state['chat_history'].append(("Bot", chunk.text))

# st.subheader("The Chat History is")
# for role, text in st.session_state['chat_history']:
#     st.write(f"{role}: {text}")
st.header("@ Team Ayushmitra")
