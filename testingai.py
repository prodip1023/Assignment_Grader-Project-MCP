import openai
import os

# Set your API key
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY", "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"))

# Test the chat completion
def test_openai():
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-4"
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Say hello world!"}
            ]
        )
        print("✅ OpenAI Response:", response.choices[0].message.content)
    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    test_openai()