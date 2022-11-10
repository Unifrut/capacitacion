# -*- coding:utf-8 -*-

{
    'name':'Biblioteca',
    'summary':"""App de pruebas Odoo""",
    'description':"""
            App diseñada como modelo de pruebas
        """,
    'author':'Unifrut',
    'website':'https://www.unifrut.com',
    'category':'Entrenamiento',
    'version':'0.1',
    'depends':['base'],
    'data':[
        'security/biblioteca_security.xml',
        'security/ir.model.access.csv',
        'views/biblioteca_menuitems.xml',
        'views/libro_views.xml',
    ],
    'demo':[
        'demo/biblioteca_demo.xml',
    ],
    'license':'OPL-1'
}