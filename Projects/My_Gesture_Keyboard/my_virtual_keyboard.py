# Credits -> https://evilporthacker.blogspot.com/2017/10/gesture-driven-virtual-keyboard-using.html

# We are going to design a keyboard which has 26 letters of the alphabet
# and has a space bar

# For each on the virtual keyboard we need 4 things
# - key label - the text displayed on the key
# - top left co-ordinate of the key
# - bottom right co-ordinate of the key
# - center co-ordinate of the key

# Import Statements
import cv2
import numpy as np
import pyautogui as pgui
import pickle
