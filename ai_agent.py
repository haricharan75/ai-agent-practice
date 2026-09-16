# ai_agent.py
import os
import anthropic
from dotenv import load_dotenv

# This loads the variables from .env into your environment
load_dotenv() 

def run_ai_review(file_path):
    print(f"🤖 Claude Agent reviewing: {file_path}")
    
    # 1. Read the original code
    with open(file_path, "r") as f:
        original_code = f.read()

    # 2. Connect to Claude (automatically reads ANTHROPIC_API_KEY)
    client = anthropic.Anthropic()

    prompt = f"""
You are a security code reviewer. 
Review the following Python code and fix any unsafe or insecure patterns (e.g., eval, command injection).
Return ONLY the raw, executable Python code with the fix applied. 
Do not wrap it in markdown backticks (```) or add explanations.

Code:
{original_code}
"""

    # 3. Call Claude
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]
    )

    fixed_code = response.content[0].text.strip()

    # Clean any accidental markdown formatting
    if fixed_code.startswith("```python"):
        fixed_code = fixed_code[len("```python"):].strip()
    if fixed_code.endswith("```"):
        fixed_code = fixed_code[:-3].strip()

    # 4. If Claude changed the code, write it back to the file
    if fixed_code != original_code.strip():
        with open(file_path, "w") as f:
            f.write(fixed_code + "\n")
        print("✅ Claude found improvements and updated the file!")
    else:
        print("✅ Code was already safe. No changes needed.")

# 5. THIS is the trigger that actually runs the function above
if __name__ == "__main__":
    run_ai_review("calculator.py")