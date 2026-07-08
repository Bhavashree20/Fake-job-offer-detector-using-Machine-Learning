# Fake Job Offer Detector Using Machine Learning

## Project Overview

The Fake Job Offer Detector is a Machine Learning-based web application developed to identify fraudulent job postings. The system analyzes job descriptions using Natural Language Processing (NLP) techniques and classifies them as either **Real** or **Fake**. This application helps job seekers avoid scams and improves the reliability of online recruitment platforms.

---

## Problem Statement

Many online job portals contain fake job advertisements that can lead to financial loss, identity theft, and misuse of personal information. This project aims to automatically detect fraudulent job postings using Machine Learning techniques.

---

## Project Objectives

- Detect fake job postings using Machine Learning.
- Analyze job descriptions using NLP techniques.
- Classify job postings as Real or Fake.
- Help job seekers identify trustworthy job opportunities.
- Improve the security of online recruitment platforms.

---

## Features

- User Login Authentication
- Fake Job Detection
- Real Job Detection
- Machine Learning-Based Prediction
- Simple and User-Friendly Interface
- Flask Web Application

---

## Modules

### Module 1: Data Collection
Collect and store datasets containing real and fake job postings.

### Module 2: Data Preprocessing
Clean the dataset, remove duplicates, handle missing values, and prepare data for analysis.

### Module 3: Feature Extraction
Convert textual job descriptions into numerical features using TF-IDF.

### Module 4: Model Training
Train the Machine Learning model using Logistic Regression.

### Module 5: Prediction
Predict whether a given job posting is Real or Fake.

### Module 6: Result Analysis
Display prediction results and evaluate model performance.

---

## Technology Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| Framework | Flask |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas, NumPy |
| NLP | TF-IDF |
| Frontend | HTML, CSS |
| Version Control | Git & GitHub |

---

## Database Design

### Table 1: User

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| user_id | INT (PK) | Unique User ID |
| name | VARCHAR(100) | User Name |
| email | VARCHAR(100) | User Email |
| password | VARCHAR(255) | User Password |
| role | VARCHAR(20) | Admin/User |

### Table 2: Job_Posting

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| job_id | INT (PK) | Unique Job ID |
| user_id | INT (FK) | User Reference |
| title | VARCHAR(200) | Job Title |
| company | VARCHAR(150) | Company Name |
| description | TEXT | Job Description |
| location | VARCHAR(100) | Job Location |
| salary_range | VARCHAR(50) | Salary Details |
| post_date | DATE | Posting Date |

### Table 3: Dataset

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| dataset_id | INT (PK) | Dataset ID |
| source | VARCHAR(100) | Dataset Source |
| description | TEXT | Dataset Description |
| records_count | INT | Number of Records |
| uploaded_date | DATE | Upload Date |

### Table 4: ML_Model

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| model_id | INT (PK) | Model ID |
| model_name | VARCHAR(100) | Model Name |
| algorithm | VARCHAR(100) | ML Algorithm |
| accuracy | FLOAT | Model Accuracy |
| training_date | DATE | Training Date |

### Table 5: Prediction

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| prediction_id | INT (PK) | Prediction ID |
| job_id | INT (FK) | Job Posting ID |
| model_id | INT (FK) | ML Model ID |
| result | VARCHAR(20) | Real/Fake |
| confidence_score | FLOAT | Prediction Confidence |
| prediction_date | DATE | Prediction Date |

---

## Database Relationships

- User → Job_Posting (1 : Many)
- Dataset → ML_Model (1 : Many)
- Job_Posting → Prediction (1 : Many)
- ML_Model → Prediction (1 : Many)

---

## Project Structure

```text
Fake_Job_Offer_Detector/
│
├── app.py
├── model.pkl
├── tfidf.pkl
├── fake_job_postings.csv
├── Fake_Job_Detector.ipynb
├── README.md
├── requirements.txt
│
├── templates/
│   ├── login.html
│   └── index.html
│
├── static/
│   ├── style.css
│   └── images/
│
├── diagrams/
│   ├── Use_Case_Diagram.png
│   ├── ER_Diagram.png
│   ├── Flowchart.png
│   └── System_Architecture.png
│
└── screenshots/
    ├── Login_Page.png
    ├── Home_Page.png
    ├── Fake_Output.png
    └── Real_Output.png
```

---

## How to Run the Project

### Step 1
Clone the repository.

### Step 2
Install the required libraries.

```bash
pip install -r requirements.txt
```

### Step 3
Run the application.

```bash
python app.py
```

### Step 4
Open your browser and visit:

```
http://127.0.0.1:5000/
```

---

## Login Credentials

| Username | Password |
|----------|----------|
| admin | 1234 |

---

## Expected Output

After successful login, the user enters a job description into the application. The Machine Learning model analyzes the input and predicts whether the job posting is **Real** or **Fake**.

**Example Results:**

- ✅ Real Job Posting
- ❌ Fake Job Posting

---

## Project Outcome

The Fake Job Offer Detector successfully identifies fraudulent job postings using Machine Learning techniques. The application provides quick and reliable predictions through a simple web interface, helping users identify trustworthy job opportunities and avoid recruitment scams.

---

## Future Enhancements

- User Registration
- Admin Dashboard
- Database Integration (MySQL/MongoDB)
- Email Notifications
- Company Verification System
- Resume Analysis
- Job Recommendation System
- Deep Learning Models for Better Accuracy
- Cloud Deployment (AWS/Azure/Render)
- Mobile Application Support
- Multi-language Support

---

## Screenshots

The repository contains screenshots of:

- Login Page
- Home Page
- Real Job Prediction
- Fake Job Prediction

---

## Author

**Bhavashree Venkatachalam**

**Project:** Fake Job Offer Detector Using Machine Learning

**Technologies:** Python, Flask, Scikit-learn, Pandas, NumPy, TF-IDF, HTML, CSS, Git & GitHub

---

## License

This project is developed for educational and academic purposes.
