# 🔍 Job Trend Analyzer

A full-stack web application that analyzes and visualizes trends in job postings using **MySQL** and **Chart.js**.

## ✅ Features

- 📊 Visualizes most in-demand skills across job listings
- 📈 Real-time bar charts using Chart.js
- 💻 Responsive UI built with Bootstrap
- 🔌 Modular Flask backend connected to MySQL
- 🧩 Easy to extend with additional filters and visualizations

## 🛠️ Tech Stack

- **Frontend**: HTML, Bootstrap, Chart.js
- **Backend**: Python, Flask
- **Database**: MySQL

## 📁 Project Structure

```
job-trend-analyzer/
├── app.py                # Flask backend
├── config.py             # MySQL config
├── requirements.txt      # Python dependencies
├── sample_job_data.sql   # Sample job data
├── templates/
│   └── index.html        # Frontend HTML
└── static/
    └── chart.js          # Chart.js (via CDN)
```

## 🚀 How to Run Locally

1. Make sure MySQL server is running and the `job_trends` database is created.
2. Import the sample data:
   ```bash
   mysql -u root -p job_trends < sample_job_data.sql
   ```

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask app:
   ```bash
   python app.py
   ```

## 📝 License

This project is licensed under the MIT License.
