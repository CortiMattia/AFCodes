n = 502;
fileID = fopen("QVENPUL_AF1.csv");
QVENPUL2  = fscanf(fileID,"%f,%f",[2 10000])';
QVENPUL2 = [QVENPUL2; QVENPUL2; QVENPUL2; QVENPUL2; QVENPUL2; QVENPUL2; QVENPUL2(1,:)];
fileID = fclose(fileID);
QVENPUL = spline(linspace(0,6,601),QVENPUL2(:,2),linspace(0,6,3001));
% perc = QVENPUL(1:20:end,2)/max(QVENPUL(1:20:end,2));
perc = QVENPUL/7.0870e-05;
n_el = ceil((1-perc)*n)-258;
PCsElimin = array2table(zeros(14,sum(n_el))','VariableNames',{'velx','vely','velz','Vx','Vy','Vz','ParticleId','ParticleSourceId','InjectedPointId','InjectionStepId','ParticleAge','Point0','Point1','Point2'});
disp("================================================================")
disp("                   SCELTA PARTICELLE DA ELIMINARE")
disp("================================================================")
disp("ITERAZIONI: ")
for jj = 0 : 3000 %length(perc)
    disp(['- Iteration: ',num2str(jj)]);
    time = tic;
    csvname = sprintf('AF1Particles_%d.csv',int16(jj));
    fileID = fopen(csvname);
    % PCs = readtable(csvname);
    fgetl(fileID);
    C  = fscanf(fileID,"%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f",[14 Inf])';
    fclose(fileID);
    PCs = array2table(C,'VariableNames',{'velx','vely','velz','Vx','Vy','Vz','ParticleId','ParticleSourceId','InjectedPointId','InjectionStepId','ParticleAge','Point0','Point1','Point2'});
    len = size(PCs,1);
    find = 0;
    PCsel = array2table(zeros(14,n_el(jj+1))','VariableNames',{'velx','vely','velz','Vx','Vy','Vz','ParticleId','ParticleSourceId','InjectedPointId','InjectionStepId','ParticleAge','Point0','Point1','Point2'});
    buffernum = zeros(1,n_el(jj+1));
    while(find < n_el(jj+1))
        buffernumapp = sum(PCs.InjectionStepId<jj) + random('Discrete uniform',size(PCs,1)-sum(PCs.InjectionStepId<jj)-1);
        if (sum(buffernum == buffernumapp) == 0)
            buffernum(find+1) = buffernumapp;
            PCsel(find+1,:) = PCs(buffernumapp,:);
            find = find + 1;
        end
    end
    if jj == 0
        a = 1;
        b = n_el(1);
    else
        a = sum(n_el(1:jj))+1;
        b = sum(n_el(1:jj+1)); 
    end
    PCsElimin(a:b,:) = PCsel;
    toc(time)
end
writetable(PCsElimin,"ParticlesToDelete.csv");