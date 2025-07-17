# Project Risk Agent: Predict → Interpret → Recommend → Notify

This AI-powered agent helps HR/PMs manage employee attrition risks by:
- Predicting employee churn
- Explaining the reasons using SHAP
- Recommending corrective actions
- Sending notifications via Slack
- Displaying everything in a Streamlit dashboard

## How to Run

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Train the model:
   ```
   python churn_model.py
   ```

3. Interpret predictions:
   ```
   python interpret.py
   ```

4. Run dashboard:
   ```
   streamlit run app.py
   ```

## Files

- `mock_data.csv` - Input HR data
- `churn_model.py` - Model training
- `interpret.py` - SHAP explanations
- `agent.py` - Action recommender
- `notify.py` - Slack/email notification
- `logger.py` - Logs actions
- `app.py` - Streamlit dashboard
