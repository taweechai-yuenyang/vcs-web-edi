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
    _name = 'vcs_web_edi.vcs_product_group'
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
    _name = 'vcs_web_edi.vcs_product_unit'
    _description = 'Product Unit'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(size=255,string="Name", tracking=True, required=True)
    code = fields.Char(size=50,string="Code", tracking=True, required=True)
    description = fields.Text(string="Description", tracking=True)
    is_active = fields.Boolean(string="Is Active", tracking=True, default=False)
    
    _sql_constraints = [
        ('uniq_unit_code', 'unique(code)', "A stuff already exists with this name . Stuff's name must be unique!"),
    ]
    
class VcsProductType(models.Model):
    _name = 'vcs_web_edi.vcs_product_type'
    _description = 'Product Type'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(size=255,string="Name", tracking=True, required=True)
    code = fields.Char(size=50,string="Code", tracking=True, required=True)
    description = fields.Text(string="Description", tracking=True)
    is_active = fields.Boolean(string="Is Active", tracking=True, default=False)
    
    _sql_constraints = [
        ('uniq_product_type', 'unique(code)', "A stuff already exists with this name . Stuff's name must be unique!"),
    ]
    
class VcsReferenceType(models.Model):
    _name = 'vcs_web_edi.vcs_ref_type'
    _description = 'Reference Type'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(size=255,string="Name", tracking=True, required=True)
    code = fields.Char(size=50,string="Code", tracking=True, required=True)
    description = fields.Text(string="Description", tracking=True)
    is_active = fields.Boolean(string="Is Active", tracking=True, default=False)
    
    _sql_constraints = [
        ('uniq_reference_type', 'unique(code)', "A stuff already exists with this name . Stuff's name must be unique!"),
    ]
    
class VcsWhs(models.Model):
    _name = 'vcs_web_edi.vcs_whs'
    _description = 'Whs'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(size=255,string="Name", tracking=True, required=True)
    code = fields.Char(size=50,string="Code", tracking=True, required=True)
    description = fields.Text(string="Description", tracking=True)
    is_active = fields.Boolean(string="Is Active", tracking=True, default=False)
    
    _sql_constraints = [
        ('uniq_whs_code', 'unique(code)', "A stuff already exists with this name . Stuff's name must be unique!"),
    ]
    
class VcsBooking(models.Model):
    _name = 'vcs_web_edi.vcs_booking'
    _description = 'Booking'
    _inherit = ['mail.thread','mail.activity.mixin']
    
    skid = fields.Char(size=8,string="ID", tracking=True, required=True)
    ref_type_id = fields.Many2one('vcs_web_edi.vcs_ref_type', string="Ref. Type ID", tracking=True) # order_type_id = models.ForeignKey(RefType, verbose_name="Type ID", on_delete=models.SET_NULL, null=True)
    product_type = fields.Many2one('vcs_web_edi.vcs_product_type', string="Product Type ID", tracking=True) # filter_product_type = models.ManyToManyField(ProductType, blank=True, verbose_name="Filter Product Type ID",null=True)
    name = fields.Char(size=255,string="Name", tracking=True, required=True)
    code = fields.Char(size=50,string="Code", tracking=True, required=True)
    prefix = fields.Char(size=50,string="Code", tracking=True) # prefix = models.CharField(max_length=250, verbose_name="Prefix", blank=True, null=True)
    description = fields.Text(string="Description", tracking=True)
    is_active = fields.Boolean(string="Is Active", tracking=True, default=False)

    _sql_constraints = [
        ('uniq_booking_skid', 'unique(skid)', "A stuff already exists with this name . Stuff's name must be unique!"),
    ]
    
class VcsBookingDetail(models.Model):
    _name = 'vcs_web_edi.vcs_booking_detail'
    _description = 'Booking'
    _inherit = ['mail.thread','mail.activity.mixin']
    
    booking_id = fields.Many2one('vcs_web_edi.vcs_booking', string="Booking ID", tracking=True)
    from_factory_id = fields.Many2one('vcs_web_edi.vcs_whs', string="From Whs ID", tracking=True) # order_type_id = models.ForeignKey(RefType, verbose_name="Type ID", on_delete=models.SET_NULL, null=True)
    to_factory_id = fields.Many2one('vcs_web_edi.vcs_whs', string="To Whs ID", tracking=True) # filter_product_type = models.ManyToManyField(ProductType, blank=True, verbose_name="Filter Product Type ID",null=True)
    name = fields.Char(size=255,string="Name", tracking=True, required=True)
    description = fields.Text(string="Description", tracking=True)
    is_active = fields.Boolean(string="Is Active", tracking=True, default=False)

    _sql_constraints = [
        ('uniq_booking_detail_id', 'unique(booking_id)', "A stuff already exists with this name . Stuff's name must be unique!"),
    ]
    
class VcsLineNotifies(models.Model):
    _name = 'vcs_web_edi.vcs_line_notifies'
    _description = 'Line Notifies'
    _inherit = ['mail.thread','mail.activity.mixin']
    
    token = fields.Char(size=50,string="Token Key",tracking=True, required=True)
    name = fields.Char(size=255,string="Name", tracking=True, required=True)
    description = fields.Text(string="Description", tracking=True)
    is_active = fields.Boolean(string="Is Active", tracking=True, default=False)
    
    _sql_constraints = [
        ('uniq_line_notifies_token', 'unique(token)', "A stuff already exists with this name. Stuff's name must be unique!"),
    ]
    

class VcsManagementUser(models.Model):
    _name = 'vcs_web_edi.vcs_management_user'
    _description = 'Management User'
    _inherit = ['mail.thread','mail.activity.mixin']
    
    user_id = fields.One2many('res.users',string="User ID", required=True, tracking=True)
    line_notifies_id = fields.One2many('vcs_web_edi.vcs_line_notifies',string="Line Notifies ID", required=True,tracking=True)
    is_upload = fields.Boolean(string="Is Upload", tracking=True, default=False)
    is_open_pr = fields.Boolean(string="Is Open Purchase", tracking=True, default=False)
    is_open_po = fields.Boolean(string="Is Open Purchase", tracking=True, default=False)
    is_confirm_invoice = fields.Boolean(string="Is Confirm Invoice", tracking=True, default=False)
    view_report = fields.Boolean(string="View Report", tracking=True, default=True)
    is_print_tag = fields.Boolean(string="Print TAG", tracking=True, default=True)
    description = fields.Text(string="Description", tracking=True)
    is_active = fields.Boolean(string="Is Active", tracking=True, default=False)
    
    _sql_constraints = [
        ('uniq_user_id', 'unique(user_id)', "A stuff already exists with this name. Stuff's name must be unique!"),
    ]

class VcsReviseType(models.Model):
    _name = 'vcs_web_edi.vcs_revise_type'
    _description = 'Line Notifies'
    _inherit = ['mail.thread','mail.activity.mixin']
    
    name = fields.Integer(string="Revise Type", tracking=True, required=True)
    description = fields.Text(string="Description", tracking=True)
    is_active = fields.Boolean(string="Is Active", tracking=True, default=False)
    
    _sql_constraints = [
        ('uniq_revise_type', 'unique(name)', "A stuff already exists with this name. Stuff's name must be unique!"),
    ]
