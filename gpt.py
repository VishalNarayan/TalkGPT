import os
import openai

from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("SECRET_KEY")

def completion(prompt):

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=25,
        temperature=1)

    return response



