from sklearn.preprocessing import LabelEncoder
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

tabela = pd.read_csv("clientes.csv")#importando a base de dados

# print(tabela.info())
# print(tabela.columns)

# vai transformar as colunasde texto em números, ex: profissoes vai sair de cientistas, professor, mecanico, etc para 0, 1, 2, etc
codificador = LabelEncoder()

# só não aplicamos na coluna de score_credito que é o nosso objetivo
for coluna in tabela.columns:
    if tabela[coluna].dtype == "object" and coluna != "score_credito":
        tabela[coluna] = codificador.fit_transform(tabela[coluna])


# verificando se realmente todas as colunas foram modificadas
for coluna in tabela.columns:
    if tabela[coluna].dtype == "object" and coluna != "score_credito":
        print(coluna)

    #print(tabela)

# escolhendo quais colunas vamos usar para treinar o modelo
# 'y' é a coluna que queremos que o modelo calcule
# 'x' vai todas as colunas que vamos usar para prover o score de credito, não vamos usar a coluna id_cliente porque ela é um número qualquer que não ajuda a previsão
x = tabela.drop(["score_credito", "id_cliente"], axis=1)
y = tabela["score_credito"]

# separamos os dados em treino e teste. Treino vamos dar para os modelos aprenderem e teste vamos usar para ver se o modelo aprendeu corretamente
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3, random_state=1)

modelo_arvore = RandomForestClassifier() # modelo arvore de decisão
modelo_knn = KNeighborsClassifier() # modelo do KNN(vizinhos mais próximos)

# treinando os modelos
modelo_arvore.fit(x_treino, y_treino)
modelo_knn.fit(x_treino, y_treino)

# se o nosso modelo chutasse tudo "Standard", qual seria a acurácia do modelo?
contagem_scores = tabela["score_credito"].value_counts()
print("Resultado de Standard")
print(contagem_scores["Standard"] / sum(contagem_scores))

# calculando as previsões
previsao_arvore = modelo_arvore.predict(x_teste)
previsao_knn = modelo_knn.predict(x_teste.to_numpy())

# comparamos as previsões com o y_teste
# esse score queremos o maior (maior acurácia, mas tambem tem que ser maior que o chute de tudo Standard)
print("Comparações de previsoes")
print(accuracy_score(y_teste, previsao_arvore))
print(accuracy_score(y_teste, previsao_knn))

# Quais as características mais importantes para definir o score de credito?
colunas = list(x_teste.columns)
importancia = pd.DataFrame(index=colunas, data=modelo_arvore.feature_importances_)
importancia = importancia * 100

print(importancia)

