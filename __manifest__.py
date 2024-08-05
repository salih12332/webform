# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'WebForm n',
    'category': 'Hidden',
    'sequence': 9,
    'summary': 'S',
    'depends': ['website'],
    'website': '',
    'description': """
Hardware Poxy
=============

This module allows you to remotely use peripherals connected to this server.

This modules only contains the enabling framework. The actual devices drivers
are found in other modules that must be installed separately.

""",


    'data': [
        'views/beauty.xml',
        'views/beautytemp.xml',
        'views/menu.xml',
        
        
      ],   
    'installable': True,
    'license': 'LGPL-3',
}
