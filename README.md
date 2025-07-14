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

#  Windows
python -m venv venv
venv\Scripts\activate

#  macOS/Linux
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

### for fast api
cd app
pip install scikit-learn    # If required
pip install scikit-learn==1.6.1   # If required
uvicorn app:app --reload

### streamlit   open new terminal and not close old terminal

cd insureML  # skip if already there

#  Windows
venv\Scripts\activate

#  macOS/Linux
source venv/bin/activate

# Move to frontend and run
cd streamlit_app
pip install scikit-learn==1.6.1   # Optional if already installed
streamlit run frontend.py


### 🐳 Docker Deployment 

### 🛠️ Build Docker Image Locally


 docker build -t insure-ml-app .
▶️ Run the Docker Container
docker run -p 8000:8000 -p 8501:8501 insure-ml-app


- FastAPI (Backend): http://localhost:8000  
- Streamlit (Frontend): http://localhost:8501

### 📥 Pull from Docker Hub


docker pull ravikum/insure-ml-app:v1
docker run -p 8000:8000 -p 8501:8501 ravikum/insure-ml-app:v1



📤 Push to Docker Hub
docker tag crop-prediction-app ravikum/insure-ml-app:v1
docker push ravikum/insure-ml-app:v1

##**Docker Hub Repo:** 
https://hub.docker.com/repositories/ravikum


### ⚙️ Notes

- Make sure Docker is installed and running.
-
- Access FastAPI and Streamlit on ports **8000** and **8501** respectively.
