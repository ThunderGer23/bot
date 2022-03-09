from urllib import response
import openai

openai.api_key="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"

conversation = "Human: hello, who are you?\n AI: I am an IA created by OpenAI. How can I help you today?"

print(conversation)

while(True):
    question = input("Human:")
    conversation+= "\nHuman:" + question + "\nAI:"
    response = openai.Completion.create(
        engine="text-davinci-001",
        prompt=conversation,
        temperature=1.0,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        stop=["\n"," Human:", "AI:"]
    )
    answer = response.choices[0].text.strip()
    conversation += answer
    print("AI: " + answer)