# Healthy Routine ML Chatbot

## Overview:-

This project is an intelligent Python-based chatbot that generates a personalized healthy daily routine based on user inputs such as sleep hours, mood, energy levels, stress levels, workload, and daily interests.  
The system uses a hybrid Machine Learning + Rule-Based approach to provide customized routines and recommendations.

## Features:-

1. Conversational chatbot interaction
2. Predicts daily routine intensity light or balanced or active
3. Predicts routine type fitness or productivity or relaxation
4. Generates complete morning–night routine
5. Provides recommendations on screen-time, habits, and lifestyle
6. Modular, maintainable Python codebase
7. Uses Naive Bayes ML models

## Technologies Used

1. Python 3
2. Scikit-learn
3. NumPy / Pandas
4.  Pickle
5. Jupyter Notebook
6. Rule-based logic
7. Object-Oriented Programming

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

1. **Clone the repository**:-
   ```
   git clone <your-repo-link>
   ```

2. **Install dependencies**:-
   ```
   pip install -r requirements.txt
   ```

3. **Run the chatbot**:-
   ```
   python main.py
   ```

## Testing Instructions

- Provide the sample input to validate chatbot flow
- Test wheather low sleep, high stress, invalid categories
- Verify the ML's predictions and routine generation

## Screenshots
