# Computation of total displacement
# Input Files:
#   - LA_Endo_A_dtot.vtp    File containing incremental displacement
# Output File:
#   - LA_Endo_A_dtot.vtp    File containing total displacement


# Import the simple Module from the Paraview
from paraview.simple import *
import numpy as np

# Directory definition
dir = 'D:/Politecnico/Mathematical Engineering - MCS/Tesi/Simulations/Fibre_Files/LA_Endo/5/'
filenamevtp = dir + 'AF2_dtot.vtp'

# Open Source Files
gALEvtp = XMLPolyDataReader(FileName=filenamevtp)

ii = 0
while ii < 99:
    if ii < 9:
        str1 = 'd000' + str(ii) + '+d000' + str(ii+1)
        str2 = 'd000' + str(ii+1)
    if ii == 9:
        str1 = 'd0009+d0010'
        str2 = 'd0010'
    if ii > 9:
        str1 = 'd00' + str(ii) + '+d00' + str(ii+1)
        str2 = 'd00' + str(ii+1)
        
    if ii == 0:
        calculator1 = Calculator(Input=gALEvtp)
    else:
        calculator1 = Calculator(Input=calculator2)
    calculator1.ResultArrayName = str2
    calculator1.Function = str1
    calculator2 = calculator1
    
    ii = ii + 1
    
SaveData(filenamevtp, proxy = calculator1) 