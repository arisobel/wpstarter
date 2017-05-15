# -*- coding: utf-8 -*-

#########################################################################
# Customize your APP title, subtitle and menus here
#########################################################################

response.logo_mini = IMG(_src=URL('static', 'images/favicon.png'), _alt=myconf.get('app.company'), _width="30px")

# response.logo = IMG(_src=URL('static', 'images/favicon.png'), _alt=myconf.get('app.company'), _width="180px")
# response.logo = SPAN('web', B(2), 'py', XML('&trade;&nbsp;'))
response.logo = myconf.get('app.abbreviation')

# default page title that appears in browser tabs and bookmarks
response.title = '%s: %s %s' % (
    myconf.get('app.abbreviation'),
    request.controller.replace('_', ' ').title(),
    request.function.replace('_', ' ').title()
)

response.subtitle = ''

# default view title that appears at top of default layout content section
response.view_title = '%s %s' % (
    request.controller.replace('_', ' ').title(),
    request.function.replace('_', ' ').title()
)

# read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = myconf.get('app.author')
response.meta.description = myconf.get('app.description')
response.meta.keywords = myconf.get('app.keywords')
response.meta.generator = myconf.get('app.generator')

response.company = myconf.get('app.company')
response.version = myconf.get('app.version')

# your http://google.com/analytics id
response.google_analytics_id = None

#====================================================================
#novo menu - 26/12/2013


from collections import defaultdict
#carrega grupos pertencentes a esse user - funcao lista_grupos() em 0.py
list_groups = list_groups()
#response.flash = lista_grupos
#carrega o menu master numa vari[avel, pra nao precisar ficar acessando o BD toda hora
master = db().select(db.t_menu_master.ALL,orderby=db.t_menu_master.f_order_master)
#carrega to tabea do menu mua variável, contendo todos os dados para montagem do menu
detalhes = db().select(db.t_menu.ALL)
#flitra os itens de menu fazendo join com a tabela t_menu_grupo - e flitrando com as que pertencem aos
#gurpos do usuário logado = lista_grupos
menu_detalhe = db(db.t_menu_group.f_group.belongs(list_groups)).select(db.t_menu.f_menu_master,
   db.t_menu.id,
        join=db.t_menu_group.on(db.t_menu_group.f_menu==db.t_menu.id),
        groupby=db.t_menu.id,
        orderby=db.t_menu.f_menu_order

                                                                       )
#atribui a variável Menu à um defaultlist - que é um dict que possuiu listas incrementáveis -
#formando o Menu Master e Details
menu = defaultdict(list)
menu_new = dict()

#itera sobre os tens de menu flitrados já pelos grupos do usuário detro da variável Menu
for row in menu_detalhe:
    if int(row.id) not in menu[row.f_menu_master]:
        menu[row.f_menu_master].append(int(row.id))
 
''' 
for row in menu_detalhe:
    if row.f_menu_master not in menu_new.keys():
        menu_new[row.f_menu_master] = [row.id]
    else:
        menu_new[row.f_menu_master].append(int(row.id))
        
#print 'menu_new =>', menu_new, '\n'
'''        
        
for row in menu_detalhe:
    if int(row.id) not in menu[row.f_menu_master]:
        menu[row.f_menu_master].append(int(row.id))
        
#response.menu=menu_new
#response.flash = menu

#monta o menu propriamente dito em ciam da variavel que já possui a estrutura do master detail
#onde o m é o Id do Master e l a lista dos detalhes

response.menu = []
for m, l in menu.iteritems():
    master = db.t_menu_master[m]
    item_master = {'nome_master':master['f_menu_master'], 'iconemaster': master['f_menu_master_icon']}
    internal_list=[]
    for x in l:
        menu_det = db.t_menu[x]
        item = {'nome':menu_det['f_menu_detail'],'url': URL(db.t_menu[x]['f_menu_controller'],menu_det['f_menu_function']), 'icon':menu_det['f_menu_detail_icon']}
        internal_list.append(item)
    response.menu.append([item_master,internal_list])

'''
for m in response.menu:
    print 'm=>', m, '\n'
    print 'm=>itens', m[0]['nome_master'], m[0]['iconemaster'], '\n\n'
'''

    
#print  XML(BEAUTIFY(response.menu))
#print  response.menu
#print '\n'
#print  menu

