# 📊 Sentiment Analysis Web App

## 🚀 Live Demo
🔗 [Click here to try the app](https://sentiment-analysis-colab-cvhv5dwvf7oxm9pxu7v74j.streamlit.app/)

---

## 📌 Project Overview

### About the Project

This project is a **Sentiment Analysis Web Application** that analyzes user-provided text and classifies it as **Positive**, **Negative**, or **Neutral** using **Natural Language Processing (NLP)** techniques.

The application provides a simple and interactive **Graphical User Interface (GUI)** where users can enter text and instantly view sentiment results.

The project is fully **cloud-deployed using Streamlit Cloud**, making it accessible through a public URL.

---

## ✨ Features

### Key Highlights

- 🔍 Classifies text sentiment as **Positive / Negative / Neutral**
- 🧠 Uses NLP techniques to calculate sentiment polarity
- 🖥️ Simple and user-friendly web interface
- 🌐 Deployed as a live web application
- 📈 Cloud-ready and easily extendable (AWS Lambda, S3)

---

## 🛠️ Technologies Used

### Tech Stack

- **Python**
- **TextBlob** – Natural Language Processing
- **Streamlit** – Web Interface & Deployment
- **Google Colab** – Model development and testing
- **GitHub** – Version control and hosting

---

## 🧩 How It Works

### Workflow

1. User enters text in the input box.
2. The text is processed using NLP techniques.
3. Sentiment polarity is calculated.
4. Based on the polarity value:
   - Positive polarity → **Positive Sentiment**
   - Negative polarity → **Negative Sentiment**
   - Zero polarity → **Neutral Sentiment**
5. The result is displayed instantly on the web interface.

---

## 🖥️ Application Interface

### User Interaction

The web application includes:
- A text input area for user input
- An **Analyze** button
- Instant sentiment result display

---

## 📸 Screenshots

Screenshots of the application interface and sample sentiment analysis outputs are included in this repository to demonstrate the functionality and user experience.

---

## 📂 Project Structure

### Repository Layout

Sentiment-Analysis/
│
├── gui/
│   └── app.py
│
├── requirements.txt
├── README.md


---

## ▶️ Run Locally (Optional)

### Local Setup Instructions

To run this project on your local machine:
```bash
pip install streamlit textblob
python -m textblob.download_corpora
streamlit run gui/app.py
```

---

## ☁️ Deployment

### Cloud Deployment Details

- The application is deployed using **Streamlit Cloud**
- The app is connected directly to the **GitHub repository**
- All dependencies are automatically installed using **requirements.txt**

---

## 🔮 Future Improvements

### Planned Enhancements

- Add sentiment confidence score
- Improve UI with charts and visual indicators
- Store inputs and outputs using AWS S3
- Automate processing using AWS Lambda
- Support multiple languages

---

## 👩‍💻 Author

### Vibhuti Sharma

- **GitHub:** https://github.com/Vibhu-18
- **LinkedIn:** https://www.linkedin.com/in/vibhuti-sharma2006

