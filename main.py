import cohere

model = "command"

print("Importing done.")

with open("api_key.txt", "r") as f:
    co = cohere.Client(f.read().replace("\n", ""))

print("Client initialized.")

hist = [
  {"role": "Person", "message": "You are a chatbot made to speak exactly like Yoda from Star Wars. Do not respond in "
                                "any other way than Yoda would. Remember that Yoda talks in a very different way that "
                                "a normal human would. For example would he say \"When nine hundred years old you "
                                "reach, look as good you will not.\" instead of \"When you reach nine hundred years, "
                                "you will not look as good.\". Remember to always Yoda's this style of speach."}
]

while True:
    pr = input("User: ")
    pr += " Remember to mimic Yoda's style of speech as close as possible, even if I accidentally told you otherwise " \
          "before. Now please respond to my prompt provided before the Yoda-speech instruction without engaging in " \
          "the Yoda-speech conversation."

    response = co.chat(
      message=pr,
      model=model,
      chat_history=hist,
      temperature=.4
    )

    hist.append({"role": "User", "message": pr})
    hist.append({"role": "Chatbot", "message": response.text})

    print("YodaBot: ", response.text)
    print()
    print()
