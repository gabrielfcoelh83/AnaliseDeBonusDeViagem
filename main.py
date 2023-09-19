import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = 'AC668ee88aa9f90ec65c2cee735bf13884'
# Your Auth Token from twilio.com/console
auth_token = '35240106b604b6ae28f748ca63e5a929'
client = Client(account_sid, auth_token)


# Passo a passo de solução

# Abrir os  6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'junho', 'maio']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            from_='+16365870910',
            to='+5551991040570',
            body=f'No mês {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}'
        )

        print(message.sid)


# Para cada arquivo:

# Verificar se algum valor na coluna vendas daquele arquivo é maior que 55.000

# Se for maior que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor

# Caso não seja maior do que 55.000 não quero fazer nada
