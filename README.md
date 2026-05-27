# AI-Based Smart Chatbot

## About
AI-Based Smart Chatbot is a web-based chatbot application built using Python and Flask. It uses a rule-based keyword matching system to understand user input and respond with appropriate replies. The project demonstrates full-stack development using Flask for backend and HTML, CSS, JavaScript for frontend integration.

---

## Technologies Used

Frontend:
- HTML
- CSS
- JavaScript

Backend:
- Python
- Flask

---

## Libraries Used
- Flask
- JSON (for intent data handling)
- Random (for selecting responses)

---

## Project Structure
AI-Based-Smart-Chatbot/
├── app.py
├── intents.json
├── README.md
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
├── demo_images/
│   ├── home_page.png
│   ├── chat_input.png
│   └── chat_response.png

---

## How to Run

1. Install Flask:
   pip install flask

2. Run the application:
   python app.py

3. Open browser and use the application locally

---

## Working
User enters a message → chatbot reads keywords from intents.json → matches intent → selects response → displays output in chat interface.

---

## Screenshots

### Home Page
![Home Page](demo_images/home_page.png)

### Chat Input
![Chat Input](demo_images/chat_input.png)

### Bot Response
![Bot Response](demo_images/chat_response.png)

---

## Future Improvements
- Integrate AI/ML based NLP model
- Improve UI design with modern chat interface
- Add database for chat history storage
- Deploy application for public access
- Add voice-based interaction system

---

## Project Status
Currently running in local environment using Flask. Deployment is not included as the project is intended for local demonstration.

---

## Author
Badarla Lihesh