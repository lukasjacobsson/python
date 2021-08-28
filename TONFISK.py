LÖSENORD = input("ANGE LÖSENORD:")
if LÖSENORD == "LUKASARBAST":
    print("KOREKT LÖSENORD")
    print("välkommen!")
    namn = input('Vad heter du? ')
print('hej '+ namn)
print('välkommen till turtle draw ')

from turtle import *
import winsound
for nummer in range(360):
    lukas = input('hur vill du åka nu ')
    if lukas == 'f':
        forward(100)
    if lukas == 'h':
        right(90)
    if lukas == 'v':
        left(90)
    if lukas == 'b':
        backward(100)
    if lukas == 's':
        right(45)
    if lukas == 'd':
        left(45)
    speed(nummer)
    color(nummer/360, 0.5, 0.9)
else:
    print("INBROTT")
    winsound.Beep(867,4573)