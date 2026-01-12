FedEx AI-Driven DCA Assignment System

Problem Statement
Manual assignment of Debt Collection Agencies (DCAs) leads to low recovery rates and delayed escalations.

Solution
An AI-driven system that:
- Predicts recovery probability
- Calculates trust score of DCAs
- Automatically assigns the best DCA for each case
- Provides a working UI for decision support

ML Components
- Logistic Regression model to predict recovery probability
- Trust score computed using historical DCA performance
- Rule-based escalation risk assessment

## 📂 Project Structure
fedx_dca_ai/
│
├── backend/                     
│   ├── __init__.py
│   ├── decision.py              
│   └── trust_score.py           
│
├── ml/                       
│   ├── __init__.py
│   ├── train_model.py          
│   └── recovery_model.pkl
│
├── frontend/                    
│   └── app.py                   
│
├── data/                        
│   ├── raw_cases.csv           
│   └── dca_performance.csv    
│
├── requirements.txt          
├── README.md                    
└── .gitignore                  
