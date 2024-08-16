import os

class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    
    # Paths to the ML models
    CHURN_MODEL_PATH = os.path.join(BASE_DIR, 'models', 'churn_analysis.sav')
    RECOMMENDER_MODEL_PATH = os.path.join(BASE_DIR, 'models', 'recommender.pkl')
    
    # Paths to datasets
    TEL_CHURN_DATASET_PATH = os.path.join(BASE_DIR, 'data', 'tel_churn.csv')
    AMAZON_DATASET_PATH = os.path.join(BASE_DIR, 'data', 'amazon.csv')
    
    # Paths to Jupyter Notebooks
    CHURN_NOTEBOOK_PATH = os.path.join(BASE_DIR, 'notebooks', 'churn_analysis.ipynb')
    RECOMMENDER_NOTEBOOK_PATH = os.path.join(BASE_DIR, 'notebooks', 'recommender.ipynb')
