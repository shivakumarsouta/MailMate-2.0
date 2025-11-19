import os
import re
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    raise RuntimeError("OPENROUTER_API_KEY is missing. Add it to your .env")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
    default_headers={
        "HTTP-Referer": "https://mailmate.app",
        "X-Title": "MailMate 2.0",
    },
)

MODEL_NAME = "mistralai/mistral-7b-instruct:free"


def clean_output(text: str) -> str:
    """Clean unwanted model artifacts like <s>, [INST], etc."""
    if not text:
        return text
    text = re.sub(r"<s>|</s>|\\[/?B_INST\\]|\\[/?INST\\]|\\[\\/?s\\]", "", text)
    return text.strip()


def _chat(prompt: str) -> str:
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt.strip()}],
        temperature=0.7,
    )
    return clean_output(response.choices[0].message.content)


def summarize_email(email_text: str) -> str:
    prompt = f"""
Summarize the following email in 3–5 bullet points.
Focus on purpose, key details, sender requests, and response expectations.

Email:
\"\"\"{email_text}\"\"\"
"""
    return _chat(prompt)


def generate_subject_line(email_text: str, tone: str) -> str:
    prompt = f"""
Generate a short subject line for replying to this email.
Tone: {tone.lower()}
Return only the subject line.

Email:
\"\"\"{email_text}\"\"\"
"""
    return _chat(prompt)


def generate_email_response(email_text: str, tone: str, length: str = "Medium") -> str:
    length_style = {
        "Short": "3–5 concise sentences.",
        "Medium": "1–2 short paragraphs.",
        "Long": "Up to 3–5 paragraphs with polite detail.",
    }.get(length, "1–2 paragraphs.")

    prompt = f"""
Write an email reply.

Tone: {tone.lower()}
Length: {length_style}
Be polite, professional and avoid unnecessary details.

Email to reply:
\"\"\"{email_text}\"\"\"

Draft reply:
"""
    return _chat(prompt)
