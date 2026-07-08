# Project Details

## Project Title
**Fake Job Offer Detector Using Machine Learning**

---

## Project Overview

The Fake Job Offer Detector is a Machine Learning-based system designed to identify fraudulent job postings. The system analyzes job descriptions, company details, and other job-related information to classify job offers as either genuine or fake. This helps job seekers avoid scams and improves the reliability of online recruitment platforms.

---

## Problem Statement

Online job portals contain numerous job advertisements, but some of them are fraudulent and intended to deceive applicants. Fake job offers can result in financial loss, identity theft, and misuse of personal information. Therefore, an intelligent system is required to automatically detect and classify fake job postings using Machine Learning techniques.

---

## Project Objectives

- Develop a Machine Learning model to detect fake job postings.
- Analyze job descriptions and company information for fraud detection.
- Classify job offers as genuine or fake.
- Assist job seekers in identifying trustworthy opportunities.
- Improve the security of online recruitment platforms.

---

## Module List

### Module 1: Data Collection
Collect and store datasets containing real and fake job postings.

### Module 2: Data Preprocessing
Clean the dataset, remove duplicates, handle missing values, and prepare data for analysis.

### Module 3: Feature Extraction
Convert textual job descriptions into numerical features using NLP techniques.

### Module 4: Model Training
Train Machine Learning algorithms such as Logistic Regression, Naive Bayes, and Random Forest.

### Module 5: Prediction
Predict whether a given job posting is genuine or fake.

### Module 6: Result Analysis
Display prediction results and evaluate model performance.

---

## Technology Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas, NumPy |
| NLP | NLTK, TF-IDF |
| Frontend | Streamlit (Optional) |
| Version Control | Git & GitHub |

---

# Database Design

## Table 1: User

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| user_id | INT (PK) | Unique User ID |
| name | VARCHAR(100) | User Name |
| email | VARCHAR(100) | User Email |
| password | VARCHAR(255) | User Password |
| role | VARCHAR(20) | Admin/User |

---

## Table 2: Job_Posting

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| job_id | INT (PK) | Unique Job ID |
| user_id | INT (FK) | User Reference |
| title | VARCHAR(200) | Job Title |
| company | VARCHAR(150) | Company Name |
| description | TEXT | Job Description |
| location | VARCHAR(100) | Job Location |
| salary_range | VARCHAR(50) | Salary Details |
| post_date | DATE | Posting Date |

---

## Table 3: Dataset

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| dataset_id | INT (PK) | Dataset ID |
| source | VARCHAR(100) | Dataset Source |
| description | TEXT | Dataset Description |
| records_count | INT | Number of Records |
| uploaded_date | DATE | Upload Date |

---

## Table 4: ML_Model

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| model_id | INT (PK) | Model ID |
| model_name | VARCHAR(100) | Model Name |
| algorithm | VARCHAR(100) | ML Algorithm |
| accuracy | FLOAT | Model Accuracy |
| training_date | DATE | Training Date |

---

## Table 5: Prediction

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| prediction_id | INT (PK) | Prediction ID |
| job_id | INT (FK) | Job Posting ID |
| model_id | INT (FK) | ML Model ID |
| result | VARCHAR(20) | Real/Fake |
| confidence_score | FLOAT | Prediction Confidence |
| prediction_date | DATE | Prediction Date |

---

## Database Relationships

| Parent Table | Relationship | Child Table |
|-------------|-------------|-------------|
| User | 1 : Many | Job_Posting |
| Dataset | 1 : Many | ML_Model |
| Job_Posting | 1 : Many | Prediction |
| ML_Model | 1 : Many | Prediction |

---

## Expected Outcome

The system automatically analyzes job posting information and predicts whether the job offer is genuine or fraudulent. This helps job seekers avoid scams and improves the security and reliability of online recruitment platforms.
