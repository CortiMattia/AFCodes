import pandas as pd

path = "D:\\AF2Particles\\"
filedel = path + "ParticlesToDelete.csv"
fdel = pd.read_csv(filedel, sep=',')
for jj in range(2000, 3001):
    fileinp = path + "AF2Particles_" + str(jj) + ".csv"

    finp = pd.read_csv(fileinp, sep=',')
    #finp.drop(['h', 'Vorticity', 'Rotation'], axis=1,inplace=True)
    cond = finp['ParticleId'].isin(fdel['ParticleId'])
    finp.drop(finp[cond].index, inplace=True)

    finp.to_csv(fileinp, index=False, float_format='%.5f')
    # print('Iteration:', jj)

#path = "D:\\AF1Particles"
#filedel = path + "ParticlesToDelete.csv"
#fdel = pd.read_csv(filedel, sep=',')
#pathout = "G:\\TesiMattia\\PH1\\"
#for jj in range(0, 3001):
#    fileinp = path + "AF1Particles_" + str(jj) + ".csv"
#    finp = pd.read_csv(fileinp, sep=',')
#    cond = (finp['InjectionStepId'] != jj)
#    finp.drop(finp[cond].index, inplace=True)
#    if jj == 0 :
#        app = finp.groupby('ParticleSourceId').size()
#    else:
#        app = finp.groupby('ParticleSourceId').size() + app
#    print('Iteration:', jj, app)

