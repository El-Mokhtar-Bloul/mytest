# -*- coding: utf-8 -*-
{
    'name': "acpec_logement",
    'summary': """Rapports sur le logemen""",
    'description': """
        Long description of module's purpose
    """,

    'author': "ACPEC SARL",
    'website': "https://www.acpec-sarl.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale_subscription', 'account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizards/wizard_view.xml',
        'views/inherit_account_move.xml',
        'reports/report.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
     #   'demo/demo.xml',
    #],
}
