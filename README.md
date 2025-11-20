# 📫 MailMate 2.0 — AI-Powered Email Assistant

MailMate 2.0 is an upgraded and smarter version of the original MailMate application — designed to help users read, analyze, and generate email replies faster with the help of AI.

With automatic summarization, tone selection, length control, and editable AI-powered responses, MailMate 2.0 makes professional email communication faster, consistent, and hassle-free.

---

You can view the app live at [MailMate-2.0](https://mailmate-2.0.streamlit.app)

---

## 🚀 Features

| Feature                         | Description                                                                |
| ------------------------------- | -------------------------------------------------------------------------- |
| ✨ AI Email Reply Generation     | Automatically generates a reply based on the content of the received email |
| 🎯 Tone Customization           | Choose between: Professional, Friendly, Apologetic, Persuasive             |
| 📏 Adjustable Length            | Generate Short, Medium, or Long responses                                  |
| 📌 Email Summarization          | Summarizes the incoming email into clear key points                        |
| 🧠 Smart Subject Line Generator | Automatically generates a relevant subject line                            |
| 📝 Editable Drafts              | Fully editable reply before sending                                        |
| 📧 Built-in Email Sender        | Send replies directly through SMTP                                         |
| 🔄 Stateful UI                  | Keeps email data and generated responses until cleared                     |

---

## 🛠️ Tech Stack

* **Python 3.10+**
* **Streamlit** — Frontend UI
* **OpenRouter API** — AI text generation
* **SMTP** — Email delivery
* **dotenv** — Environment variable management

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/shivakumarsouta/MailMate-2.0.git
cd MailMate-2.0
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add:

```env
OPENROUTER_API_KEY=your_openrouter_key
SENDER_EMAIL=your_email@example.com
EMAIL_PASSWORD=your_email_app_password
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

💡 If using Gmail, ensure **App Passwords** are enabled.

---

## ▶️ Run the App

```bash
streamlit run app.py
```

The app will open in your browser.

---

## 🧪 Known Improvements (Future Enhancements)
* 🎨 Custom theme and dark mode

---

## 🧩 Folder Structure

```
MailMate-2.0/
│
├── app.py                 # Main Streamlit application
├── agents/
│   └── email_agent.py     # AI handling logic
│
├── utils/
│   └── email_sender.py    # SMTP email handler
│
├── requirements.txt       # Dependencies
├── .env                    # Environment configuration (not included in repo)
└── README.md              # Documentation
```

---

## 📄 License

This project is released under the **MIT License** — free for personal and educational use.

---

## 🤝 Contributions Welcome

* Found a bug? Open an issue.
* Want to add more tones or language support? PRs are welcome!
* Want to switch models? Support for Claude, Mistral, or Llama can be added easily via OpenRouter.

---

### ⭐ If you like MailMate 2.0, consider giving it a star on GitHub!

---

## ✨ Credits

Built with:

* [Streamlit](https://streamlit.io/)
* [OpenRouter.ai](https://openrouter.ai/)
* [SMTP via Gmail](https://support.google.com/mail/answer/7126229)

---

## 📫 Connect

* [Email](shivakumarsouta18@gmail.com)
* [LinkedIn](https://www.linkedin.com/in/shivakumarsouta/)


