import Outputfunctions as OUT
import SimulationFunctions as SIM
import LightFunctions as Light
import LEDFunctions as LED
import IDs as ID
import Database as DATA



def Main():

    StartConditions:list = []
    LEDSetToAdd:list = []
    EmissionParameterToAdd:list = []
    SimulationWaveformSettings:list = []
    SimulationResult:list = []

    DatabaseHost:str =      "localhost"
    DatabaseUser:str =      "Admin"
    Databasepassword:str =  "St!ller21Admin"
    DatabaseName:str =      "testdatabase"


    Database = DATA.ConnectDatabase(DatabaseHost, DatabaseUser, Databasepassword, DatabaseName)
    
    print(Database)


    #The whole Initiation section here should probably go into some sort of initialization routine or function or something
    #define the LED characteristics used in this simulation run
    #These should be the two prime ones needed for photosynthesis
    LEDSetToAdd=LED.BuildLEDSet(1000, 696, 0, 1)
    SimulationLEDSets:list=LEDSetToAdd
    LEDSetToAdd=LED.BuildLEDSet(1000, 655, 0, 1)
    SimulationLEDSets.append(LEDSetToAdd)

    #define LED emission parameters
    #These define the emission parameters of the LED sets
    EmissionParameterToAdd=LED.BuildEmissionParameters(1, 0.5, 100)
    SimulationWaveformSettings.append(EmissionParameterToAdd)
    EmissionParameterToAdd=LED.BuildEmissionParameters(2, 0.5, 150)
    SimulationWaveformSettings.append(EmissionParameterToAdd)

    #define how long the simulation will run. (Number of steps, Width of individual step in us)
    SimulationTimeParameters:list=SIM.DefineSimulationGlobalTimeParameters(2000, 1)
    
    ConstantConditions = SIM.BakeSimulationConstConditions(SimulationLEDSets, SimulationTimeParameters, SimulationWaveformSettings)
    StartFrameConditions = SIM.BakeStartFrameConditions(2)

    StartConditions:list = [ConstantConditions, StartFrameConditions]

    SimulationResult=SIM.RunSimulation(StartConditions)
    OUT.OutputResult(SimulationResult)
    return


Main()
