💳 Credit Risk Model
Empowering smarter credit decisions with explainable ML-based risk predictions.


This repository presents a machine learning–powered credit scoring system that predicts loan applicant risk categories—poor, Average, Good, and Excellent—based on financial and demographic indicators. Inspired by the CIBIL score methodology, the model aids in evaluating creditworthiness with transparency and interpretability.

🔗 Try the Live App
Click below to access the deployed Streamlit app:

👉 Launch the App https://credit-risk-model-machine-learning.streamlit.app/

📁 Project Structure
 ```commandline
├── artifacts/                # Directory for trained model
│   └── model_data.joblib     # Serialized trained model object
├── main.py                   # Streamlit app entry point
├── prediction_helper.py      # Core prediction and preprocessing logic
├── requirements.txt          # List of required Python packages
├── README.md                 # Project documentation
├── LICENSE                   # License information
├── StreamlitUI.png           # Screenshot of the UI
└── .gitignore                # Files and folders to ignore in version control
```
📊 Model Info
To improve prediction accuracy and usability:

A classification model was trained using features like income, loan amount, credit history, tenure, etc.

Feature preprocessing includes encoding categorical values and normalization, where needed.

The model outputs a risk category inspired by the logic behind the CIBIL score ranges.

⚡ Quick Start
1. Clone the Repository
```bash
git clone https://github.com/mochitha/credit-risk-model.git
cd credit-risk-model
```
3. Install Dependencies
```commandline
pip install -r requirements.txt
```
5. Run the Streamlit App
```commandline
streamlit run main.py
```

✅ Features
🧠 Intelligent credit risk classification

💡 Inspired by real-world scoring frameworks (like CIBIL)

🖥️ Clean, interactive user interface via Streamlit

📦 Modular codebase for easy customization and enhancement

🤝 Feedback & Contributions
Feel free to:

⭐ Star this repo if you found it helpful

🛠️ Raise issues for bugs, ideas, or enhancements

📬 Submit pull requests for contributions

📜 License
Licensed under the Apache 2.0 License.
