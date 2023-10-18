#########################################################################
# This File contains the required functions to simulate the C6F-Complex #
#########################################################################

#####################
#  ----Q-CYCLE----  #         
#####################

###########
# Step A: #
###########

#Location:
# heam CN (Cn-site)

#Input & Sources: 
# FD-FNRred <- Stroma
# PQ        <- Membrane (This does not seem to belong here)

#Output & Targets:
# FD-FNRox  -> Stroma
# PQ        -> Qn-slot (This does not seem to belong here)
# 1e-       -> charged Cn-site
# 1H+       -> charged Cn-site

#Processes:

#The Cn-Site is charged with an e- and an H+.
#FD-FNRred is oxidized and released into the stroma

###########
# Step B: #
###########

#Location:
# Qp-Site

#Input & Sources: 
# PQH2      <- Membrane
# PQ        <- Present in Qn-Slot

#Output & Targets:
# PQH-       -> Further Occupies Qp-Site
# 1e-       -> Charged CytF
# 1H+       -> Lumen

# Processes:
# PQH2 is oxidized at the Qp-Site

###########
# Step C: #
###########

#Location:
# Qp-Site

#Input & Sources: 
# PQH-       <- Present in Qp-Slot

#Output & Targets:

# PQ        -> Occupies Qp-slot
# 1e-       -> Charges Bn-Site
# 1H+       -> Lumen

#Processes:
# PQH- reduces Bp
# Bp passes electron to Heam Bn

###########
# Step D: #
###########

#Location:
# General

#Input & Sources: 
# PQ        <- Present in Qn-Slot
# 1e-       <- Bn-Site -> Discharged
# 1e-       <- Cn-Site -> Discharged
# 1H+       <- Cn-Site -> Discharged
# 1H+       <- Stroma

#Output & Targets:

# PQH2      -> Qn-Slot -> PQ/Pool



############################
#  ----PC-Interaction----  #         
############################

#B6F donates electrons to PC through cytF


##############################
# ----Internal Reactions---- #
##############################


#Generally, all complexes will be modelled as state machines.
#it is kept track of how many of the complexes are in what state at which point in time.
#it should also be kept track on how many complexes changed state during a timeframe.
#Through this I should be able to calculate the turnover rates on an absolute level
#The throughput will be calculated once and then be used for
#The throughput will be calculated based on a static dtB6F

#- 3 Reaction Slots:
#   Fd-FNR
#   Qn
#   Qp

#- Reaction Sites: