{
    'name' : 'Real -estate',
    'version' : '1.2',
    'summary': 'Advertising real estate property',
    'sequence': 10,
    'depends':['purchase','mail'],

    'data': [
        'security/ir.model.access.csv',       
        'views/views.xml',
        'views/property_type.xml',
    ],
}




