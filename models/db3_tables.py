# coding: utf8
########################################

import datetime

########################################

########################################

db.define_table('CLIENTES',
   Field('CODIGO' ,'id'),
   Field('DATA', 'date', label='Data de  Resgistro', default=datetime.datetime.now()),
   Field('NOME', 'string', label='Nome'),
   Field('ENDERECO', 'string', label='Endereço'),
   Field('BAIRRO', 'string'),
   Field('CIDADE', 'string'),
   Field('ESTADO', 'string', requires=IS_IN_SET(dal_list_states_br)),
   Field('CEP', 'string'),
   Field('TELEFONE1', 'string'),
   Field('TELEFONE2', 'string'),
   Field('TELEFONE3', 'string'),
   Field('BAIRRO', 'string'),
   Field('BAIRRO', 'string'),
   Field('BAIRRO', 'string'),
   Field('CNPJ', 'string'),
   Field('INSCRICAO', 'string'),
   Field('RG1', 'string'),
   Field('CPF1', 'string'),
   Field('OBS', 'string'),
   Field('EMAIL', 'string'),
   format='%(NOME)s',
   migrate=False )
   
   
   
############################################
#   FORNECEDORES
#   CODFORNEC  NOMEFRN   

db.define_table('FORNECEDORES',
   Field('CODFORNEC' ,'id'),
   Field('NOMEFRN', 'string', label='Fornecedor'),      
   format='%(NOMEFRN)s',
   migrate=False )      

      
#############################################
# PRODUTOS 
# CODIGO  NOME    NOME_HEB   PRECO  ESTOQUE  ENTRADA  CONJUNTO     CODFORNEC  FORNECEDOR  FORNEC  NOMEFRN  

db.define_table('PRODUTOS',
   Field('CODIGO' ,'id'),
   Field('NOME', 'string', label='Produto'),   
   Field('NOME_HEB', 'string', label='Produto Hebraico'),      
   Field('PRECO', 'string', label='Preço'),
   Field('ESTOQUE', 'integer'),
   Field('ENTRADA', 'integer'),
   Field('CONJUNTO', 'string', label='Produto'),
   Field('CODFORNEC', db.FORNECEDORES),
   Field('FORNEC', 'string'),
   Field('NOMEFRN', 'string'),
   format='%(NOME)s',
   migrate=False )

#############################################
# EVENTOS  qual feira se refere
#ID_EVENTO  NOME_EVENT  TAXA_DOLAR  
   
db.define_table('EVENTOS',
   Field('ID_EVENTO' ,'id'),
   Field('NOME_EVENT', 'string', label='Produto'),  
   Field('TAXA_DOLAR', 'double', label='Taxa Dolar'),    
   Field('ATUAL', 'boolean', label='Atual'),    
   format='%(NOME_EVENT)s',
   migrate=False )         
   
#############################################
# VENDAS
# ORDEM  DT_SAIDA             CLIENTE   JUROS  VAL_JUROS  DESCONTO  VAL_DESCON  VAL_TOTAL  VAL_MERC  VALPAGO  EVENTO  
db.define_table('SAIDA',
   Field('ORDEM' ,'id'),
   Field('DT_SAIDA', 'date', label='Data da Venda'),   
   Field('CLIENTE', db.CLIENTES, label='Cliente'),      
   Field('JUROS', 'double', label='Preço'),
   Field('VAL_JUROS', 'double', label='Valor dos Juros'),
   Field('DESCONTO', 'double', label='Desconto'),
   Field('VAL_DESCON', 'double', label='Valor do Desconto'),
   Field('VAL_TOTAL', 'double', label='Valor Total'),
   Field('VAL_MERC', 'double', label='Valor da Mercadoria'),
   Field('VALPAGO', 'double', label='Valor Pago'),
   Field('EVENTO', db.EVENTOS),
   migrate=False )
   
   
#==========================================
#
#ORDEM, POSICAO, DT_SAIDA, PRODUTO, NOME, PRECO_VEND, QUANTIDADE, VAL_TOTAL  
db.define_table('ITENS_SAIDA',
   Field('ORDEM' ,'integer'),
   Field('POSICAO' , 'integer'),
   Field('DT_SAIDA' ,'date'),
   Field('PRODUTO' ,db.PRODUTOS),
   Field('NOME' ,'string'),
   Field('PRECO_VEND' ,'double'),
   Field('QUANTIDADE' ,'integer'),
   Field('VAL_TOTAL' ,compute=lambda r: r['PRECO_VEND']*r['QUANTIDADE']),
   migrate=False )