import matplotlib.pyplot as plt
import IDs as ID

def OutputResult(SimulationData:list):
    plt.plot(CreateLightInputData(SimulationData))
    plt.show()
    return

def CreateLightInputData(SimulationData:list):
    Runner:int = 0
    LightInputResult:list = []
    while (Runner) < len(SimulationData[ID.MAIN.IDFrameConditions]):
        LightInputResult.append(SimulationData[ID.MAIN.IDFrameConditions][Runner][ID.FRAME.IDLightEmission])
        Runner += 1
    return LightInputResult

