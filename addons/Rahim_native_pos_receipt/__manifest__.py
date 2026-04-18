{
    'name': 'Rahim Custom Receipt with Table Layout',
    'version': '19.0.1.0.0',
    'category': 'Point of Sale',
    'summary': 'Custom receipt template with table layout for POS in Odoo 19',
    'author': 'Native Innovations',
    'website': 'https://yourwebsite.com',
    'depends': ['point_of_sale'],
    'license': 'OPL-1',

    'assets': {
        'point_of_sale._assets_pos': [
            'Rahim_native_pos_receipt/static/src/xml/OrderReceipt.xml',
            # 'native_pos_receipt/static/src/js/OrderReceipt.js',
            
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}

