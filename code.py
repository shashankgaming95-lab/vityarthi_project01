#installing bellow package
!pip install scikit-learn numpy pandas

import pickle
import json
import numpy as np
from sklearn.naive_bayes import MultinomialNB

# ml model function
def load_encoder():
    # manual mapping
    return {
        "mood": {"happy": 2, "neutral": 1, "sad": 0},
        "energy": {"high": 2, "medium": 1, "low": 0},
        "stress": {"low": 2, "medium": 1, "high": 0},
        "workload": {"light": 0, "medium": 1, "heavy": 2}
    }

def load_model_intensity():
    X = np.array([
        [8,2,2,2,0],  # This Shows:-high sleep, happy, high energy, low stress, light work which means active
        [6,1,0,2,1],  # This Shows:-low sleep, neutral, low energy, high stress, medium work which means light
        [7,1,1,1,1],  # This Shows:-avg sleep, neutral, medium energy, medium stress, medium work which means balanced
    ])
    y = np.array(["active","light","balanced"])
    m = MultinomialNB()
    m.fit(X,y)
    return m

def load_model_routine_type():
    X = np.array([
        [8,2,2,2,0],  # if it isactive day -> fitness
        [6,1,0,2,1],  # if it is light day -> relaxation
        [7,1,1,1,1],  # if it is balanced -> productivity
    ])
    y = np.array(["fitness","relaxation","productivity"])
    m = MultinomialNB()
    m.fit(X,y)
    return m

# it is for inputing the data
def collect_user_inputs():
    print("Welcome to Healthy Routine ML Chatbot!")
    sleep_hours = float(input("How many hours did you sleep last night? "))
    mood = input("How is your mood today (happy/sad/neutral)? ")
    energy = input("What is your current energy level (low/medium/high)? ")
    stress = input("Your stress level (low/medium/high)? ")
    workload = input("Today's workload (light/medium/heavy)? ")
    interests = input("Any special interests/goals today? ")
    return {
        "sleep_hours": sleep_hours,
        "mood": mood,
        "energy": energy,
        "stress": stress,
        "workload": workload,
        "interests": interests
    }

# it is Preprocessing the input
def preprocess_inputs(inputs, encoders):
    x = []
    x.append(inputs['sleep_hours'])
    for feature in ["mood", "energy", "stress", "workload"]:
        mapping = encoders[feature]
        x.append(mapping.get(inputs[feature], 0))
    return np.array(x)

# it is a Routine Generator module
def generate_routine(intensity, routine_type, inputs):
    routine = []
    wake_hour = max(6, int(8 - inputs['sleep_hours']//1))
    routine.append(f"Wake up at: {wake_hour}:00 AM")
    if routine_type == "fitness":
        routine.append("Do morning workout/yoga:-")
    elif routine_type == "productivity":
        routine.append("Morning planning & focus session:-")
    elif routine_type == "relaxation":
        routine.append("Gentle morning stretching & meditation should be done")
    routine.append("Healthy breakfast")
    routine.append(f"Work blocks: {inputs['workload']}")
    if intensity == "active":
        routine.append("Take Active breaks: walk, stretch every 2 hours")
    else:
        routine.append("Take Regular short breaks & hydration")
    routine.append("You should Limit screen time to 2 hours outside work")
    routine.append("Evening routine & dinner should be:-")
    routine.append("Wind down: reading/meditation")
    routine.append("Recommended sleep time: 10:30 - 11:30 PM")
    return routine

# it is for a Recommendation Engine
def get_recommendations(inputs):
    recos = []
    if float(inputs['sleep_hours']) < 7:
        recos.append("Aim for at least 7 hours of sleep tonight for optimal health.")
    if inputs['energy'] == "low":
        recos.append("Take short walks and hydrate to boost energy during the day.")
    if inputs['stress'] == "high":
        recos.append("Practice relaxation/mindfulness for 10 minutes in afternoon.")
    recos.append("Try to reduce screen-time outside work and get some fresh air.")
    if inputs['interests']:
        recos.append(f"Include time for: {inputs['interests']}")
    return recos

# it shows Main chat loop
def chatbot_main():
    encoders = load_encoder()
    m_intensity = load_model_intensity()
    m_routine_type = load_model_routine_type()
    # it Collects the input of user
    inputs = collect_user_inputs()
    # it Preprocess the inputted data
    features = preprocess_inputs(inputs, encoders).reshape(1,-1)
    # it Predicts the data
    intensity = m_intensity.predict(features)[0]
    routine_type = m_routine_type.predict(features)[0]
    # it Generates the output
    routine = generate_routine(intensity, routine_type, inputs)
    recommendations = get_recommendations(inputs)
    print("\n🌞 Your Personalized Healthy Routine is 🌞:-")
    for item in routine:
        print("-", item)
    print("\n💡 Recommendations:-")
    for r in recommendations:
        print("-", r)

if __name__ == "__main__":
    chatbot_main()
