namn = input('Vad heter du?')
print('hej '+ namn)
print('välkommen till python ')
print('du skapar kodar eller något annat trycker du på knappen med 2 papper och sedan trcker du på det vikta pappret med ett plus på, och sedan skriver du ett namn och på slutet skriver du en punkt och det program t.ex py = python och så klart.... ')

import os
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Rate = 0

speaker.Speak("welkomme to Visual studio code")