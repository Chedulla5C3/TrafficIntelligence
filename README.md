# 🚦 Traffic Volume Prediction

This project uses machine learning to predict traffic volume based on weather, time, and holiday data.
It includes a trained ML model, a Flask web application for predictions, and clear setup instructions.

## 📁 Project Structure
TrafficIntelligence/ │ ├── static/             
# (Optional) Static assets like CSS/images ├── templates/ │   └── index.html          
# HTML frontend for user input ├── app.py                  
# Flask application file ├── requirements.txt       
# Python dependencies ├── README.md                
# Project description and setup ├── .gitignore            
# Files excluded from Git └── 📦 model files (see below)

---

## 📦 Model Files

The trained model and encoders are *not included in this repository* due to size limits.

Download them from Google Drive and place in the project folder:

| File | Link |
|------|------|
| model.pkl | [Download](https://drive.google.com/your_model_link_here) |
| encoder.pkl | [Download](https://drive.google.com/file/d/1U9guMU86cxuViy1ZYQYWpRu3xO3r4VDX/view?usp=drive_link)
| scaler.pkl | [Download](https://drive.google.com/file/d/1fAcvHsQsVIOIvhqnszLy1S7Cu9GJKmuf/view?usp=drive_link)

> After downloading, place these in the *root folder* (same place as app.py).

---

## ⚙️ Installation

1. *Clone the repository*  
```bash
git clone https://github.com/YourUsername/TrafficIntelligence.git
cd TrafficIntelligence

2. Install dependencies
pip install -r requirements.txt

3. Add downloaded .pkl files (see links above)
---
🚀 Running the App
Start the Flask app locally:

python app.py

Then open your browser and go to:
http://127.0.0.1:5000

---

❗ Notes
.pkl files are ignored using .gitignore and not tracked by Git.
Git LFS was removed to avoid large file uploads.
Model must be downloaded manually before use.
---

🙋‍♀️ Author
Made by Chedulla Meghana
Contact: m17531746@gmail.com

