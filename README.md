# Healthy Routine ML Chatbot

## Overview

This project is an intelligent Python-based chatbot that generates a personalized healthy daily routine based on user inputs such as sleep hours, mood, energy levels, stress levels, workload, and daily interests.  
The system uses a hybrid Machine Learning + Rule-Based approach to provide customized routines and recommendations.

## Features

- Conversational chatbot interaction
- Predicts daily routine intensity (light / balanced / active)
- Predicts routine type (fitness / productivity / relaxation)
- Generates complete morning–night routine
- Provides recommendations on screen-time, habits, and lifestyle
- Modular, maintainable Python codebase
- Uses Naive Bayes ML models

## Technologies Used

- Python 3
- Scikit-learn
- NumPy / Pandas
- Pickle
- Jupyter Notebook
- Rule-based logic
- OOP (Object-Oriented Programming)

## Project Folder Structure

```
HealthyRoutineChatbot/
│
├── data/
│   ├── dataset.csv
│   └── encoder_mappings.json
│
├── models/
│   ├── intensity_model.pkl
│   └── routine_type_model.pkl
│
├── src/
│   ├── chatbot_interface.py
│   ├── input_handler.py
│   ├── preprocessor.py
│   ├── intensity_model.py
│   ├── routine_type_model.py
│   ├── routine_generator.py
│   └── recommendation_engine.py
│
├── training/
│   ├── train_intensity_model.ipynb
│   ├── train_routine_type_model.ipynb
│   └── preprocess_dataset.ipynb
│
├── main.py
│
├── README.md
└── statement.md
```

## Installation & Usage

1. **Clone the repository**:
   ```
   git clone <your-repo-link>
   ```

2. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

3. **Run the chatbot**:
   ```
   python main.py
   ```

## Testing Instructions

- Provide sample inputs to validate chatbot flow
- Test low sleep, high stress, invalid categories
- Verify ML predictions and routine generation

## Screenshots

*(Add after running your project)*

## License

This project is for academic purposes under VIT University’s flipped course evaluation.
