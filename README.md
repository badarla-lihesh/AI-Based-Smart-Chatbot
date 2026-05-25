# AI-Based Smart Chatbot

AI-Based Smart Chatbot is a simple web-based chatbot application built using Python and Flask. It allows users to interact through a web interface and receive responses based on keyword matching logic. The project demonstrates basic chatbot development using rule-based NLP concepts along with frontend and backend integration.

## Features
- Simple and interactive chat interface  
- Keyword-based response system  
- Flask backend integration  
- Frontend built using HTML, CSS, and JavaScript  
- JSON-based intent storage  
- Lightweight and easy to run locally  

## Technologies Used
Python, Flask, HTML, CSS, JavaScript, JSON  

## Project Structure
AI-Based-Smart-Chatbot/  
├── app.py  
├── intents.json  
├── templates/  
│   └── index.html  
├── static/  
│   ├── style.css  
│   └── script.js  
└── README.md  

## How to Run
1. Install Flask: pip install flask  
2. Run the project locally: python app.py  
3. Open in browser: http://127.0.0.1:5000

## Working
User enters a message → chatbot checks keywords from intents.json → selects matching response → displays reply in chat interface.

## About Project
This project was developed to understand how a chatbot works using Python, Flask, and basic rule-based logic. It focuses on frontend and backend integration and simple conversational flow.