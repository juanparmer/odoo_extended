# -*- coding: utf-8 -*-
{
    'name': "Electronic invoicing for Colombia",

    'summary': """
        Colombia - E-invoicing""",

    'description': """
        E-invoice implementation
    """,

    'author': "aamm solutions",
    'website': "http://www.aammsolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Localization',
    'version': '12.1',

    # any module necessary for this one to work correctly
    'depends': ['l10n_co', 'report_xml'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'templates/account_invoice_template.xml',
        'reports/account_invoice_report.xml',
        'views/account_invoice_view.xml',
        'views/res_partner_view.xml',
        'views/res_company_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
