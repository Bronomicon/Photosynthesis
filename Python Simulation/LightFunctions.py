#Definition of activity of PS1 per Wavelength
import Wavelengthcharacteristica as WAVE
import random as rng
import LEDFunctions as LED

def AbsorbtionBasedDampening(LEDSet:list=[], FrameLEDActivity:float=1):
    return round(LEDSet[LED.IndexAbsorbtion] * LEDSet[LED.IndexIntensity] * FrameLEDActivity)

def CalculateHits(Photons:int, AcceptorsAmount:int, ReadyAcceptorsAmount:int, RelativeActivity:float):
    
    Total:int = AcceptorsAmount
    Ready:int = ReadyAcceptorsAmount
    Excited:int = 0
    
    for Incoming in round(Photons * RelativeActivity):
        if rng.random() * Total <= Ready:
            Ready = Ready - 1
            Excited = Excited + 1
        return

    return Excited
