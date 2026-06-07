# WikiRAG

WikiRAG is a lightweight Retrieval-Augmented Generation (RAG) application that combines Wikipedia's knowledge base with Google's Gemini 2.5 Flash model.

## Features

* Search any topic using natural language questions
* Automatically identifies the most relevant Wikipedia article
* Retrieves article content from Wikipedia
* Generates context-aware answers using Gemini 2.5 Flash
* Interactive Streamlit web interface
* Displays source context used for answer generation

## Tech Stack

* Python
* Streamlit
* LangChain
* Google Gemini 2.5 Flash
* Wikipedia API

## How It Works

1. User enters a question.
2. Gemini determines the most relevant Wikipedia article.
3. The application retrieves content from Wikipedia.
4. Retrieved content is provided as context to Gemini.
5. Gemini generates an answer grounded in the retrieved information.

## Example Queries

* Who invented Cricket?
* What is Artificial Intelligence?
* Tell me about the Boeing 747
* Explain Quantum Computing

This project demonstrates the fundamentals of Retrieval-Augmented Generation (RAG) by combining external knowledge retrieval with LLM-powered answer generation.
