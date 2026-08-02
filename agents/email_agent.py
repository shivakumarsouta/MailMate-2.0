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

MODEL_NAME = "meta-llama/llama-3.1-8b-instruct"


def clean_output(text: str) -> str:
    """Clean unwanted model artifacts like <s>, [INST], etc."""
    if not text:
        return text
    text = re.sub(r"<s>|</s>|\\[/?B_INST\\]|\\[/?INST\\]|\\[\\/?s\\]", "", text)
    return text.strip()


def _chat(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt.strip()}],
            temperature=0.3,
        )
        content = response.choices[0].message.content
        return clean_output(content)
    except Exception as e:
        print(f"API Error: {e}")
        return "Error: Unable to process request due to an AI service issue. Please try again."


def summarize_email(email_text: str) -> str:
    if len(email_text.strip()) < 10:
        return "The provided text is too short or invalid to be a meaningful email. Please enter a proper email body."

    prompt = f"""
Analyze the email below and output ONLY 3 to 5 bullet points summarizing it. 
Strict formatting rule: Do NOT write any introduction, conversational filler, or preamble sentences. Start your response immediately with the first bullet point character (-).

Email:
\"\"\"{email_text}\"\""""
    return _chat(prompt)


def generate_subject_line(email_text: str, tone: str) -> str:
    if len(email_text.strip()) < 10:
        return "Response to inquiry"

    prompt = f"""
Generate a professional email reply subject line for the email provided below. 
It should look like a proper email thread reply (e.g. starting with "Re: " followed by the context of the original email).
Tone: {tone.lower()}
Return only the subject line text. No quotes, no labels.

Email:
\"\"\"{email_text}\"\""""
    return _chat(prompt)


def generate_email_response(email_text: str, tone: str, length: str = "Medium") -> str:
    if len(email_text.strip()) < 10:
        return "Hello,\n\nThank you for your message. Could you please provide more details so I can properly address your request?\n\nBest regards,\n[Your Name]"

    length_style = {
        "Short": "3–5 concise sentences.",
        "Medium": "1–2 short paragraphs.",
        "Long": "Up to 3–5 paragraphs with polite detail.",
    }.get(length, "1–2 paragraphs.")

    prompt = f"""
You are acting as an email reply assistant for the owner of this app. 
Analyze the incoming email provided below. The incoming email was sent TO the user by someone else. 
Your task is to write a reply FROM the user BACK TO the sender of this email. 
- Do NOT write the reply addressed to the user's own name. 
- Address the reply to the sender/organization that sent the incoming email.
- Write from the perspective of the person receiving the email replying back.

Tone: {tone.lower()}
Length: {length_style}

Strict formatting rule: Do NOT write any conversational filler, explanations, notes, or intro text. Output ONLY the raw email body text starting directly with a professional greeting directed at the original sender.

Incoming Email to reply to:
\"\"\"{email_text}\"\""""
    return _chat(prompt)