# Healthy Routine Chatbot - Humanized Structure

## What This Project Does

Imagine having a personal wellness coach that asks you a few simple questions about your day, like how well you slept, how stressed you are, your mood, and this coach give you a customized daily schedule to help you feel better. That's what this chatbot does! It uses AI to understand your situation and suggests activities for morning, afternoon, and evening that matches your needs.



## How It Works

1. You talk to the chatbot
2. You answer questions about yourself (sleep, mood, stress, workload)
3. The AI learns from your answers and processes them
4. The AI predicts two things:
   - How intense should your day be? (take it easy vs. go hard)
   - What should you focus on? (exercise vs. work vs. relaxation)
5. The chatbot gives you a personalized schedule
6. You get wellness tips based on your situation


## Project Organization

### Core Files - The Brain of the Chatbot

**chatbot_interface.py**

This is the "face" of the chatbot where you talk to it. It's responsible for greeting you and keeping the conversation flowing, while also asking follow-up questions to understand what you need. The file shows you the final results in a nice, readable way and make sure everything is presented correctly.

**input_handler.py**

This file listens carefully to everything you tell the chatbot. It makes sure you give valid answers, for example you can't sleep negative hours! It stores all your information safely and asks clarifying questions if something don't make sense.


### Intelligence Files - The Decision Makers

**routine_type_model.py**

This file learns patterns from lots of past data about people. When you give your information, this AI decides whether you should focus on fitness, productivity, or relaxation. It uses something called Naive Bayes, a machine learning algorithm, to make smart guesses. If you say you are very stressed and have heavy work, it might suggest relaxation instead of a workout.

**intensity_model.py**

Another AI that decides whether your day should be light, balanced, or active. It looks at your sleep, energy, and stress to make this decision and understand your situation. If you only slept 4 hours, it won't suggest a 45-minute workout.

**preprocessor.py**

This file takes your human answers and converts them to something the AI can understand. It encodes things like "happy" to a number, "stressed" to another number and loads these encodings so the AI always understands the same way. It makes sure data is in the right format before the AI sees it.


### Helper Files - The Doers

**routine_generator.py**

This file takes the AI's predictions and creates an actual daily routine. It has a library of activities for different scenarios including light day activities like gentle yoga and short walks, balanced day activities with a mix of exercise and work. It picks activities that match what the AI predicted and shows them to you in a nice morning to afternoon to evening format.

**recommendation_engine.py**

This file looks at your information and gives personalized tips. If you are sleep-deprived, it suggest better sleep habits and if you are stressed it recommend relaxation techniques. It adapts recommendations based on your unique situation and provide tailored advice.


### Entry Point

**main.py**

This is what you run to start the whole thing. Just one command: python main.py will connects all the pieces together and gets the conversation started.

**requirements.txt**

This file lists all the tools and libraries you need to install. Before running the chatbot, you install everything listed here.


## The Data Flow

<img width="706" height="574" alt="Screenshot 2025-11-24 185508" src="https://github.com/user-attachments/assets/cdcec03f-cbbc-4103-88e6-b20c5111e119" />


## What Each File Needs to Do

<img width="827" height="374" alt="Screenshot 2025-11-24 185459" src="https://github.com/user-attachments/assets/d47418d7-d419-4ebb-b45c-3dc6f6f9f0db" />


## How to Use This Project

What Happens Next:

1. Chatbot says hello
2. You answer 5-6 simple questions
3. AI makes predictions
4. You get a personalized routine plus tips
5. You can generate another routine or exit
