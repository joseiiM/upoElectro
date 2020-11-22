# -*- coding: utf-8 -*-
{
    'name': "upoelectro",

    'summary': """upoElectro""",

    'description': """UpoElectro module""",

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/clientes_view.xml',
        'views/pagos_view.xml',
        'views/pedidos_view.xml',
        'views/almacenes_view.xml',
        'views/articulos_view.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
