Healthcare Data Analysis

📌 Project Overview

This project focuses on data cleaning, preprocessing, and visualization of a healthcare dataset using Python. The dataset includes patient details such as age, blood pressure, cholesterol levels, symptoms, and disease outcomes.

📊 Features Implemented

Handling Missing Data:

Imputing numerical values with the median.

Imputing categorical values with the most frequent (mode).

Encoding Categorical Data using LabelEncoder.

Data Visualization:

Histogram of age distribution.

Bar chart of disease outcome distribution.

Box plot of blood pressure & cholesterol.

Pair plot to show relationships between variables.

🛠 Technologies Used

Pandas – Data handling

NumPy – Numerical operations

Matplotlib & Seaborn – Data visualization

Scikit-learn – Data preprocessing (handling missing values, encoding categorical data)

📂 Project Structure

├── healthcare.py  # Main script for data processing & visualization
├── healthcare_data.csv  # Sample dataset
├── README.md  # Project documentation

🚀 How to Run the Project

Clone the repository:

git clone https://github.com/your-username/healthcare-data-analysis.git
cd healthcare-data-analysis

Install dependencies:

pip install pandas numpy matplotlib seaborn scikit-learn

Run the script:

python healthcare.py

📌 Sample Dataset

Age

Blood Pressure

Cholesterol

Symptom

Disease Outcome

25

120

200

Y

0

30

130

220

N

1

...

...

...

...

...

📸 Output Visualizations

The script generates the following visualizations:

Histogram of Age Distribution

Bar Chart of Disease Outcomes

Box Plot of Blood Pressure & Cholesterol

Pair Plot of Numerical Features

🤝 Contributing

Feel free to fork this repository and contribute by:

Adding more features or datasets.

Improving visualizations.

Optimizing data processing.

📜 License

This project is open-source and available under the MIT License.
