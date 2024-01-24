import pandas as pd
import plotly.express as px

tabela = pd.read_csv("cancelamentos.csv")
tabela = tabela.drop("CustomerID", axis=1)
#print(tabela)

# identificando e removendo valores
tabela = tabela.dropna()

# Com essa simples análise você já nota que temos a seguinte
# proporção na duração dos contratos:
# Anual 40,19%
# Trimestral 40,00%
# Mensal 19,75%
# print(tabela["duracao_contrato"].value_counts(normalize=True))

# Sem formatação
# print(tabela["duracao_contrato"].value_counts())

# Analisando o contrato mensal
# print(tabela.groupby("duracao_contrato").mean(numeric_only=True))
# descobrimos aqui que a média de cancelamentos é 1, ou seja, praticamente todos os contratos mensai cancelaram (ou todos)

# então descobrimos que contrato mensal é ruim, vamos tirar ele e continuar analisando
# tabela = tabela[tabela["duracao_contrato"] != "Monthly"]
# print(tabela)
# print(tabela["cancelou"].value_counts())
# print(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))

# chegamos agora em menos da metade de pessoas cancelando, mas ainda temos muitas ai, vamos continuar analisando
# print(tabela["assinatura"].value_counts(normalize=True))
# print(tabela.groupby("assinatura").mean(numeric_only=True))
# vemos que assinaturas é quase 1/3, 1/3, 1/3
# e que os cancelamentos são na média bem parecidos, então fica difícil tirar alguma conclusão da media, vamos precisar e mais a fundo.

#for coluna in tabela.columns:
#    grafico = px.histogram(tabela, x=coluna, color="cancelou", width=600)
#    grafico.show()

# com os gráficos consegue descobrir muitas coisas
# dias atraso acima de 20 dias, 100% cancela
# ligações call center acima de 5 todos cancelam

tabela = tabela[tabela["ligacoes_callcenter"] <5 ]
tabela = tabela[tabela["dias_atraso"] <= 20]
print(tabela)
print(tabela["cancelou"].value_counts())
print(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))

# resolvendo isso, já caiu para 18% de cancelamento
# é claro que 100% é utópico, mas com isso já temos as principais causas (ou talvez 3 das pricipais)
# menos forma de contrato mensal
# menos necessidade de ligações no callcenter
# menos atraso no pagamento
