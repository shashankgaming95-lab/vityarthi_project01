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
4. Pickle
5. Google Collab
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
  # git clone <your-repo-link>

2. **Install dependencies**:-
  # pip install -r requirements.txt

3. **Run the chatbot**:-
  # python main.py

## Testing Instructions

- Provide the sample input values to validate chatbot's data flow
- Test wheather low sleep, high stress, invalid categories are there
- Verify the ML's predictions and make routine generation

## Screenshots
Code Input:-
<img width="1908" height="929" alt="Screenshot 2025-11-24 171249" src="https://github.com/user-attachments/assets/45e21741-866c-4e92-a271-c235d814ed1d" />
<img width="1590" height="791" alt="Screenshot 2025-11-24 171302" src="https://github.com/user-attachments/assets/bf3dadfc-5b13-4a27-ab09-065d45bb7ea9" />
<img width="1919" height="937" alt="Screenshot 2025-11-24 171317" src="https://github.com/user-attachments/assets/ff6758a3-9c8d-4aab-8b42-ce60efeaefd1" />
<img width="1900" height="916" alt="Screenshot 2025-11-24 171333" src="https://github.com/user-attachments/assets/c421cf0a-1162-4e13-8bee-4f94dbb32905" />
<img width="1919" height="935" alt="Screenshot 2025-11-24 171357" src="https://github.com/user-attachments/assets/b4e029d2-428b-44d8-a294-9f1ad401414f" />
Code's Output:-
<img width="1718" height="838" alt="Screenshot 2025-11-24 182419" src="https://github.com/user-attachments/assets/1aa6ad71-812f-405a-bca7-7d5ed24115a2" />
