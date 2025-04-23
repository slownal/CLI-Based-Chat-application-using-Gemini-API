# CLI Chat Application with Gemini AI

A command-line interface chat application powered by Google's Gemini AI. This application enables natural conversational interactions with the Gemini language model, collects user feedback, and saves chat history.

## Features

- Interactive CLI-based chat with Gemini AI
- Smart exit detection - the chatbot recognizes when you want to end the conversation
- Feedback collection using Gemini's Function Calling API
- Saving user reviews and ratings to a feedback file
- Chat history logging (optional feature)
- Rich text formatting for better readability

## Requirements

- Python 3.7+
- Google Gemini API key
- Required Python packages:
  - google-generativeai
  - rich

## Setup Instructions

### 1. Install Required Libraries

```bash
pip install google-generativeai rich
```

### 2. Get a Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the API key for use in the next step

### 3. Set Up Your API Key

Set the API key as an environment variable:

For Windows (Command Prompt):
```
set GEMINI_API_KEY=your_api_key_here
```

For Windows (PowerShell):
```
$env:GEMINI_API_KEY="your_api_key_here"
```

For macOS/Linux:
```
export GEMINI_API_KEY=your_api_key_here
```

## Running the Application

1. Navigate to the directory containing the script
2. Run the script:

```bash
python cli_chat.py
```

3. Start chatting with the AI
4. To exit, type phrases like "bye", "exit", "end chat", or similar
5. When exiting, you'll be prompted for feedback and a rating

## Example Chat Session

```
Welcome to Gemini Chat CLI!
Type your messages and press Enter. Type 'exit', 'bye', or similar to end the chat.
--------------------------------------------------

[You]: Hello, how are you today?

[AI]: 
I'm doing well, thank you for asking! As an AI, I don't experience emotions, but I'm functioning properly and ready to assist you with information, answer questions, or just chat. How are you doing today?

[You]: Can you explain what quantum computing is?

[AI]:
Quantum computing is a type of computing that uses quantum phenomena like superposition and entanglement to perform calculations.

In classical computing, information is processed in bits (0s and 1s). In quantum computing, we use quantum bits or "qubits" that can exist in multiple states simultaneously thanks to superposition.

Key concepts:
- Superposition: Qubits can be in multiple states at once
- Entanglement: Qubits can be connected so that the state of one instantly affects another
- Quantum interference: Used to manipulate probabilities to increase correct answers

This allows quantum computers to solve certain problems much faster than classical computers, especially in areas like cryptography, optimization, simulation of quantum systems, and certain types of search algorithms.

While still largely experimental, companies like IBM, Google, and Microsoft are making significant advances in quantum computing hardware and software.

[You]: Thanks, that was helpful. Goodbye!

[AI]: I see you want to end our conversation.
Before you go, could you please provide a brief review and rating (1-5) of your experience?

[You]: I really enjoyed our conversation. The explanations were clear and helpful. 5 stars!

Thank you for your feedback! Your rating of 5/5 and review have been saved.
Thank you for chatting! Goodbye!
```

## Files

- `cli_chat.py` - The main Python script for the chat application
- `feedback.txt` - Contains saved user reviews and ratings (auto-generated on first feedback)
- `chat_history.txt` - Records all conversations (auto-generated, optional feature)

## Notes

- The application handles errors gracefully and continues the conversation
- Feedback is validated to ensure ratings are between 1-5
- Rich text formatting enhances the chat experience with colors and styles 