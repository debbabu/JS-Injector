from odoo import models,fields

class res_groups(models.Model):
    _inherit = "res.groups"

    js_injector = fields.Many2many('js.injector', 'groups_group_js', 'group_id', 'group_js_id', string='JS Injector' )
