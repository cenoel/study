# -*- coding: utf-8 -*-
{
    'name': "START",
    'icon': '/start/static/src/img/start.png',
    'sequence': -10,
    'summary': """""",
    'description': """""",
    'author': "ALLCODETRUE",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'base',
        'contacts',
        'maintenance',
        'product',
        'stock',
        'purchase'
    ],
    'data': [
        # 'security/ir.model.access.csv',
        'data/start_res_config_settings_data.xml',
        'data/start_type_partner_data.xml',
        'views/start_maintenance_equipment_view.xml',
        'views/start_res_partner_view.xml',
        'views/start_menu_view.xml',
    ],
}

