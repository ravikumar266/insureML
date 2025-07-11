# insureML
insurance-risk-analyzer
A full-stack machine learning application to predict the **insurance premium category** (Low, Medium, High) based on user data such as age, BMI, income, city, and lifestyle.  
This project uses **FastAPI** for the backend and **Streamlit** for the frontend interface.

---

## 🚀 Features

- 🚦 Predicts insurance premium category (Low / Medium / High)
- 🧠 Machine learning model trained and saved using `model.pkl`
- 🔌 FastAPI REST API for prediction endpoint
- 🌐 Streamlit frontend to collect user input
- 📄 PDF report generation of the project

---

## 🗂️ Project Structure


---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/ravikumar266/insureML.git
cd insureML


python -m venv venv
venv\Scripts\activate  # For Windows
pip install -r requirements.txt

cd app
uvicorn app:app --reload

## open new terminal but not delete the previous terminal

cd streamlit_app
pip install scikit-learn==1.6.1

streamlit run frontend.py


