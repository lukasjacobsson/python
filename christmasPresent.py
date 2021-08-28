

import os
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Rate = 0

speaker.Speak("merry christmas and a happy new year.")