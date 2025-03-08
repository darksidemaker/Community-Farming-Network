import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
load_dotenv()


def create_client():
    return genai.Client(api_key=os.environ.get("GEMINI_API_KEY"),) 

def create_generate_content_config():
    return types.GenerateContentConfig(
        temperature=1,
        top_p=0.95,
        top_k=64,
        max_output_tokens=8192,
        safety_settings=[
            types.SafetySetting(
                category="HARM_CATEGORY_HARASSMENT",
                threshold="BLOCK_LOW_AND_ABOVE",  # Block most
            ),
            types.SafetySetting(
                category="HARM_CATEGORY_HATE_SPEECH",
                threshold="BLOCK_LOW_AND_ABOVE",  # Block most
            ),
            types.SafetySetting(
                category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
                threshold="BLOCK_LOW_AND_ABOVE",  # Block most
            ),
            types.SafetySetting(
                category="HARM_CATEGORY_DANGEROUS_CONTENT",
                threshold="BLOCK_LOW_AND_ABOVE",  # Block most
            ),
            types.SafetySetting(
                category="HARM_CATEGORY_CIVIC_INTEGRITY",
                threshold="BLOCK_LOW_AND_ABOVE",  # Block most
            ),
        ],
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text="""you are an expert at farming """),
        ],
    )

def append_user_input(contents, user_input):
    contents.append(
            types.Content(
                role="user",
                parts=[
                    types.Part.from_text(text=user_input),
                ],
            )
        )
    
def append_model_output(contents, chunk):
    contents.append(
            types.Content(
                role="model",
                parts=[
                    types.Part.from_text(text=chunk),
                ],
            )
        )
    
def generate_response(client,model,contents,config):
    response_text = ""
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=config,
    ):
        response_text += chunk.text
    return response_text

def generate():

    client = create_client()
    model = "gemini-2.0-pro-exp-02-05"
    contents = []
    generate_content_config = create_generate_content_config()

    while True: 
        user_input = input("You: ")
        if user_input.lower == "exit":
            break
        append_user_input(contents, user_input)

        response_text = generate_response(client,model,contents,generate_content_config)
        print("Model: ", response_text)
        append_model_output(contents,response_text)


if __name__ == "__main__":
    generate()