import urllib.request
import json
import os
import ssl
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# UI for the chat app

st.title("Chat with PromptFlow")  

# Create a selectbox for mode selection  
mode = st.selectbox("Select Mode:", ["Chat", "Chat with your data"])  

# Create a text input for user query  
user_query = st.text_input("Enter your query:")  

if mode=="Chat with your data":
    result_limit = st.number_input("Number of search results to use:", min_value=1, max_value=100, value=10)
else:
    result_limit = None

# def allowSelfSignedHttps(allowed):
#     # bypass the server certificate verification on client side
#     if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
#         ssl._create_default_https_context = ssl._create_unverified_context

# allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.


# Define a function to call my promptflow endpoint
def call_aml_endpoint(query, mode, top):
    
    if mode=="Chat with your data":
        data = {
            "question": query,
            "top_k": top or 5
        }
        deployment_name = 'aml-rag-endpoint-2'
    else:
        data = {
            "question": query,
            "chat_history": []
        }
        deployment_name = 'aml-rag-endpoint-1'


    body = str.encode(json.dumps(data))

    url = 'https://aml-rag-endpoint.uksouth.inference.ml.azure.com/score'
    api_key = os.getenv("PF_API_KEY")
    
    # The azureml-model-deployment header will force the request to go to a specific deployment.
    # Remove this header to have the request observe the endpoint traffic rules
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'azureml-model-deployment': deployment_name }

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)

        result = response.read()
        print(result)
        return json.loads(result)
    
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(error.read().decode("utf8", 'ignore'))
        return "error"


# Create a button to submit the query  
if st.button("Send"):  
    response = call_aml_endpoint(user_query, mode, result_limit)  
    st.write(response)  