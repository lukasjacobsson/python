from turtle import *
for nummer in range(360):
    lukas = input('hur vill du åka nu ')
    if lukas == 'fram':
        forward(100)
    if lukas == 'höger':
        right(90)
    if lukas == 'vänster':
        left(90)
    if lukas == 'bakåt':
        backward(100)
    if lukas == 'sidan':
        right(45)
    if lukas == 'ditåt':
        left(45)
    speed(nummer)
    color(nummer/360, 0.5, 0.9)
    