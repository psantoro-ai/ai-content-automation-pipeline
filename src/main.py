from generator import generate_content
from prompts import marketing_post_prompt
import os

def save_output(content: str, filename: str):
    os.makedirs("outputs", exist_ok=True)
    
    with open(f"outputs/{filename}.txt", "w", encoding="utf-8") as f:
        f.write(content)

def run():
    topic = input("Enter content topic: ")

    # 👉 MODO DEMO (sem API)
    if not os.getenv("OPENAI_API_KEY"):
        print("\n⚠️ Running in DEMO mode (no API key)\n")

        content = """Headline: AI is transforming marketing

Copy:
Automated content can scale your business efficiently and improve results.

CTA:
Start using AI today and stay ahead of the competition.
"""
        print(content)
        save_output(content, "demo_output")
        return

    # 👉 MODO REAL
    prompt = marketing_post_prompt(topic)
    content = generate_content(prompt)

    print("\n=== GENERATED CONTENT ===\n")
    print(content)

    save_output(content, topic.replace(" ", "_"))

if __name__ == "__main__":
    run()
