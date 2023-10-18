#Physical Constraints
#These are taken from various sources and represent measured values for different settings
#They should be passed to the relevant functions




#dPH regulates B6F activity

#LHC1 and LHC2 regulate the activity of PS1 and PS2. How fast they do it will be a major concern!

#How mobile are LHC1 and LHC2?

#Redox Poise describes the ratio between reduced and oxidized state of one of the photosynthetic components

#Where is the 6:9 regulation for NADPH/ATP production? -> Should come from the balance of CET 1 and 2
#PGR5 should be there to make it happen
#but how?
#its CET1 and CET2
#CET1 produces NADPH. CET2 produces additional dPH and thus additional ATP.
#The higher the activity of CET2, the higher the higher the lower the NADPH/ATP ratio gets.
#This means, CET1 is probably the primary process that outproduces ATP.
#So CET1 is probably limited. Any excess from CET1 increases CET2 activity which increases dPH, which increases ATP production and reduces PS1 activity, which reduces NADPH production.
#Steady state should produce an NADPH/ATP Ratio of 6:9
#Where comes PGR5 into play?
 

#There seem to be several regulations within the system.
#-PQ is used by to connect B6F with both NDH1 and PS2
#-dPH determines PS2 Efficiency. Probably due to PC behaving differently under different dPH. It seems to be membran bound, so maybe there is some effect there
#-FD is used by both the CET1 and CET2 cycle.
#-rerouting FD via CET2 ultimately increases ATP production at the cost of NADPH production
#
#Both seem to involve the PS1 Center
#First is the 

#######################
# General Constraints #
#######################


ElectronExchangetime:float = 1
ProtonExchangetime:float = 1

MinimumLumenPH:float = 5.7                        #the minimum value ph within the Lumen can reach
MaximumLumenPH:float = 7.32
MinimumStromaPH:float = 7.32                    
MaximumStromaPH:float = 8
StromaVolume:float= 19,51916728 #um³
Lumenvolume:float = 0,48083272  #um³

###########################
# Reaction Rate Constants #
###########################
#Reaction Rate Constant for PC and PS1 etc. 

RrcPCPS1:float = 1          #3.9 * 10^8 1/(M*s) #Ilya B. Kovalenko et.al. 2010 (theoretical)   
                            #4.2 * 10^8 1/(M*s) #Hervas et al. 1992 (experimental)    
RrcPCB6F:float = 1          #3,4 Direct simulation of plastocyanin and cytochrome f interactions in solution (theoretical)
RrcFDPS1:float = 1          #0,3 A LASER FLASH SPECTROSCOPY STUDY OF THE KINETICS OF ELECTRON TRANSFER FROM SPINACH PHOTOSYSTEM I TO SPINACH AND ALGAL FERREDOXINS (Experimental)
RrcFDFNR:float = 1          #21,3 (um/s) Roles of Ferredoxin-NADP+ Oxidoreductase and Flavodoxin in NAD(P)H-Dependent Electron Transfer Systems
RrcFDNDH1:float = 1         #
RrcFNRB6F:float = 1         #This one is most like PH dependent
RrcPQPS1:float = 1          #
RrcPQB6F:float = 1          #
RrcPQH2B6F:float = 1        #
RrcPQNDH1:float = 1         #


#############################
# Membrane bound components #
#############################

#So, within the membrane there also seems to be something called PGRL1.
#Right now it seems to be an enzyme that connects FNR with PQ.
#Does it need B6F for this?

#Photosynthesis 1
#Behaviour:
PS1Centers:int = 1000
PS1ReactionTime:float = 0.2 #ms
PS1ReactionCenterSize:int = 1
PS1ProtonAcceptors:int = 2
    
#Photosynthesis 2
#Source of the process: Harvests light energy to excite electrons
#Target of the process: Reduces Platiquinone (PQ) to Plastoquinol (PQH2)
#Two protons will be taken from the Stroma, two from H20 in the Lumen.
#Two will be donated to PQ, together with harvested electrons to form PQH
#Behaviour:
#The PS2 behaves as a reaction complex
#Light excites the complex which then Splits an H20, taking two electrons from it and thus increasing H+ concentration in the lumen by +2
#At the same time O will be created which is probably removed from the lumen.
#The two electrons taken will be transferred to PQ which is turned into PQH.
#PS2 takes the required protons for this from the stroma, changing H+ in the process by -2
#Reactions will always occur. The process is reset by contact with PQ.
PS2Centers:int = 1000
PS2ReactionTime:float = 1 #ms
PS2ReactionCenterSize:int = 1
PS2ProtonAcceptors:int = 2    #source: Directly from Stroma -> influences dPH
PS2ElectronAcceptors:int = 2  #source: light + H20 From Lumen
PS2H2OAcceptors:int = 1       
    
#PlastoquinoneMolecule (PQ) /Plastoquinol (PQH2)
#these transport electrons through the membrane.
#Source of the Process: NDH/PS2
#Target of the Process: B6F
#They also pump H+ into the Thylakoid Lumen
#Behaviour:
PQTransportTime:float = 0.6 #ms
PQMolecules:int = 1000
PQElectronAcceptors:int = 2

#Cytochrome B6F complex (B6F)
#These pump 4 H+ into the lumen. They use Energy from PQ and GPR5
#Source of the Process: GPR5, PQH2
#Target of the Process: Pumping H+ into the lumen and providing electron enriched PC for PS1
#Behaviour:
#B6F behaves as a reaction complex
#B6F rearms FD after it has been spent in FNH creating NADP. It most likely uses PGR5 as reductase in the process.
#
B6FCenters:int = 1000
B6FTransportTime:float = 20 #ms
B6FProtonAcceptors:int = 4 #4?
B6FElectronAcceptors:int = 4 #4?

#ATP Synthase
#These let H+ from inside the Lumen flow to the Stroma, 
#They create ATP in the process
#Source: dPH from stroma to lumen, ADP and P from the Stroma
#Target: Pumps H+ into the Stroma, enriches Stroma with ATP
#Behaviour:
ATPSynthaseProteins:int = 1000
ATPSynthesisTime:float = 1000
ATPProtonAcceptors:float = 4.7 #That might be a problem. I should increase all values by ten maybe

#And these are also here. I think now I have them all
#NDH-1 Multi subunit complex. This takes enriched Ferredoxin and uses it to Pump H+ into the lumen and enrich PQ
#Ferrodoxin probably contributes two H+ and two electrons
#Source: enriched Ferrodoxin, H+ from the stroma
#Target: enrich PQ, pump H+ to the lumen
#Behaviour:
NDH1Centers:int = 10000
NDH1ReactionTime:float = 0.2
NDH1ProtonAcceptors:int = 4
NDH1ElectronAcceptors:int = 4

###########################
# Stroma bound components #
###########################

#Do not forget ADP and ATP, these are linked in a cycle
#they are input and output of the ATP-Synthase
#Adenosin Diphosphat, Adenosin Triphosphat
#Behaviour:
ADPMolecules:int = 10000
ATPMolecules:int = 0

#And also do not forget NADP and NADPH, you need to simulate the full system
#Where are these actually within the system?
#Nicotinamidadenindinukleotidphosphat
#Behaviour:
NADPMolecules:int = 10000
NADPHMolecules:int = 10000
NADPTTransportTime:float = 1

#There is more. CET1 and CET2 seem to contain additional components.
#Maybe I should include mobility in the calculations one day
#one day, one day, one day.....

#Ferredoxin-NADP+-Reductase
#Behaviour:
FNRProteins:int = 10000

#Ferredoxin probably contributes two H+ and two electrons
#Behaviour:
#FD is attracted to the required binding sites through long range electrostatic forces. These should be at PS1 and FNR.
FDProteins:int = 10000
FDElectronReceptors:int = 2
FDProtonAcceptors:int = 2

#PGR5
#Assumption: These allow Spent enriched FNR to rearm. Meaning, it decouples FD from FNR, freeing up both components.
#PGR5 is most likely a reductase for B6F and spent FNR+FD and will henceforth be treated as such.
#PGR5 concentrations are used to regulate CET1 activity.
#Or rephrased: PGR5 determines outflow speed of CET1
#What does PGR5 actually do?
#Source: Reduced armed FNR
#Target: B6F,
#Behaviour: 

##########################
# Lumen bound components #
##########################

#PlastocyaninProteins (PC)
#these transport electrons from B6F to PS1
#Behaviour: PC transports electrons from B6F to P700+ in the PS1 complex
#Chance to attach to B6F is determined by ready PC concentration and PH in the Lumen
#Time to detach seems to be static. So once Contact has been made the process starts
#PC is attracted to the required binding sites through long range electrostatic forces.
#PC should possibly be modelled by a flow. The number of carriers in respect to reaction
#centers should be high enough to forgoe first order requirements for diffusion.
#The Interaction between mobile proteins is dictated by brownian motion and electrostatic forces.
#A curve can be implemented to simulate the number of collisions. See Simulation of Interaction of Photosystem I
#Relevant Values to implement the Curve should:
#

PCTransportTime:float = 0.2 #ms
PCEnzymes:int = 1000
PCElectronAcceptors:int = 1

#########################
# Additional Components #
#########################
#Rubisco
#rubosomething. The thing from the calvin cycle. Takes NADPH and ATP and fixates CO2