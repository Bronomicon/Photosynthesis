import Wavelengthcharacteristica as WAVE
import IDs as ID

#Takes a core wavelength and creates side wavelengths for later use in more precise LED representations    
def DefineWavelengths(PrimeWavelength:int, WavelengthSpread:int=2, WavelengthSteps:int=2):
    
    Wavelengths:list=[PrimeWavelength]
    #Create lower bound

    for LowerStep in range(0, WavelengthSteps, 1):
        NextWavelength:int=(PrimeWavelength-((LowerStep+1)*WavelengthSpread))
        Wavelengths.insert(0, NextWavelength)
        
    for UpperStep in range(0, WavelengthSteps, 1):
        NextWavelength:int=(PrimeWavelength+((UpperStep+1)*WavelengthSpread))
        Wavelengths.append(NextWavelength)  

    return Wavelengths

def BuildLEDSet(SetIntensity:int, CoreWavelength:int, SetWavelengthSteps:int, SetWavelengthSpread:int):

    LEDSetIndexes:list = DefineWavelengths(CoreWavelength, SetWavelengthSpread, SetWavelengthSteps)
    LEDSetValues:list = []
    WaveLengthParameters:list = [GetWavelengthParameters(LEDSetIndexes[0])]
    Index:int = 1
    
    while Index <= len(LEDSetIndexes):
        WaveLengthParameters = GetWavelengthParameters(LEDSetIndexes[Index-1])
        WaveLengthParameters.append(SetIntensity)
        Index += 1
        LEDSetValues.append(WaveLengthParameters)
    return LEDSetValues

def BuildEmissionParameters(LEDSet:int, DutyCycle:float, Frequency:int):
    return [LEDSet, DutyCycle, Frequency]

def GetWavelengthParameters(Wavelength:int):

    for sublist in WAVE.Attributes:
        if sublist[0] == Wavelength:
            return sublist

    return WAVE.ErrorAttribute


