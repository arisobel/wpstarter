# -*- coding: utf-8 -*-

def index():
    

    links = [lambda row: A(XML("<i class='icon-shopping-cart'></i>"),_href=URL("vendas","add_new",args=[row.id]), _class='btn')]
    form = SQLFORM.grid(db.CLIENTES,
    links=links,
    buttons_placement = 'left',
    deletable=False,
    fields=[db.CLIENTES.NOME,
    	        db.CLIENTES.TELEFONE1,
    	        db.CLIENTES.EMAIL],
    orderby = db.CLIENTES.NOME,
    showbuttontext=False, # Exibe os botões
    _class='web2py_grid',
    exportclasses=dict(xml=False,html=False,csv_with_hidden_cols=False,json=False,tsv_with_hidden_cols=False),
    )
        
    for c in form.elements('select'): c.add_class('select2')
    
    return dict(form=form)

