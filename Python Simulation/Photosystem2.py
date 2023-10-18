#States of the Photosystem 2

#Model with light absorbtion superstate

#Data to store within a timeframe
ExcitedPS2inFrame:int=0

State_H20_PQ_On:int=0
State_H20_On:int=0
State_PQ_On:int=0
State_On:int=0
State_H20_PQ_Off:int=0
State_H20_Off:int=0
State_PQ_Off:int=0
State_Off:int=0

PS2State:list=[State_H20_PQ_On, State_H20_On, State_PQ_On, State_On, State_H20_PQ_Off, State_H20_Off, State_PQ_Off, State_Off]

def DetermineNextPS2Excitations(PS2States:list, ExcitedPS2inFrame:int):        
    return

def DetermineNextPS2Contacts(PS2States:list, ):
    return

def DetermineNextPS2Decay():
    return

#   Light   H20 PQ
#1      e   e   e   
#2      e   e   f
#3      e   f   e
#4      e   f   f
#5      f   e   e
#6      f   e   f
#7      f   f   e
#8      f   f   f

#State Transitions

#Origin Target  Trigger
#1      2       Contact
#1      3       Contact
#1      5       Capture
#2  	6       Capture
#2      4       Contact
#3      4       Contact
#3      7       Capture
#4  	8       Capture
#5      1       Decay
#5      6       Contact
#5      7       Contact
#6      2       Decay
#6      8       Contact
#7      3       Decay
#7      8       Contact