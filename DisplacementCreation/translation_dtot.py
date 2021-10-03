# Translation of the displacement field in time
# Input Files:
#   - LA_Endo_A_dtot.vtp    File containing initial displacement
# Output File:
#   - LA_Endo_A_dtot.vtp    File containing translated displacement


# Import the simple Module from the Paraview
from paraview.simple import *
import numpy as np

# Directory definition
dir = 'D:/Politecnico/Mathematical Engineering - MCS/Tesi/Simulations/Patients/Patient_7/7LAE/LeftAtriumMesh/'
filenamevtp = dir + 'LA_Endo_7_dtot2.vtp'

# Open Source Files
gALEvtp = XMLPolyDataReader(FileName=filenamevtp)

ii = 100
while ii >= 0:
    if ii == 100:
        str1 = 'd0099'
        str2 = 'tmp'
    else:
        if ii == 0:
            str1 = 'tmp'
            str2 = 'd0000'
        else:
            if ii <= 9:
                str1 = 'd000' + str(ii-1)
                str2 = 'd000' + str(ii)
            if ii == 10:
                str1 = 'd0009'
                str2 = 'd0010'
            if ii > 10:
                str1 = 'd00' + str(ii-1)
                str2 = 'd00' + str(ii)
            
    if ii == 100:
        calculator1 = Calculator(Input=gALEvtp)
    else:
        calculator1 = Calculator(Input=calculator2)
    calculator1.ResultArrayName = str2
    calculator1.Function = str1
    calculator2 = calculator1
    
    ii = ii - 1
    
SaveData(filenamevtp, proxy = calculator1) 