import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


file = pd.read_excel(r'C:\mysql_dump\ABC_february.xls')
Quarters = file.id_tov_cl

A = file.BaseSum[file.ABC == "A"]
A.index = range(len(Quarters))
B = file.BaseSum[file.ABC == "B"]
B.index = range(len(Quarters))
C = file.BaseSum[file.ABC == "C"]
C.index = range(len(Quarters))


DataQ1 = A[0] + B[0] + C[0]
DataQ2 = A[1] + B[1] + C[1]
DataQ3 = A[2] + B[2] + C[2]
DataToatal = DataQ1+DataQ2+DataQ3

Commerce = [DataQ1/DataToatal, DataQ2/DataToatal, DataQ3/DataToatal]
labels = Quarters

plt.pie(x = Commerce,
        labels=labels,
        autopct='%.1f%%',
        colors = np.array(['#332DF1','#2F8177','#A21B63','#22BB99']),
        radius= 1.2,
        shadow= True,
        startangle = 0,
        counterclock= False,
        wedgeprops = {'linewidth': 1.5, 'edgecolor':'green'},
        textprops = {'fontsize':20, 'color':'black'},
       )

plt.title("ABC")

plt.show()