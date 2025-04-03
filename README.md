# 🍺 BrewCompass - Your AI-Powered Beer Guide

BrewCompass is a smart conversational web app that helps users discover beers based on taste, mood, and characteristics. It leverages Dialogflow for natural language interaction, a FastAPI backend for data processing, and a custom-trained recommendation model to personalize suggestions.

---

## Features

- Conversational beer recommendations
- Voice output using Speech Synthesis API
- Dialogflow chatbot integration
- Machine learning-based clustering and recommendation
- Stylish beer-themed frontend
- Responsive design

---

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript (Vite)
- **Backend**: Python, FastAPI
- **Machine Learning**: scikit-learn, xgboost
- **Chatbot**: Dialogflow ES
- **Deployment**: Netlify (Frontend), Ngrok (for local backend tunnel)

---

## Setup Instructions

### Frontend Setup (Vite Project)

1. **Install dependencies**
   ```bash
   npm install
   ```

2. **Run in development mode**
   ```bash
   npm run dev
   ```
   > Visit: http://localhost:5173

3. **Build for production**
   ```bash
   npm run build
   ```

4. **Preview production build**
   ```bash
   npm run preview
   ```

---

### 🔧 Backend Setup (FastAPI)

1. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the backend server**
   ```bash
   uvicorn main:app --reload
   ```

3. **Start ngrok**
   > Download from https://ngrok.com and start a tunnel:
   ```bash
   ngrok http http://localhost:8000
   ```

4. **Copy the ngrok URL** and paste it into **Dialogflow → Fulfillment → Webhook URL**

---

###  Dialogflow Setup

- Use the backup `BeerChatBot.zip` to import the agent in Dialogflow
- Ensure your webhook is enabled and linked to the ngrok tunnel
- Test the chatbot from the Dialogflow interface

---

### Machine Learning

- Clustering model and recommendation logic are built on a curated beer dataset
- XGBoost and KMeans used for personalized suggestions
- Dataset and training scripts are included in the backend repo

---

### 🌐 Deployment

- Frontend is deployed on **Netlify** at:
  > [https://brewcompass.netlify.app](https://brewcompass.netlify.app)
- Backend runs locally with Ngrok tunnel exposed to Dialogflow

---

## Dataset

- Custom beer dataset used to build recommendation models.
- Available in `backend/data/beer-dataset.csv`

---

## 📎 Optional

- For improved accuracy, consider deploying the backend on a persistent cloud platform like **Render**, **Railway**, or **GCP** instead of using Ngrok.

---

## 📌 License

MIT License © 2024 BrewCompass Dev Team
