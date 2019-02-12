# -*- coding: utf-8 -*-
{
    'name': "JS Injector",
    'summary': """It implement JS to user as per group""",
    'description': """

=======================

This module use for impliment the javascript , whatever javascript enter by the admin for the group or
assign to the group , the javascript impliment to the user of the group . When the user login , the
javascript apply to the user.
    """,
    'author': "Debasish Dash",
    'website': "http://www.debweb.com",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base','web'],
    'data': [
        'view/js_injector_view.xml',
        'view/res_users_view.xml',
        'view/js_injector.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
        ],
    'license': 'LGPL-3',
    'installable':True,
    'auto_install':False,
}
