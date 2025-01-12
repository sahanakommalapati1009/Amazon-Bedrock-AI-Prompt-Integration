# Amazon Bedrock AI Prompt Integration
This project demonstrates how to leverage Amazon Bedrock to interact with foundation models, enabling AI-generated insights and responses based on custom prompts.
## Features
* Connects to AWS Bedrock using the boto3 library.
* Sends custom prompts to a foundation model (meta.llama3-70b-instruct-v1:0) hosted on AWS Bedrock.
* Processes the AI-generated response and outputs it in a user-friendly format.
* Includes configurable parameters for AI responses:
  - Prompt: User-defined text to guide AI responses.
  - Max Generation Length: Limits the length of AI-generated content.
  - Temperature & Top-p: Controls randomness and token sampling for creative responses.
## Files
1. llama3.py: Python script for connecting to AWS Bedrock, sending prompts, and retrieving responses​.
2. requirements.txt: Dependencies required for running the project (e.g., boto3, awscli)​.
3. test.json: Example payload format for interacting with the Bedrock model API​.
## Use Case
The project acts as a template to build and test AI interactions, such as:
* Motivational text generation.
* Industry-specific insights.
* Creative content production.
## Usage
1. Install dependencies:
* pip install -r requirements.txt
2. Update the prompt_data variable in llama3.py with your desired prompt.
3. Run the script:
* python llama3.py
4. View the AI-generated output in the console.
