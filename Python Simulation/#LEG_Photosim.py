import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import sympy

import PhysicalConstraints as Phys
import ReactionFunctions as Reac
import SimulationFunctions as Simu

#simulation of single chloroplast light uptake and metabolism
#Simulation should take place at the scale of 100s of usec. The interesting effects should appear at frequencies higher than 1Khz
#Hypothesis:
#-All Reaction Components of Photosynthesis have been identified
#-There is an optimal ratio of involved reaction centers, which can be determined by searching for highest throughput for dPH = 0
#-if the theoretical steady state output of the model matches real world measurements, a ratio for the components can be searched

#Non photochemical quenching might be something that actually does not exist, or rather, the data is misinterpreted at some points

#right now I'm still completly working on the light reactions

#at some point I need to code:
#A Program to calculate a 5-dimensional scalar field, determine its gradient and then find the maximum gradient. At least I think that is what I need to do to determine
#The actual ratios of the different Components of photosynthesis



#This is used to determine how big the area for the simulation is. I should probably check the literature for real values
TotalSimulationArea:int = 1000000
#Thylakoid Lumen Volume and Chloroplast Stroma Volumen will be used for PH Gradient calculations
LumenVolume:float = 1000
StromaVolume:float = 1000

#def CalculateIt (MaxTimeSteps:int, StepWidth:int, DutyCycle:float, Frequency:int, LightIntensity:float, TheTitle:str):
#initiate Variables






def PhotoEfficiency (TotalPhotosynthesis:float, TotalIrradiance: float):

    return TotalPhotosynthesis/TotalIrradiance


#This function determines if there is currently a photon input into the system. Output in the form of 
#arbitrary functions can be implemented as long as the return value stays in range of 0 and 1
  
#determine the fetch range and round to the next number
def DetermineFetchPoint (RangeReactionTime:float, RangeTimeStep:float):
    return math.floor(RangeTimeStep/RangeReactionTime)

def DeterminePHGradient (LumenPH:float = 7.32, StromaPH:float = 7.32):
    return
#This function determines how many Reactions are started and returns the new value for ready reaction centers and Free reaction Centers
#It should work for all relevant processes. The Relevant PH Gradient should be 0 except for Transport processes between Lumen and Stroma
#The efficiency will be applied to the free reaction centers. The target of the function so to say
#in case there are more ready sources than free targets, the free targets determin how many reactions are started



def SimulateChloroplast(MaxTimeSteps:int, StepWidth:float, DutyCycle:float, Frequency:int, LightIntensity:int, SimulationTitle:str):
    

    
    #Look at Chloroplast PH

     
    #Set constant for different Places of Reaction, Including amount of Centers and Reaction Time for the different Centers
    
    #The amount of the different Reaction Centers should be chosen as to result in an optimal electron transport under ideal Environmental Parameters
    #This means, that in case of a sudden light input, there will be a continuous flow of electrons if the PH Gradient is 0.
    #Basis for this assumption is space. Every reaction center requires a set amount of space in the membrane. There will be an optimal balance between their density and what they do.
    #The required value should result from the smallest denominator of reaction times.
    # Trust Nature!
    #All reaction times are in ms 



    #Here are the Variables that store the current state of the system at different times
    CurrentLightInput:int = 0   #make that a list
    Time:int = 0

    #Initiate start conditions
    CurrentFreePC:int = Phys.PlastocyaninProteins
    CurrentFreePQ:int = Phys.PlastoquinoneMolecules
    CurrentFreePS1:int = Phys.PS1Centers #this should probably start at 0, I have to look into it
    CurrentFreePS2:int = Phys.PS2Centers
    CurrentFreeB6F:int = Phys.B6FCenters
    CurrentADPMolecules:int = Phys.ADPMolecules
    CurrentATPMolecules:int = Phys.ATPMolecules
    CurrentStromaPH:float = Phys.MinimumStromaPH
    CurrentLumenPH:float = Phys.MaximumLumenPH
    CurrentNADPMolecules:int = Phys.NADPMolecules
    CurrentNADPHMolecules:int = Phys.NADPHMolecules
    CurrentO2Production:int = 0
    
    #The next values are only required for components of the system that have a reaction center in any way and belong to the light dependant reactions
    #Store how many Reactions started this simulation step
    StartedPCReactions:int = 0
    StartedPQReactions:int = 0
    StartedPS1Reactions:int = 0
    StartedPS2Reactions:int = 0
    StartedB6FReactions:int = 0

    #Store how many Reaction Centers are ready for the next step
    ReadyPC:int = 0
    ReadyPQ:int = 0
    ReadyPS1:int = 0
    ReadyPS2:int = 0
    ReadyB6F:int = 0

    #Initialize the timekeeping-values
    CurrentTimeStep:int = 0
    SimulationFrequencyValue:int = 1000000/Frequency
    CurrentLightInput:int = 0

    #A list to keep the results of the photon collision calculations
    #Store Value 1 @ spot 1 and Value 2 @ spot 2
    CurrentHitReactionCenters:int = (0,0)

    while CurrentTimeStep < MaxTimeSteps:
        #determine the current light input into the system from duty cycle
        CurrentLightInput.append(Simu.DutyCycleOutput(DutyCycle, SimulationFrequencyValue, StepWidth, CurrentTimeStep) * LightIntensity)

        #Calculate Step 1, Photosynthesis Center PS2 and PS1
        #Calculate how many reaction centers each have been hit
        CurrentHitReactionCenters = (Reac.HitReactionCenters(CurrentLightInput(CurrentTimeStep), CurrentFreePS1, CurrentFreePS2, TotalSimulationArea, (Phys.PS1ReactionCenterSize*CurrentFreePS1 + Phys.PS2ReactionCenterSize*CurrentFreePS2)))
        StartedPS1Reactions.append(CurrentHitReactionCenters(1))
        StartedPS1Reactions.append(CurrentHitReactionCenters(2))

        #Now we look how many of the started reactions are ready and append them to our lists
        #The order of the appends is not important here
        CurrentFreePS2.append(CurrentFreePS2(CurrentTimeStep-1) + Reac.FreeUpReactionCenters(StartedPS2Reactions(DetermineFetchPoint(Phys.PS2ReactionTime, StepWidth))))
        CurrentFreePC.append(CurrentFreePC(CurrentTimeStep-1) + Reac.FreeUpReactionCenters(StartedPCReactions(DetermineFetchPoint(Phys.PCTransportTime, StepWidth))))
        CurrentFreePS1.append(CurrentFreePS1(CurrentTimeStep-1) + Reac.FreeUpReactionCenters(StartedPS1Reactions(DetermineFetchPoint(Phys.PS1ReactionTime, StepWidth))))
        CurrentFreePQ.append(CurrentFreePQ(CurrentTimeStep-1) + Reac.FreeUpReactionCenters(StartedPQReactions(DetermineFetchPoint(Phys.PQTransportTime, StepWidth))))
        CurrentFreeB6F.append(CurrentFreeB6F(CurrentTimeStep-1) + Reac.FreeUpReactionCenters(StartedB6FReactions(DetermineFetchPoint(Phys.B6FTransportTime, StepWidth))))
        
        #Now we take a look at how many ready reactions will result in a reaction in the next step of the path
        #The order of the started reactions probably matters, as they are chained through source and target. But maybe not. They need some time to get ready anyway
        
        #We start with PQ Reactions. They get their source material from the PS2 complex
        StartedPQReactions.append(Reac.StartReactions(ReadyPS2(CurrentTimeStep-1), CurrentFreePQ, 0))
        StartedB6FReactions.append(Reac.StartReactions(ReadyPQ(CurrentTimeStep-1), CurrentFreeB6F, 0))
        StartedPCReactions.append(Reac.StartReactions(ReadyB6F(CurrentTimeStep-1), CurrentFreePC, 0))
        StartedPQReactions.append(Reac.StartReactions(ReadyPS2(CurrentTimeStep-1), CurrentFreePQ, 0))


        #Integrateion
        #NextIntegratedDarkReactionRate = IntegratedDarkReactionRate[CurrentTimeStep - 1] + DarkReactionRate[CurrentTimeStep -1]
        #NextIntegratedLightReactionRate = IntegratedLightReactionRate[CurrentTimeStep - 1] + LightReactionRate[CurrentTimeStep - 1]
        #IntegratedDarkReactionRate.append(NextIntegratedDarkReactionRate)
        #IntegratedLightReactionRate.append(NextIntegratedLightReactionRate)
        #Calculations



#Test Environment
#I should code some more broad use plot functions!
StartedReactions:int = (0,0)
n:float = 0
while n < 5:
    StartedReactions=Reac.StartReactions(100,100,n)
    print(StartedReactions)
    n = n + 0.1


x=0



