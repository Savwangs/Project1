from openai import OpenAI

class LLM:
    def __init__(self, api_key, model="gpt-4o-mini"):
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def get_response(self, conversation):
        """Get a response from OpenAI based on the conversation history."""
        messages = [{"role": "system", "content": "You are a helpful assistant."}]
        
        for role, content in conversation:
            messages.append({"role": role, "content": content})

        try:
            completion = self.client.chat.completions.create(
            model=self.model,
            messages=messages
            )
            return completion.choices[0].message.content
        except APIConnectionError as e:
            logging.error(f"API Connection Error: {e}")
            st.error("Failed to connect to OpenAI API. Please try again later.")
            return "Error connecting to the OpenAI API."
