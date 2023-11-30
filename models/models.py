# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class product_group(models.Model):
#     _name = 'product_group.product_group'
#     _description = 'product_group.product_group'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class VcsProductGroup(models.Model):
    _name = 'vcs_product_group.vcs_product_group'
    _description = 'Product Group'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(size=255,string="Name", tracking=True, required=True)
    code = fields.Char(size=50,string="Code", tracking=True, required=True)
    description = fields.Text(string="Description", tracking=True)
    is_active = fields.Boolean(string="Is Active", tracking=True, default=False)
    
    _sql_constraints = [
        ('uniq_product_group_code', 'unique(code)', "A stuff already exists with this name . Stuff's name must be unique!"),
    ]
    
class VcsProductUnit(models.Model):
    _name = 'vcs_product_unit.vcs_product_unit'
    _description = 'Product Unit'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(size=255,string="Name", tracking=True, required=True)
    code = fields.Char(size=50,string="Code", tracking=True, required=True)
    description = fields.Text(string="Description", tracking=True)
    is_active = fields.Boolean(string="Is Active", tracking=True, default=False)
    
    _sql_constraints = [
        ('uniq_unit_code', 'unique(code)', "A stuff already exists with this name . Stuff's name must be unique!"),
    ]
