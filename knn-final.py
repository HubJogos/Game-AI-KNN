# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import joblib

from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing, model_selection, neighbors
from sklearn.preprocessing import StandardScaler


from sklearn.model_selection import train_test_split
from scipy.spatial import distance #só pra testar a distancia

# %%
mapa = pd.read_csv("data-base.csv") #LENDO O DATASET USANDO O PANDAS
mapa.columns


# %%
mapa['fun'].value_counts()

# %%
mapa['fun'].describe()

# %%
mapa.loc[mapa['fun']< 2 , 'fun'] = 0    #BASEADO NA MEDIANA ACIMA, SE A NOTA DADA AO FUN FOR MENOR QUE 2, ENTÃO RECEBE 0
mapa.loc[mapa['fun']>= 2 ,'fun'] = 1    #SE NÃO, RECEBE 1

mapa["fun"].unique()

# %%
#test_column = mapa[["timeSpent","percentKills","mapSize","enemyAmount","enemyDensity","interactionAmount","conversationMaterial",
#                    "difficulty","percentItems","totalLifeLost","seed", "fun"]]
#conjunto de dados 1

# %%
test_2 = mapa[["totalLifeLost","timeSpent","playthroughs", "deaths", "steps","seed", "fun"]]

# %%
sns.heatmap(test_2.corr(), annot=False, vmin=-1, vmax = 1)
plt.show()

# %%
test_column = mapa[["timeSpent","percentKills","mapSize","enemyAmount","enemyDensity","interactionAmount","conversationMaterial",
                    "difficulty","percentItems","totalLifeLost","seed", "fun"]]

# %%
sns.heatmap(test_column.corr(), annot=False, vmin=-1, vmax = 1)
plt.show()

# %%
#SÓ TESTANDO O PLOT DOS MAPAS, CRIAREI NOVOS DEPOIS

# %%
seed = (test_column['seed'])
X = (test_column.drop(['seed','fun'],1)) #PARA O TESTES E TESTES, USEI TODAS A COLUNAS MENOS A FUN
y = (test_column['fun'])          #PARA O TARGET, SOMENTE A COLUNA FUN FOI USADA


# %%
X


# %%
X_train,X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size = 0.2, random_state = 0,shuffle=False) 
#SEPARANDO O DATASET EM TREINO E TESTE, ONDE 20% DO DATASET REPRESENTAM O TESTES, E 80% PARA TREINO

# %%
mapa[["timeSpent","percentKills","mapSize","enemyAmount","enemyDensity","interactionAmount","conversationMaterial",
                    "difficulty","percentItems","totalLifeLost","seed", "fun"]].iloc[[148]]


# %%
X_test

# %%
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)    #DANDO UM FIT NOS DADOS DE TREINO E TESTE
X_test = sc_X.transform(X_test)

# %%
X_test

# %%
clf = neighbors.KNeighborsClassifier(n_neighbors = 3, metric = 'euclidean') #APLICANDO O KNN

# %%
clf.fit(X_train, y_train)

# %%
accuracy = clf.score(X_test, y_test) #ACURÁCIA DO MODELO, ATUALMENTE EM 72%
accuracy


# %%
test_column.head(4) #SÓ SERVE DE AUXILIO PARA EU VER QUAIS ENTRADAS USAR

# %%
exemplo = np.array([81.96,0.09090909,4,1,1,2,4,2,0.3333333,25]) #ENTRADA TESTE49.14	0.4666667	2	2	2	3	4	2	0.375	15
exemplo = exemplo.reshape(1,-1)     # COLOCANDO TODOS OS VALORES ENTRE -1 E 149.14,0.4666667,2,2,2,3,4,2,0.375,15
exemplo = sc_X.transform(exemplo)   # TRANSFORMANDO TODOS ESSES DADOS PARA UMA MESMA MÉTRICA
predict = clf.kneighbors(exemplo, 3)


#exemplo = np.array([41.3,0.3571429,3,3,4,4,3,3,0.2857143,20])    

print("Indices dos mapas: ", predict)
#print(type(predict.tolist())) #CASO SEJA NECESSÁRIO TROCAR O TIPO DESSA CARALHA
 



# %%
joblib.dump(clf,"knnmodelTESTE.joblib")

# %%
#PARA REFERENCIA!!

#def seedMapas():
  #  Mapas=[]
#    for i in predict:
#        for j in i:
#            Mapas.append(j)  
#    index_mapas = X_train.iloc[Mapas]
#    final_result = index_mapas.merge(seed, left_index=True, right_index=True)
#    return final_result['seed']

#print(seedMapas())


