import streamlit as st
from langchain.llms import OpenAI

#setting the title of the Streamlit application
st.title('Simple LLM-App 🤖')

#creating a sidebar input widget for the OpenAI  API key, input type is password  for security
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

# defining a function to generate a response using the OpenAI language model

def generate_response(input_text):
    #initializing the OpenAI language model with a specific temperature and API key
    llm = OpenAI(temperature=0.7,openai_api_key=openai_api_key)
    #Displaying the generated response as an informational message in the Streamlit app
    st.info(llm(input_text))

# creating a form in thestreamlit app for user input
with st.form('my_form'):
    # adding a text area for user input
    text = st.text_area('Enter text:','')
    # adding a submit button for the form
    submitted = st.form_submit_button('Submit')
    # Displaying a warning if the entered API key does not start with 'sk-'
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!',icon='⚠️')
        # if the form is submitted and the API key is valid, generate a response
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)