# 🕵️‍♀️ Indian Crime Domain Predictor

This project is a simple yet powerful AI/ML web app that predicts the **crime domain** (e.g., Violent Crime, Other Crime, Traffic Fatality, etc.) based on a short crime description. Built using **Python**, **Scikit-learn**, and **Streamlit**.

---

## 📌 Project Overview

🚨 Input: A crime description (e.g., *"Man caught with illegal firearm"*)  
🎯 Output: Predicted crime domain (e.g., *Other Crime*)

---

## 💡 Features

- 🔎 Predicts crime domain from description
- 💻 Clean, interactive Streamlit web app
- 🧠 Trained ML model using Logistic Regression
- 📊 Works with real Indian crime dataset (Kaggle)

---

## 🛠️ Tech Stack

- Python
- Pandas, Scikit-learn
- Streamlit (for web UI)
- Jupyter Notebook / VS Code

---

## 📁 Files

| File                | Description                               |
|---------------------|-------------------------------------------|
| `app.py`            | Streamlit UI for the web app              |
| `train_model.py`    | Script to train the ML model              |
| `model.pkl`         | Trained Logistic Regression model         |
| `india_crime_small.csv` | Cleaned & sampled dataset from Kaggle |
| `README.md`         | You're reading it!                        |

---

## ⚙️ How to Run the App

```bash
# 1. Clone the repository
git clone https://github.com/Akshatakokane10/Crime_Predictor_India.git

# 2. Move into the folder
cd Crime_Predictor_India

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Streamlit app
streamlit run app.py


📦 Dependencies
Create a requirements.txt file with:

streamlit
scikit-learn
pandas
joblib

Install all with:
pip install -r requirements.txt


✨ Sample Predictions
Crime Description                           	Predicted Domain
Man caught with illegal firearm	                Other Crime
Child kidnapped from school	                    Other Crime
Cyber fraud using fake OTP messages	            Other Crime
Shoplifting in retail mall	                    Other Crime
Blunt object attack during robbery	           Violent Crime
FireArm Offence                                Fire Accident


🙋‍♀️ Author
Akshata Kokane
📬 GitHub: @Akshatakokane10
🧠 AI/ML Enthusiast | B.E. Information Technology


## 🖼️ Screenshots

### 🔹 Violent Crime Example
![Violent Crime](https://github.com/Akshatakokane10/Crime_Predictor_India/blob/7c34edce3771fe47e61d3d9c5e9c5b97c16f2741/screenshots/violent_crime.png)

### 🔸 Traffic Violation Example
![Traffic Violation](https://github.com/Akshatakokane10/Crime_Predictor_India/blob/7c34edce3771fe47e61d3d9c5e9c5b97c16f2741/screenshots/traffic_violation.png)

### 🔥 Fire Accident Prediction
![Fire Accident](https://github.com/Akshatakokane10/Crime_Predictor_India/blob/7c34edce3771fe47e61d3d9c5e9c5b97c16f2741/screenshots/fire_accident.png)

### 🔹 Another Violent Crime Example
![Violent Crime 2](https://github.com/Akshatakokane10/Crime_Predictor_India/blob/7c34edce3771fe47e61d3d9c5e9c5b97c16f2741/screenshots/violent_crime2.png)

