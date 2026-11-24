# Project Documentation: Cybersecurity Study Assistant

## Project overview
I developed this Python command-line application to make it easier to review cybersecurity concepts. A user enters a question, and the program sends it to an AI model and displays the response.

## My development work
I defined the purpose and basic workflow, organized the Python program, configured the request to the AI service, and added input handling and error messages. I used an AI tool as a development aid to help plan the program, review implementation choices, and improve error handling. I reviewed the resulting code and documentation and remain responsible for understanding, testing, and maintaining the project.

## Technologies
- Python
- OpenAI Chat Completions API
- Python standard library: `urllib`, `json`, and `os`

## How the program works
1. The user starts the Python program.
2. The program prompts for a cybersecurity question.
3. It reads the API key from the `OPENAI_API_KEY` environment variable.
4. It sends the question with instructions to provide a clear, safety-conscious educational answer.
5. It displays the response and waits for another question.

## Security considerations
The API key is not hard-coded or stored in the repository. It should remain private. The assistant is intended for learning and authorized lab environments. Responses should be checked for accuracy before being relied on.

## Testing checklist
- Run without an API key and confirm that a helpful error appears.
- Run with a valid API key and ask a basic cybersecurity question.
- Test an empty question and the `exit` command.
- Check how the program responds to a network or API error.

## Current limitations
The program requires internet access and an active API key. API usage may incur charges depending on the account. Complete the tests above before describing the application as fully tested.
