# Christmas Calendar

## Description
ChristmasCalendar is a Python project that uses Pygame library. Like the name suggests ChristmasCalendar is a calendar app that has openable lids that can be opened on the correct day. The app also contains beautiful art and sentimental music.

## Authors
- Code and music: Boris Hiltunen ([BorisHiltunen](https://github.com/BorisHiltunen))
- Art: Sarlotta Hiltunen ([zenzensama](https://www.instagram.com/zenzensama/))

## Tools and Libraries
- [Pygame](https://www.pygame.org/docs/)
- You can find required packets from requirements.txt

## Setup
- Clone or fork the repository.

- Install virtualenv if not already installed
-> (pip install virtualenv)

- Make an Virtual Environment
-> (virtualenv env)

- Access it
-> (Windows -> .\env\Scripts\activate -> Mac source env/bin/activate)

- Install requirements.txt
-> (pip install -r requirements.txt)

- Run
-> (Go inside refactored folder and write python runner.py)

## Calendar's structure
```GAP
- ├── env
- ├── refactored
- |   ├── app
- |   |   ├── __init__.py
- |   |   ├── data.py
- |   |   ├── event_analyser.py
- |   |   ├── file_management.py
- |   |   ├── game_visualizer.py
- |   |   ├── lid_management.py
- |   |   ├── roller.py
- |   |   ├── sound_and_music_management.py
- |   |   ├── time_management.py
- |   ├── images
- |   ├── music
- |   ├── sounds
- |   ├── __init__.py
- |   ├── runner.py
- ├── testing
- ├── unrefactored
- ├── .qitignore
- ├── picture_of_the_game.jpg
- ├── picture_of_the_game.png
- ├── README.md
- ├── requirements
```

## Demonstration


<p align="center">
  <img src="https://github.com/BorisHiltunen/ChristmasCalendar/raw/main/picture_of_the_game.png"/>
</p>
