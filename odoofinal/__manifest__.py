# -*- coding: utf-8 -*-
{
    'name': "odoofinal",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/odoofinal_security.xml',
        'security/ir.model.access.csv',
        'report/odoofinal_restaurante_report.xml',
        'report/odoofinal_encargado_report.xml',
        'report/odoofinal_empleado_report.xml',
        'report/odoofinal_mesa_report.xml',


        'views/views.xml',
        'views/views1.xml',
        'views/views2.xml',
        'views/views3.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
