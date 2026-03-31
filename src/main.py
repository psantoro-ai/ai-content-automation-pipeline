from generator import generate_content
from prompts import marketing_post_prompt
import os

def save_output(content: str, filename: str):
    os.makedirs("outputs", exist_ok=True)
    
    with open(f"outputs/{filename}.txt", "w", encoding="utf-8") as f:
        f.write(content)

def run():
    topic = input("Enter content topic: ")

    prompt = marketing_post_prompt(topic)
    content = generate_content(prompt)

    print("\n=== GENERATED CONTENT ===\n")
    print(content)

    save_output(content, topic.replace(" ", "_"))

if __name__ == "__main__":
    run()
