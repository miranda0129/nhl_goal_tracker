## 🚨 Nhl Goal Tracker
*🚀 Powering your GameBuddy*

### Purpose
The purpose of this code is to track goals of a given NHL team throughout a game. 

### Usage

1. Create python virtual environment
2. Pip install
3. python3 main.py

main.py contains the constant TEAM_ABBREV which sets team value for which you are tracking. 

### Testing

testDisplay.py is a driver class that has been used to test the various text displayed throughout time. In particular the goal animation

### Context

this program is designed to be run on something like a raspberry pi powering a led display.

### Behaviour

When your team is not playing a live game, the display shows the date and time of the next game (currently assuming eastern time zone).


<img src="/readmePhotos/nextGame.jpg" alt="The Game Buddy next game display. It includes a led lit 3D printed logo on top. It reads, The next game is at December 31, 8 pm." width="200"/>

During a live game. The score of the game is displayed including your team and opposing team abbreviations. When your team scores, the screen will flash red and white reading GOAL! 

<img src="/readmePhotos/liveGame.jpg" alt="The game buddy live game display. It reads, Detroit verses Philly, 0, 0." width="200"/>

### Improvements

1. Make time zone dependent only on a single constant so other time zones could be supported

It also would have been nice to spruce up the display a bit more. Experimenting with elements such as 

1. Fonts
2. Backgrounds
3. Goal animations
