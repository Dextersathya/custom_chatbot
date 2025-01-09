# Conversational AI with LangChain and Ollama

This project demonstrates a conversational AI application using the **LangChain** framework and the **OllamaLLM** model (`gemma2:2b`). It allows users to interact with the AI in a conversational manner while maintaining context from previous exchanges.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Future Enhancements](#future-enhancements)

---

## Overview

The application leverages:
- **LangChain**: For chaining prompts and models together.
- **OllamaLLM**: A lightweight and efficient language model (`gemma2:2b`) for generating conversational responses.
- **Streaming Responses**: Real-time streaming of AI responses for a better user experience.

---

## Features

- **Conversational Context**: Keeps track of the conversation history for coherent and contextual replies.
- **Real-Time Interaction**: Responses are streamed in real time for a dynamic user experience.
- **Easy to Use**: Simple Python script to run and interact with.

---

## Setup

### Prerequisites

1. Python 3.8 or higher.
2. Install the required libraries:
   ```bash
   pip install langchain-core langchain-ollama
   ```

### Clone the Repository
```bash
git clone https://github.com/your-repo/conversational-ai.git
cd conversational-ai
```

---

## Usage

1. Run the script:
   ```bash
   python main.py
   ```

2. Start interacting with the AI. Type your queries, and the AI will respond. Type `exit` to quit the conversation.

---

## Code Explanation

### Template
The conversation prompt template ensures that the AI has access to the conversation history (`context`) and the current question (`question`):
```python
template = """
Answer the question below.

Here is the conversation history: {context}
Question: {question}

Answer:
"""
```

### Core Components
1. **OllamaLLM**: The `gemma2:2b` model is used for generating responses.
2. **LangChain Prompt**: Combines the template and the model to process user queries.
3. **Streaming**: Real-time streaming of responses for a seamless experience.

### Conversation Handler
The `handle_conversation()` function manages the interaction:
- Maintains the conversation history.
- Streams responses as they are generated.

---

## Future Enhancements

- Add support for multiple LLMs and dynamic model selection.
- Integrate a web or desktop interface for user interaction.
- Save and load conversation history for continuity across sessions.
- Implement sentiment analysis for better context understanding.

---

Feel free to contribute to this project or raise issues for further improvements!

---
