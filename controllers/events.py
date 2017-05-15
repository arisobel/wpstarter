# coding: utf8
# tente algo como
def index():

    form = SQLFORM.grid(db.EVENTOS,
    fields=[db.EVENTOS.NOME_EVENT,
    	        db.EVENTOS.TAXA_DOLAR,
                db.EVENTOS.ATUAL
                ],

    buttons_placement='left',
    showbuttontext=False, # Exibe os botões
    _class='web2py_grid',
    exportclasses=dict(xml=False,html=False,csv_with_hidden_cols=False,json=False,tsv_with_hidden_cols=False),
    )
    return dict(form=form)
