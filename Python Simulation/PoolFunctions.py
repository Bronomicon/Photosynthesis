#This file contains pool related functions like determination of occured contacts

#PQ Pool
DockedPQ:int = 0
DockedPQH2:int = 0
FreePQ:int = 0
FreePQH2:int = 0

PQState:list=[FreePQ, DockedPQ, FreePQH2, DockedPQH2]


def OccuredContacts(ParticipantA:int, ParticipantB:int, ReactionRate:int):
    return (ParticipantA*ParticipantB*ReactionRate)