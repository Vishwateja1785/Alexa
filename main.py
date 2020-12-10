import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import PyPDF2
import os
import webbrowser
import sys

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'open images' in command:
        talk('Ofcourse..In a moment')
        image_dir = 'Image Directory'
        images = os.listdir(image_dir)
        print(images)
        os.startfile(os.path.join(image_dir, images[0]))

    elif 'open music' in command:
        talk('Ofcourse..In a moment')
        music_dir = 'Music Directory'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'open movies' in command:
        talk('Ofcourse..In a moment')
        movie_dir = 'Movies Directory'
        movies = os.listdir(movie_dir)
        print(movies)
        os.startfile(os.path.join(movie_dir, movies[0]))

    elif 'open youtube' in command:
        talk('Ofcourse..In a moment')
        webbrowser.open('https://youtube.com')

    elif 'search' in command:
        talk('Ofcourse..In a moment')
        talk('What do you want to search for?')
        search = take_command()
        url = 'https://google.com/search?q=' + search
        webbrowser.get('chrome').open_new_tab(url)
        talk('Here is What I found for' + search)

    elif 'open google' in command:
        talk('Ofcourse..In a moment')
        webbrowser.open('https://google.com')

    elif 'date' in command:
        talk('sorry, I have a headache')

    elif 'are you single' in command:
        talk('I am in a relationship with wifi')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    else:
        talk('Please say that again.')


while True:
    run_alexa()
