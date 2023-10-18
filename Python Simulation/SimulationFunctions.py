# This file contains the s
import LEDFunctions as LED
import LightFunctions as Light
import PoolFunctions as Pool
import Photosystem2 as PS2
import IDs as ID

#Current time of the step within the simulation
CurrentTime:int = 0

#Current step within the simulation
CurrentStep:int = 0

DefaultFrameData:list = [CurrentTime, CurrentStep]
CurrentFrameData:list = [DefaultFrameData]
NextFrameData:list = [DefaultFrameData]

#Packs the desired global simulation constraints into a list of the format [Steps, Stepwidth]

def RunSimulation (SimulationData:list=[DefaultFrameData]):
    
    LastFrameData:list
    CurrentFrameData:list
    CurrentLightOutput:list
    TimeParameters:list = SimulationData[ID.MAIN.IDConstant][ID.CONST.IDTime] 
    
    Frame:int = 1

    while Frame <= TimeParameters[ID.TIME.IDSteps]:
        CurrentFrameData = CreateNextFrame(Frame, SimulationData[ID.MAIN.IDConstant][ID.CONST.IDAllLEDSets][ID.LEDCONST.IDNumberofSets])
        CurrentLightOutput = DefineFrameLightInput(SimulationData[ID.MAIN.IDConstant], CurrentFrameData)
        CurrentFrameData
        
        SimulationData[ID.MAIN.IDFrameConditions].append(CurrentFrameData)
        Frame += 1

    return SimulationData

def DefineSimulationGlobalTimeParameters(Steps:int, StepWidth:int):
    return [Steps, StepWidth]

def CreateNextFrame(FrameNumber:int, NumberOfLEDSets:int):
    FrameOfFrame:list = [FrameNumber,[]]
    Runner:int = 0
    while Runner < NumberOfLEDSets:
        FrameOfFrame[ID.FRAME.IDLightEmission].append(0)
        Runner += 1
    return FrameOfFrame

def BakeSimulationConstConditions(AllLEDSetConditions:list, TimeParameters:list, WaveformSettings:list):
    #insert the number of All LED sets into the LED Set Conditions
    AllLEDSetConditions.insert(0, len(AllLEDSetConditions))
    SimulationConstConditions:list = [TimeParameters]
    SimulationConstConditions.append(AllLEDSetConditions)
    SimulationConstConditions.append(WaveformSettings)
    return SimulationConstConditions

def BakeStartFrameConditions(NumberOfLEDSets:int):
    #Runner:int = 0
    SimulationStartConditions:list = [CreateNextFrame(0, NumberOfLEDSets)]
    #append initial ligth input
    #while Runner < NumberOfLEDSets:
    #    SimulationStartConditions[0].append(0)
    #    Runner += 1

    return SimulationStartConditions

def DutyCycleOutput(DutyCyclePercent: float, Frequency:int, TimeStepWidth: int, CurrentTimeStep: int):
    #see if the light is currently on or off, depending on time within the simulation, the stepwidth, the frequency of the lght and the dutycycle
    if (CurrentTimeStep * TimeStepWidth) % Frequency < (DutyCyclePercent * Frequency):
        return 1
    else:
        return 0
    
def DefineFrameLightInput(ConstantConditions:list, FrameConditions:list):
    Runner:int=0
    while Runner < (ConstantConditions[ID.CONST.IDAllLEDSets][ID.LEDCONST.IDNumberofSets]):
        FrameConditions[ID.FRAME.IDLightEmission][Runner]=DutyCycleOutput(ConstantConditions[ID.CONST.IDWaveformSettings][Runner][ID.WAVEFORM.IDDutyCycle], 
                                                                          ConstantConditions[ID.CONST.IDWaveformSettings][Runner][ID.WAVEFORM.IDFrequency], 
                                                                          ConstantConditions[ID.CONST.IDTime][ID.TIME.IDWidth],
                                                                          FrameConditions[ID.FRAME.IDFrameNumber])
        Runner += 1
    return
