🎓 Student Placement Prediction System

A Machine Learning project that predicts whether a student is likely to be placed based on academic and attendance-related information.

🚀 Features

- Student placement prediction
- Data analysis using Pandas
- Data visualization using Matplotlib and Seaborn
- Random Forest Machine Learning model
- Model accuracy evaluation
- Confusion matrix
- Feature importance analysis
- Flask web application
- Responsive student prediction form

🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Flask
- HTML
- CSS

📂 Project Structure

student-ml-project/
│
├── dataset/
│   └── students.csv
│
├── model/
│   └── placement_model.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── analysis.py
├── train_model.py
├── app.py
├── requirements.txt
├── .gitignore
└── README.md

⚙️ Installation

Clone the repository:

git clone YOUR_GITHUB_REPOSITORY_URL

Open the project:

cd student-ml-project

Create a virtual environment:

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

🧠 Train the Machine Learning Model

Run:

python train_model.py

This trains the Random Forest model and creates:

model/placement_model.pkl

📊 Run Data Analysis

Run:

python analysis.py

This generates visualizations such as:

- Placement distribution
- Study hours vs placement
- Attendance vs placement
- Correlation heatmap
- Confusion matrix
- Feature importance

🌐 Run the Flask Application

Start the application:

python app.py

Open your browser and visit:

http://127.0.0.1:5000

🔄 How It Works

Student Data
     ↓
Pandas Data Processing
     ↓
Exploratory Data Analysis
     ↓
Train/Test Split
     ↓
Random Forest Model
     ↓
Model Evaluation
     ↓
Flask Web Application
     ↓
Placement Prediction

📥 Input Features

The model uses:

- Study Hours
- Attendance
- Assignment Score
- Internal Marks
- Previous Percentage

📤 Output

The system predicts:

PLACED

or

NOT PLACED

🎯 Project Purpose

This project demonstrates a complete beginner-friendly Data Science and Machine Learning workflow, from dataset analysis and model training to deploying predictions through a Flask web application.

⚠️ Disclaimer

This project is created for educational purposes. The prediction is based only on the provided sample dataset and should not be considered a real-world placement decision system.

👨‍💻 Author

Zaid Haque

Diploma in Computer Science Engineering