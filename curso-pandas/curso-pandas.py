import pandas as pd

#para ver todas as colunas no print
pd.set_option('display.max_columns',None)
#criando um dataframe com dicionário
vendas = {"produtos":['arroz','feijão'],
          'preço':[500,400],
          'quantidade':[50,60]}
#dataFrame é uma tabela no python tem 2 jeitos de criar
#1. criando dataframe vazio
tabela_vazia = pd.DataFrame()

#2. criando dataframe a partir de um dicioário
tabela_vendas = pd.DataFrame(vendas)


#importando arquivos e base de dados
tabela = pd.read_excel('Vendas.xlsx')

#resumo de visualizações simples e úteis
#1. head(x) x = quantas linhas quer ver
tabela.head(10)

#2. shape = mostra o número de linhas e colunas
tabela.shape

#3. describe = faz uma análise da tabela
tabela.describe()

#observação um dataframe é uma tabela do pandas e cada coluna é uma serie. quando tem 2 series é uma tabela do pandas

#pegar colunas 
#serie
produtos = tabela['Produto']

#tabela
tabela_produtos = tabela[['ID Loja','Produto']]



#pegar uma linha
tabela.loc[0]

#pegar mais de uma linha
tabela.loc[0:5]

#pegar linhas com uma condição
tabela.loc[tabela['ID Loja'] == 'Iguatemi Esplanada']

#pegar linhas com colunas específicas 
tabela.loc[tabela['ID Loja'] == 'Iguatemi Esplanada',['ID Loja','Produto','Valor Final']]

#pegar um valor específico
tabela.loc[1,'Produto']

#criar colunas
#1. a partir de uma coluna existente
tabela['comissão'] = tabela['Valor Final'] * 0.05

#2. criar uma coluna com um valor padrão
tabela.loc[:,'imposto'] = 0

#adicionar linhas
tabela_dezembro = pd.read_excel('Vendas - Dez.xlsx')
#tabela = pd.concat([tabela,tabela_dezembro],ignore_index=True)

#excluir linha e coluna
#1. coluna
tabela = tabela.drop('imposto',axis=1)
#obs axis 0 = linha axis 1 = coluna
#linha 
tabela = tabela.drop(0,axis=0)

#excluir linhas e colunas completamente vazias
#1 linhas 
tabela = tabela.dropna(how='all')

#2. coluna
tabela = tabela.dropna(how='all',axis=1)

#excluir linhas com pelo menos 1 valor vazio
tabela = tabela.dropna()

#preencher os valores vazios
tabela['comissão'] = tabela['comissão'].fillna(tabela['comissão'].mean())

#preencher com o último valor
tabela = tabela.ffill()

#value conts
tabela_contada = tabela['ID Loja'].value_counts()

#groupby
tabela_faturamento = tabela[['ID Loja','Valor Final']].groupby('ID Loja').sum()

#mesclar 2 dataframes em um,obs ele vai procurar informações em outro dataframe

tabela_gerentes = pd.read_excel('Gerentes.xlsx')
tabela = tabela.merge(tabela_gerentes)


