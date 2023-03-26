import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

asistant = {"role": "system", "content": "Make message more exciting."}

msgs = [asistant]

while True:
    user = {"role": "user", "content": input("You: ")}
    msgs.append(user)
    # msgs.remove(asistant)
    # msgs.append(asistant) # Just tried a case
    print(f"Current messages: {msgs}")
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=list(msgs)
    )

    print(completion.choices[0].message.content)