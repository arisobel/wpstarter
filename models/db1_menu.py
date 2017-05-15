#menus tables
########################################

#=====================================================================================
# menu Master
#=====================================================================================
#tabela do Master do menu

db.define_table('t_menu_master',
        Field('f_menu_master', 'string', label='Menu Master'),
        Field('f_menu_master_icon', 'string', label='Icon'),
        Field('f_order_master', 'integer', label='Ordem'),
        format='%(f_menu_master)s',
        migrate=True )
        

#populate menus
if db(db.t_menu_master.id > 0).count() == 0:
    x = adminuser()
    print x
    master_menu_list_data = [{"f_menu_master": "Cadastros", "id": 1, "f_order_master": 1, "f_menu_master_icon": "calendar-plus-o"}, 
        {"f_menu_master": "Tabelas", "id": 2, "f_order_master": 2, "f_menu_master_icon": "table"}, 
        {"f_menu_master": "Registros", "id": 3, "f_order_master": 3, "f_menu_master_icon": ""}, 
        {"f_menu_master": "Relat\u00f3rios", "id": 4, "f_order_master": 4, "f_menu_master_icon": ""}, 
        {"f_menu_master": "Admin", "id": 5, "f_order_master": 5, "f_menu_master_icon": ""}]
    for m in master_menu_list_data:
        db.t_menu_master.insert(**m)

#=====================================================================================
# menu
#=====================================================================================
#tabela do menu
db.define_table('t_menu',
        Field('f_menu_master', db.t_menu_master, label='Menu Master'),
        Field('f_menu_detail','string', label='Menu Detalhe'),
        Field('f_menu_detail_icon','string', label='Icon'),
        Field('f_menu_controller','string',label='Controller'),
        Field('f_menu_function','string',label='Function'),
        Field('f_menu_order', 'integer', label='Ordem'),
        Field('f_need_sign', 'boolean', label='User Signature'),
        format='%(f_menu_detail)s',
        migrate=True )
 
#populate menus
if db(db.t_menu.id > 0).count() == 0:
    detail_menu_list_data = [{"f_menu_detail": "Users", "f_need_sign": False, "f_menu_order": None, "f_menu_controller": "adminlion", "f_menu_function": "users_manage", "f_menu_detail_icon": "", "f_menu_master": 5, "id": 1}, 
        {"f_menu_detail": "Menus", "f_need_sign": False, "f_menu_order": None, "f_menu_controller": "adminlion", "f_menu_function": "menu_manage", "f_menu_detail_icon": "", "f_menu_master": 5, "id": 2}, 
        {"f_menu_detail": "Produtos", "f_need_sign": False, "f_menu_order": 3, "f_menu_controller": "produtos", "f_menu_function": "produtos_manage", "f_menu_detail_icon": "cubes", "f_menu_master": 1, "id": 3},
        {"f_menu_detail": "Clientes", "f_need_sign": False, "f_menu_order": 1, "f_menu_controller": "client", "f_menu_function": "index", "f_menu_detail_icon": "user-plus", "f_menu_master": 1, "id": 4},
        {"f_menu_detail": "Eventos", "f_need_sign": False, "f_menu_order": 2, "f_menu_controller": "events", "f_menu_function": "index", "f_menu_detail_icon": "bullhorn", "f_menu_master": 1, "id": 5}, 
        {"f_menu_detail": "Venda", "f_need_sign": False, "f_menu_order": None, "f_menu_controller": "vendas", "f_menu_function": "vendas_manage", "f_menu_detail_icon": "", "f_menu_master": 3, "id": 6},
        {"f_menu_detail": "Grupos / Fun\u00e7\u00f5es", "f_need_sign": False, "f_menu_order": None, "f_menu_controller": "adminlion", "f_menu_function": "groups_manage", "f_menu_detail_icon": "", "f_menu_master": 5, "id": 7}, 
        {"f_menu_detail": "Entradas", "f_need_sign": False, "f_menu_order": None, "f_menu_controller": "entradas", "f_menu_function": "entradas_manage", "f_menu_detail_icon": "", "f_menu_master": 3, "id": 8}]

    for m in detail_menu_list_data:
        db.t_menu.insert(**m) 
        
#=====================================================================================
# Menu x Grupos
#=====================================================================================
db.define_table('t_menu_group',
        Field('f_menu', db.t_menu, label='Menu'),
        Field('f_group',db.auth_group, label='Groups'),
        migrate=True )
if db(db.t_menu_group.id > 0).count() == 0:
    
    menu_group=[{"f_group": 1, "f_menu": 2}, 
                {"f_group": 1, "f_menu": 1},
                {"f_group": 1, "f_menu": 3},
                {"f_group": 1, "f_menu": 4},
                {"f_group": 1, "f_menu": 5},
                {"f_group": 1, "f_menu": 6},
                {"f_group": 1,  "f_menu": 7},
                {"f_group": 1,  "f_menu": 8}]
         
    for m in menu_group:
        db.t_menu_group.insert(**m)
    

########################################