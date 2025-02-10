import streamlit as st
import nltk
from transformers import pipeline 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

chatbot = pipeline("text-generation", model="medllama2")


def healthcare_chatbot(user_input):
    if "symptoms" in user_input:
        return "It seems like you're experiencing symptoms. Please consult a doctor."
    elif "appointment" in user_input:
        return "Would you like me to schedule an appointment for you?"
    elif "medication" in user_input:
        return "It's important to take your prescribed medication regularly."
    else:
        response = chatbot(user_input,max_length=300,num_return_sequences=1)
        return response[0]['generated_text']

def main():
    st.title("Healthcare Assist Chatbot")
    user_input = st.text_input("How can I assist you today?", "")
    if st.button("Submit"):
        if user_input:
            st.write("User:",user_input)
            response = healthcare_chatbot(user_input)
            st.write("Assistant:", response)
        else:
            st.write("Please enter a query to get started.")
if __name__=="__main__":
    main()