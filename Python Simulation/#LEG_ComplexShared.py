

import random as rng
import math
import PhysicalConstraints as Phys

#Let's start with the Reaction Centers
#Takes the number of Free PS1 or PS2 Reaction Centers and determines how many are struck by a photon during the current dt.
#Hit reaction Centers will be taken out of the equation.
def HitReactionCenters (HitPhotonNumber:int, InputOpenReactionCentersPS1:int, InputOpenReactionCentersPS2:int, HitTotalArea: int, HitAreaPerReactionCenter: int):

    CurrentOpenReactionCenters:int = InputOpenReactionCentersPS1 + InputOpenReactionCentersPS2
    CurrentOpenPS1:int = InputOpenReactionCentersPS1
    CurrentOpenPS2:int = InputOpenReactionCentersPS2

    for n in range (1, HitPhotonNumber, 1):
        if rng.randrange(1, HitTotalArea, 1) < ((CurrentOpenPS1 + CurrentOpenPS2) * HitAreaPerReactionCenter):
            if rng.randrange(0, CurrentOpenPS1 + CurrentOpenPS2, 1) <= CurrentOpenPS1:
                CurrentOpenPS1 = CurrentOpenPS1 - 1
            else:
                CurrentOpenPS2 = CurrentOpenPS2 - 1

    return (InputOpenReactionCentersPS1 - CurrentOpenPS1, InputOpenReactionCentersPS2 - CurrentOpenPS2)

#this function is used to free up reaction centers of the type passed. The specific field of the passed list should be determined 
#by the following DetermineFetchPoint-Function
def FreeUpReactionCenters (AmountOfTypeToFree:int):

    
    return AmountOfTypeToFree

def StartReactions (ReadyReactionCentersSource:int, FreeReactionCentersTarget:int, RelevantPHGradient:float = 0):
   
    MaximumPHGradient:float = 2.3       #I put this value here because it is basically a constant only used in this calculation. No need to calculate it every time
    CurrentEfficiency:float = math.exp(-(RelevantPHGradient/MaximumPHGradient))
    MaximumReactions:int = math.floor(FreeReactionCentersTarget*CurrentEfficiency)
    if ReadyReactionCentersSource > MaximumReactions:
        return (ReadyReactionCentersSource-MaximumReactions, FreeReactionCentersTarget-MaximumReactions)
    else:
        return (0, FreeReactionCentersTarget-ReadyReactionCentersSource)
 
 #NextLightReactionRate =((math.exp(-(LightProduct[CurrentTimeStep-1])/LPSL)))*(1-(math.exp(-(NextLightInput/LRRSL))))
        #NextLightProduct = LightProduct[CurrentTimeStep-1] + (NextLightReactionRate * LRC) - (NextDarkReactionRate * DRC)
        #NextDarkProduct = DarkProduct[CurrentTimeStep-1] + NextDarkReactionRate * DRC

#The different Reaction Centers and molecules generally 
#This should be used by PS2, PQ
def StartElectronExchange(Donors:int, Acceptors:int):
    return

def StartProtonExchange(Donors:int, Acceptors:int):
    return

def StartLightReaction(Donors:int, Acceptors:int):
    return

#Functions for PC and FD need to take electrostatic Forces and concentration 
#into account to determine the chance of meeting between them and the currently required reaction centers.
#Concentration will not be taken into account. Instead, only mean travel time will be looked at.
#Concentration dependent behaviour should be modelled by keeping track of all components, sub-components and their current state.

#I have a model for the formed complexes over time.
#If I interprete the curve correctly, complexes means, that a meeting between
#a ready PC and a ready PS1 occurs.
#After the collision, a complex is formed and both participants are taken from the equation
#The Ionic strengh of the solution plays a direct roll in this equation and can be implemented as an LUT hopefully
#The Paper already calculates the number of formed complexes at every timestep
#Beginning from here I can try to build the model. I have to start somewhere.

#This function calculates the current Value for K. K is the second order constant that dictates the current number of formations in dependence to Ionic Strengh of the solution.
#This removes dPH from the equation, but includes PH of Lumen and Stroma Directly 
#K is the Second-Order Associtian Rate Constant k
#This has been experimentally derifed and will be taken as first physical anchor point of the model


#Ionic Strengh of a solution
#The Ionic Strengh in this model is calculated by taking the amount of H+ directly, as it is the only contributor taken into account
#Later models might need to include additional contributors
#We can determin the starting ionic strengh by looking at the normal PH Values of Lumen and Stroma
#The absolute move from equilibrium to maximum PH should yield the relative volume of Lumen and Stroma 

#Probably not required anymore. As the Volume of the solution is now a known, I can calculare the concentration which is needed for the reaction rate
def CalculateProtonAmount (PHValue:float, SolutionVolume: int):
    Protons = 10^PHValue
    return Protons

#CalculateConcentration returns the concentration in 
def CalculateH3OConcentration (PHValue:float):
    return 10^(-PHValue)

# Ionic Strengh is calculated by multiplying the concentration with the square of the charge.
# This is added up for all stroma/lumen contents, which carry a charge
# For the moment I will calculate the base ionic strength and add a compensation value which will represent the presense of NaCl and other salts in the chloroplast.
# In the future the influence of external salt concentrations can be taken into account through "BaseIonicStrength"

#In the Stroma NaCl as well as H3O+ and NADP+ should determine the current Ionic strength
#The Players are:
#Stroma: 
# ~150mM K+
# 50-90 mM Cl-
# This leads to a base ionic strength of (1/2) * (150mM + 70 mM) = 110 mM
# So 110mM will be taken as the base Ionic strength. The influence of H+ on the ionic strength should actually be minor, so it is probably not a limiting factor.
# 

#This one gets mothballed. The Ionic strength is consideres a constant 110mM or 100mM. Moreover, it is actually only required for more complex simulations.
def CalculateIonicStrengh (BaseIonicStrength:int, SolutionConcentration:float, SolutionVolume:float):
    return BaseIonicStrength + SolutionConcentration 
    	
#Mass Action Law
# The Mass action law allows to calculate how many complexes between different participants are formed over the course of t.
# A second order reaction rate constant is needed 
# The MAL will be used to determine how many complexes have formed in the time of the last frame.
# It can definitely used for Reactants in Stroma and Lumen.
# Within the membrane another approximation might be needed.

#Reaction rate. Now I got you!
#The ReactionRate takes the absolute amount of present participants X and Y and calculate how often they react (collide) in a given timeframe
#This function can be used to determine all complex formations in the simulation.
#The participants are generally the reaction-sites of the different proteins and the stroma/lumen solutable participants like Fd, PC or Fd-FNR
#Every Reaction pair needs its own reaction constant.
#I will normalize all values to um³ and probably us.

def CalculateReactionRate(SoluteVolume:int, SolventXAmount:int, SolventYAmount: int, ReactionConstant:float, TimeFrame:float):
    Avogadro:float = 6 * 10^23
    ReactionRate:float

    ReactionRate = (Avogadro/SoluteVolume)*SolventXAmount*SolventYAmount*ReactionConstant*TimeFrame
    
    return ReactionRate