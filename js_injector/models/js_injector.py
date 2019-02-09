# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
from odoo import fields
from odoo import models,api
# import json

_logger = logging.getLogger(__name__)

class JSInjector(models.Model):
    _name = "js.injector"
    _description = "JS Injector"

    name = fields.Char('Purpose', required=True, select=1)
    js = fields.Text('Javascript',required=False, index=False,store=True)
    active = fields.Boolean('Active')
    groups = fields.Many2many('res.groups', 'groups_group_js', 'group_js_id', 'group_id', track_visibility='onchange' , string='Groups')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'The name of the Javascript available , You must change your javascript name or check the javascript code may available !!!')
    ]

    @api.model
    def get_current_user_js(self):
        user_group_ids = self.env.user.groups_id
        user_group_js_ids = []
        for user_group in user_group_ids:
            user_group_js_ids += user_group["js_injector"]
        output_javascripts = []
        for user_group_js_item in user_group_js_ids:
            output_javascripts.append(user_group_js_item['js'])
        return ";".join(output_javascripts);
