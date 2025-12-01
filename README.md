# 🏠 India Housing Real Estate Investment Advisor

## ML Capstone Project - Real Estate Investment Analysis

### 🎯 Project Overview
AI-powered investment advisor for India's real estate market using machine learning to predict property values and investment viability.

### 📊 Features
- **Good Investment Classification**: Predict whether a property is a good investment
- **Future Price Prediction**: Estimate property price after 5 years
- **Investment Score**: Multi-factor scoring system
- **Interactive Dashboard**: Streamlit-based web interface

### 🚀 Live Demo
[Streamlit Cloud App](#) *(Deploy and add link here)*

### 📁 Project Structure
```
India_Housing_Investment_Advisor/
├── app.py                          # Streamlit web application
├── india_housing_clean.csv         # Cleaned dataset (5000 samples)
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
└── India_Housing_ML_Capstone.ipynb # Complete ML pipeline notebook
```

### 🛠️ Technologies Used
- **Python 3.10+**
- **Streamlit** - Web interface
- **Scikit-learn** - ML models (Random Forest)
- **Pandas & NumPy** - Data processing
- **Matplotlib & Seaborn** - Visualization
- **XGBoost** - Gradient boosting
- **MLflow** - Experiment tracking

### 📈 Model Performance

#### Classification (Good Investment)
| Model | Accuracy | F1-Score |
|-------|----------|----------|
| Logistic Regression | 0.734 | 0.826 |
| **Random Forest** | **0.883** | **0.915** |
| XGBoost | 0.871 | 0.906 |

#### Regression (Future Price 5Y)
| Model | RMSE | R² |
|-------|------|----|
| Linear Regression | 136.32 | 0.558 |
| **Random Forest** | **7.49** | **0.999** |
| XGBoost | 10.50 | 0.997 |

### 🎓 EDA Highlights (20 Questions Answered)
1. Price & size distributions
2. Location-based pricing (state/city/locality)
3. Correlation analysis
4. Investment factor analysis (amenities, transport, parking)

### 📦 Installation

```bash
git clone https://github.com/alwinappu/India_Housing_Investment_Advisor.git
cd India_Housing_Investment_Advisor
pip install -r requirements.txt
streamlit run app.py
```

### 🌐 Deployment (Streamlit Cloud)

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect repository: `alwinappu/India_Housing_Investment_Advisor`
4. Deploy `app.py`

### 👨‍💻 Author
**Alwin Appu**  
📧 Email: appu050.1021@hotmail.com  
🐙 GitHub: [@alwinappu](https://github.com/alwinappu)  
📅 Date: December 1, 2025

### 📝 License
MIT License - Feel free to use for educational purposes

### 🙏 Acknowledgments
- Dataset: India Real Estate Data
- MLflow for experiment tracking
- Streamlit for rapid prototyping
