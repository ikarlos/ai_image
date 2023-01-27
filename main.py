import os
import openai
openApi_key = os.getenv("OPENAI_API_KEY")
PROMPT = "a happy face"

openai.api_key = openApi_key
response = openai.Image.create(

    prompt=PROMPT,

    n=1,

    size="256x256",

)


print(response["data"][0]["url"])
