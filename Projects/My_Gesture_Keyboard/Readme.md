##### Credits - https://evilporthacker.blogspot.com/2017/10/gesture-driven-virtual-keyboard-using.html <br/>

##### Requirements
- PyAutoGUI
- Python3, OpenCV
- Any text editor placed at (0, 0) of the screen
- Yellow piece of paper ( from a post-it or a sticky note )

##### Constraints
- Every key of the keyboard is of fixed length
- All keys are square

##### Observations / Conclusion
- Used a FREERATIO window size so as to allow the user to stretch the window as
  per the resolution of the screen
- Note: The best lower and upper bounds for the yellow paper(post-it) was:
  [ 20  21 181]
  [ 32  98 255]
