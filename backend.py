import openai
import os


class Chatbot:
    def __init__(self):
        openai.api_key = "sk-None-xsRejmXEA5B1AR85dGsWT3BlbkFJvUi7YZ3dfhc65bLOuReT"

    def get_response(self, user_input):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.2
        ).choices[0].text
        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("write something")
    print(response)


