# -*- coding: utf-8 -*-
{
    'name': 'crm_project_application',
    'version': '13.0.1',
    'summary': 'crm_project_application',
    'category': 'project',
    'author': 'Magdy,TeleNoc',
    'description': """
    crm_project_application
    """,
    'depends': ['base', 'mail', 'crm'],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_project.xml',
    ]
}
