🧾 Personal Finance Tracker Dashboard
💡 Overview

The Personal Finance Tracker is a beginner-friendly Streamlit web app that helps users track and analyze their daily expenses.
It converts your raw expense data into an interactive dashboard with visual insights, spending analysis, and downloadable reports — perfect for students, professionals, or anyone learning data analytics.

🚀 Features

✅ Upload your expense CSV file (date, category, amount, description, user)
✅ Automatic data cleaning & analysis using Pandas + NumPy
✅ Interactive dashboard with real-time updates
✅ Expense breakdown by category, user, and month
✅ Visual insights (Pie, Bar, and Line charts) using Matplotlib + Streamlit
✅ Monthly income input to calculate savings & spending percentage
✅ One-click Excel report download with all summaries
✅ Built with simplicity for students & beginners

🧩 Technologies Used
Tool	Purpose
Python 3.x	Core programming language
Streamlit	Interactive web app framework
Pandas	Data manipulation and analysis
NumPy	Numerical computations
Matplotlib	Chart and visualization generation
XlsxWriter	Exporting Excel reports
📂 Project Structure
📁 personal-finance-tracker/
│
├── app.py                  # Streamlit dashboard code
├── expense.csv             # Sample dataset
├── output/
│   ├── category_pie_chart.png
│   └── finance_summary.xlsx
├── requirements.txt        # Dependencies list
└── README.md               # Project documentation

🧠 How It Works

Upload your CSV file containing expenses:
Example format:

date,category,amount,description,user
01-10-2025,Food,150,Veg Biryani,Aarav Sharma
02-10-2025,Transport,50,Bus Fare,Neha Reddy
03-10-2025,Books,200,Python Guide,Rohan Gupta


Enter your monthly income (₹) in the sidebar.

The dashboard displays:

Total and average expenses

Standard deviation (spending consistency)

Savings percentage

Charts showing spending patterns by category, user, and time

Download Excel Report with all analytics and charts.

🧰 Installation & Setup
Step 1: Clone the Repository
git clone https://github.com/<your-username>/personal-finance-tracker.git
cd personal-finance-tracker

Step 2: Install Dependencies
pip install -r requirements.txt


(If you don’t have a requirements.txt, create one with:)

pip freeze > requirements.txt

Step 3: Run the App
streamlit run app.py

Step 4: Open in Browser

Visit the local URL displayed (usually: http://localhost:8501)

📦 Deployment (Streamlit Cloud)

You can deploy this app for free using Streamlit Cloud:

Push your project (with app.py and expense.csv) to GitHub

Go to https://share.streamlit.io

Connect your GitHub repo → Select app.py → Deploy

Your live dashboard will be available at a public URL 🎉

📊 Example Dashboard Preview

Expense Distribution by Category:


🧑‍💻 Author

Abhishek Kumar Harendra Gupta
📍 Mumbai, India
🎓 Data Science & AI Enthusiast | Streamlit Developer
📧 [Add your email or portfolio link here]

🏁 Future Enhancements

Multi-user authentication (login + personalized dashboard)

Integration with Google Sheets for live expense tracking

AI-based expense prediction and budgeting suggestions

Dark mode toggle

Dashboard insights via email

📜 License

This project is open-source under the MIT License.
You’re free to use, modify, and distribute it for educational or personal use.
