# -*- coding: utf-8 -*-
{
    'name': "Base Vat Co",

    'summary': "VAT validation for Partner's VAT numbers.",

    'description': "",

    'author': "Avancys",
    'contributors': "Juan Arcos https://github.com/juanparmer",
    'website': "http://www.avancys.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '12.1',

    # any module necessary for this one to work correctly
    'depends': ['base_vat'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
