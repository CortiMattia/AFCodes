# Computation of gALE function
# Input Files:
#   - hALE.csv              File containing function hALE values at any time
#   - LA_Endo_N_dinc.vtp    File containing function fALE values at any point
# Output File:
#   - LA_Endo_A_dinc.vtp    File containing function gALE values at any point and time


# Import the simple Module from the Paraview
from paraview.simple import *

# Import numpy
import numpy as np

# Directory definition
dir = 'D:/Politecnico/Mathematical Engineering - MCS/Tesi/Simulations/Fibre_Files/LA_Endo/5/'
filenamevtp = dir + 'AF2_dinc.vtp'
filenamecsv = dir + 'hALE.csv'

# Open Source Files
lA_Endo_A_gALEvtp = XMLPolyDataReader(FileName=filenamevtp)

hALE = np.genfromtxt(filenamecsv, dtype=float, names=True, delimiter=',', autostrip=True)

# Loop over the csv file columns
for name in hALE.dtype.names:
    array = hALE[name]
    cont = 0
    
    # Control of the Correct Column Finding
    if name == 'hALE':
        namesarray = np.array('fALE')
        for ii in array:
        
            # Output Function Name Definition
            if cont > 999:
                strcalname = 'd' + str(cont)
                if cont > 1000:
                    stwrapname = 'd' + str(cont-1)
                if cont == 1000:
                    stwrapname = 'd0999'
            if cont > 99 and cont < 1000:
                strcalname = 'd0' + str(cont)
                stwrapname = 'd0' + str(cont-1)
                if cont > 100:
                    stwrapname = 'd0' + str(cont-1)
                if cont == 100:
                    stwrapname = 'd0099'
            if cont > 9 and cont < 100:
                strcalname = 'd00' + str(cont)
                if cont > 10:
                    stwrapname = 'd00' + str(cont-1)
                if cont == 10:
                    stwrapname = 'd0009'
            if cont < 10:
                strcalname = 'd000' + str(cont)
                stwrapname = 'd000' + str(cont-1)
            
            # Move surface to compute the flux
            if cont != 0:
                warpByVector1 = WarpByVector(Input=lA_Endo_A_gALEvtp, Vectors = stwrapname)
                                
                # Normal vector field generation
                generateSurfaceNormals1 = GenerateSurfaceNormals(Input=warpByVector1)
                
                # Integrand computation
                calculator1 = Calculator(Input=generateSurfaceNormals1)
                calculator1.ResultArrayName = 'Flux'
                calculator1.Function = '100*fALE.Normals'
               
                # Integral Computation
                integrateVariables1 = IntegrateVariables(Input=calculator1)
                DataSliceFile = paraview.servermanager.Fetch(integrateVariables1)
                fluxvalue = DataSliceFile.GetPointData().GetArray('Flux').GetTuple(0)
                strcal = 'fALE*(' + str(ii) + '/' + str(fluxvalue[0]) + ')'
                print(strcal)
                
                # Calculator Operation
                calculator2 = Calculator(Input=calculator1)
                calculator2.ResultArrayName = strcalname
                calculator2.Function = strcal
            else:            
                # Normal vector field generation
                generateSurfaceNormals1 = GenerateSurfaceNormals(Input=lA_Endo_A_gALEvtp)
                
                # Integrand computation
                calculator1 = Calculator(Input=generateSurfaceNormals1)
                calculator1.ResultArrayName = 'Flux'
                calculator1.Function = '100*fALE.Normals'
               
                # Integral Computation
                integrateVariables1 = IntegrateVariables(Input=calculator1)
                DataSliceFile = paraview.servermanager.Fetch(integrateVariables1)
                fluxvalue = DataSliceFile.GetPointData().GetArray('Flux').GetTuple(0)
                strcal = 'fALE*(' + str(ii) + '/' + str(fluxvalue[0]) + ')'
                print(strcal)

                # Calculator Operation
                calculator2 = Calculator(Input=calculator1)
                calculator2.ResultArrayName = strcalname
                calculator2.Function = strcal
                
            cont = cont + 1
            namesarray = np.append(namesarray,strcalname)
            
            # Save Output File Updates 
            SaveData(filenamevtp, proxy = calculator2, PointDataArrays = namesarray)
            
            # Open Source Files
            lA_Endo_A_gALEvtp = XMLPolyDataReader(FileName=filenamevtp)