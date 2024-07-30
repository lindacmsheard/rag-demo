import os
import streamlit as st
import requests
from dotenv import load_dotenv

load_dotenv()
index_name = os.getenv("AZURE_AI_SEARCH_INDEX_NAME")
search_service_name = os.getenv("AZURE_AI_SEARCH_SERVICE_NAME")
api_key = os.getenv("AZURE_AI_SEARCH_KEY")
api_version = os.getenv("AZURE_AI_SEARCH_API_VERSION")

st.title("Chat with Azure Search")  
  
# Create a text input for user query  
user_query = st.text_input("Enter your query:")  
result_limit = st.number_input("Number of results to return:", min_value=1, max_value=100, value=10)  
  
# Define the function to call Azure Search API  
def call_azure_search_api(query, top):  
    url = f"https://{search_service_name}.search.windows.net//indexes/{index_name}/docs?api-version={api_version}&search={query}&$top={top}"  
    headers = {  
        'Content-Type': 'application/json',  
        'api-key': api_key 
    }  
      
    response = requests.get(url, headers=headers)  
    return response.json()  
  
# Create a button to submit the query  
if st.button("Search"):  
    response = call_azure_search_api(user_query, result_limit)  
    st.write(response)  