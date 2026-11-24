# Cybersecurity Study Assistant

A Python command-line tool for reviewing cybersecurity topics. Enter a question and the program requests an explanation from an AI model.

## Requirements
- Python 3.9+
- An OpenAI API key and API access

## Run
Windows PowerShell:
```powershell
$env:OPENAI_API_KEY="your_api_key_here"
python app.py
```

macOS/Linux:
```bash
export OPENAI_API_KEY="your_api_key_here"
python3 app.py
```

The program reads the API key from an environment variable. Do not put the key in the source code or commit it to GitHub.

## Example questions
- What is the principle of least privilege?
- Explain the difference between authentication and authorization.
- What does a Linux file permission such as 755 mean?

## Intended use
Use the assistant for study and authorized lab learning. AI responses can be inaccurate, so verify important information with course materials and trusted technical references.
