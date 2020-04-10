# Programmer - Milind Diwane
# for mp3 pygame module
#
# Healthy programmer
#   9 am to 5 pm
# Water  - water.mp3   -3.5 ltrs total 18 glasses   - after drinking water (input-drank)-time reset - maintain log




# Eyes  - eyes.mp3   - every 30 min - after eyes exercise (input-EyDone)  - time reset  -maintain log
# Physical activity  - physical.mp3  - every 45 mins  - after exercise (input-ExDone)  - time reset  maintain log

# Rules - use pygame module to play audio


import pygame
import time
import datetime

m=pygame.mixer

def play_music(file):
    m.init()
    m.music.load(file)
    m.music.set_volume(0.7)
    m.music.play()

def stop_music(file):
    m.music.stop()

def write_to_file(str):
    f = open(report,"a")
    f.write(str)
    f.close()


def IsOfficeTime(currenttime):
    if currenttime > '09:00:00' and currenttime < '17:00:01':
        return True
    else:
        return False

report="health_report.txt"
water_music_file="water.mp3"
eye_music_file="eyes.mp3"
physical_music_file="physical.mp3"

NumberofWaterRemaining = 18

waterAfterEvery = 1200  # Seconds  - 20 minutes
eyeExerciseAfterEvery = 1800  # Seconds - 30 minutes
physicalExerciseAfterEvery = 2700  # Seconds  - 45 minutes

water_taken_at=time.time()
eye_Exercise_At = time.time()
physical_Exercise_At = time.time()

currenttime = time.strftime('%H:%M:%S')
print(currenttime)
SleepTime = 60  # Sleep time in seconds It will check after every 60 seconds.

while (IsOfficeTime(currenttime)):
    #     Check for water
    if NumberofWaterRemaining > 0 and (time.time() - water_taken_at) > waterAfterEvery:  # water after every 20 minutes
        print("Time to drink water")
        while True:
            play_music(water_music_file)
            comment = input("Please enter any comment, if you want to add : ")
            if input("Enter 'Done' if you had water: ").lower() == "done":
                water_taken_at = time.time()
                NumberofWaterRemaining -= 1
                stop_music(water_music_file)
                str = f"\nyou drink 200 ml water -Comment : {comment} at ---- {time.asctime(time.localtime(time.time()))}"
                write_to_file(str)
                break
    if time.time() - eye_Exercise_At > eyeExerciseAfterEvery:
        print("Time to do eye exercise")
        while True:
            play_music(eye_music_file)
            comment = input("Please enter any comment, if you want to add : ")
            if input("Enter Done if you done eye exercise : ").lower() == "done":
                eye_Exercise_At = time.time()
                stop_music(eye_music_file)
                str = f"\nyou did Eye Exercise -Comment : {comment} at ---- {time.asctime(time.localtime(time.time()))}"
                write_to_file(str)
                break
    if time.time() - physical_Exercise_At > physicalExerciseAfterEvery:
        print("Time to do Physical exercise")
        while True:
            play_music(physical_music_file)
            comment = input("Please enter any comment, if you want to add : ")
            if input("Enter Done if you done Physical exercise : ").lower() == "done":
                PhysicalExerciseAt = time.time()
                stop_music(physical_music_file)
                str = f"\nyou did Physical Exercise -Comment : {comment} at ---- {time.asctime(time.localtime(time.time()))}"
                write_to_file(str)
                break
    time.sleep(SleepTime)
    currenttime = time.strftime('%H:%M:%S')
    print(currenttime)

