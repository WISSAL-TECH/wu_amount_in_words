# -*- coding: utf-8 -*-

{
    'name': 'Amount In Words',
    'summary': 'Application to display amount in word and print in report',
    'version': '15.0.1.0.0',
    'author':'WAMANU',
    'maintainer': 'WAMANU',
    'website': 'http://www.wamanu.com',
    'depends': ['sale_management','purchase',],
    'data': [
        #'report/header_footer_inherit.xml',
        'report/sale_order_report.xml',
        'report/purchase_order_report.xml',
        'report/account_invoice_report.xml',
        'views/amount_word_view.xml',
        'views/res_company.xml',
        'views/res_partner.xml',
        'security/ir.model.access.csv',
    ],
    'assets': {
        'web.assets_backend' : [
            'wu_amount_in_words/static/src/css/style.css',
        ],
    },
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'images': ['static/description/poster_image.png'],
}
