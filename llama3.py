import boto3
import json

prompt_data="""
Act as Virat kohli and give some insights abouts cricket
"""
#with the help of boto3 we are able to connect ot the bedrock
bedrock=boto3.client(service_name='bedrock-runtime')

# In the format of the body given in text.json file like keey value pair
payload={
    "prompt": prompt_data,
    "max_gen_len":512,
    "temperature":0.5,
    "top_p":0.9
}

body=json.dumps(payload) # converting into json

model_id="meta.llama3-70b-instruct-v1:0"

# Call the Model Using Bedrock API
response=bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json"
)

# Retrieves the response body (raw data) from the API and converts to  json
response_body=json.loads(response.get("body").read())
# Extracts the text generated by the AI model from the response
response_text=response_body['generation']
print(response_text)