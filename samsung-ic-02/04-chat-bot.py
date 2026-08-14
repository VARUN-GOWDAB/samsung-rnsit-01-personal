# Import the Groq client
from groq import Groq

# Get the API key - copy and paste
api_key = r""

# Initialize the Groq client with the API key
client = Groq(api_key=api_key)

# Select a model and set up the request parameters
model = "llama-3.1-8b-instant"

# Define the chat function
def chat():

    # welcome message
    print("Welcome to the Groq Chat Bot! Type 'exit' to quit.")

    # setup conversation history
    messages = []

    # inifinite loop
    while True:

        # get the user message
        user_input = input("You: ")

        # check for the exit criterion
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # insert the user query into chat buffer
        messages.append({"role": "user", "content": user_input})

        try:

            # invoke the llm
            response = client.chat.completions.create(
                model=model,
                messages=messages
            )

            # extract the response message
            assistant_message = response.choices[0].message.content

            # print it for the user
            print(f"Bot: {assistant_message}")

            # add the response to chat buffer
            messages.append({"role": "assistant", "content": assistant_message})

        except Exception as e:

            # print exception message
            print(f"Error: {e}")

# invoke the chat function
if __name__ == "__main__":
    chat()
