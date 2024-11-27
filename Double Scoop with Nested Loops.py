import random

# List of moods
moods = ["Happy", "Sad", "Energetic", "Tired", "Calm", "Excited", "Angry"]

# List of times of the day
times_of_day = ["morning", "afternoon", "evening"]

# List of days of the week
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


for day in days_of_week:
    
    for time in times_of_day:
    
        mood = random.choice(moods)
        
        # Print the mood for that day and time
        print(f"On {day} {time} you were feeling {mood}.")