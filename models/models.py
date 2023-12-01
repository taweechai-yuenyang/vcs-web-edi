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
    
    user_id = fields.Many2one('res.users',string="User ID", required=True, tracking=True)
    line_notifies_id = fields.Many2one('vcs_web_edi.vcs_line_notifies',string="Line Notifies ID", required=True,tracking=True)
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
    
class VcsOnMonth(models.Model):
    _name = 'vcs_web_edi.vcs_on_month'
    _description = 'On Month'
    _inherit = ['mail.thread','mail.activity.mixin']
    
    name = fields.Char(size=255,string="Name", tracking=True, required=True)
    value = fields.Integer(string="Value", tracking=True, required=True)
    description = fields.Text(string="Description", tracking=True)
    is_active = fields.Boolean(string="Is Active", tracking=True, default=False)
    
    _sql_constraints = [
        ('uniq_on_month_name', 'unique(name)', "A stuff already exists with this name. Stuff's name must be unique!"),
        ('uniq_on_month_value', 'unique(value)', "A stuff already exists with this name. Stuff's name must be unique!"),
    ]

class VcsOnYear(models.Model):
    _name = 'vcs_web_edi.vcs_on_year'
    _description = 'On Year'
    _inherit = ['mail.thread','mail.activity.mixin']
    
    name = fields.Char(size=255,string="Name", tracking=True, required=True)
    value = fields.Integer(string="Value", tracking=True, required=True)
    description = fields.Text(string="Description", tracking=True)
    is_active = fields.Boolean(string="Is Active", tracking=True, default=False)
    
    _sql_constraints = [
        ('uniq_on_year_name', 'unique(name)', "A stuff already exists with this name. Stuff's name must be unique!"),
        ('uniq_on_year_value', 'unique(value)', "A stuff already exists with this name. Stuff's name must be unique!"),
    ]
    
class VcsUploadForecast(models.Model):
    _name = 'vcs_web_edi.vcs_upload_forecast'
    _description = 'Upload Forecast'
    _inherit = ['mail.thread','mail.activity.mixin']
    
    file_forecast = fields.Binary(string='Upload Forecast', required=True,tracking=True)# file_forecast = models.FileField(upload_to="static/forecasts",verbose_name="File Forecast")
    forecast_date = fields.Date(string="Forecast Date", tracking=True, default=lambda self: fields.Date.today())# forecast_date = models.DateField(verbose_name="Date", default=timezone.now, blank=True, null=True)
    forecast_month_id = fields.Many2one('vcs_web_edi.vcs_on_month',string='On Month',required=True, tracking=True)# forecast_month = models.ForeignKey(OnMonthList, verbose_name="Month", on_delete=models.CASCADE)
    forecast_year_id = fields.Many2one('vcs_web_edi.vcs_on_year',string='On Year',required=True, tracking=True)# forecast_year = models.ForeignKey(OnYearList, verbose_name="Year", on_delete=models.CASCADE)
    forecast_book_id = fields.Many2one('vcs_web_edi.vcs_booking',string='Booking ID',required=True, tracking=True)# forecast_book_id = models.ForeignKey(Book, verbose_name="Book ID", on_delete=models.CASCADE)
    forecast_revise_id = fields.Many2one('vcs_web_edi.vcs_revise_type',string='Revise Type ID',required=True, tracking=True)# forecast_revise_id = models.ForeignKey(EDIReviseType, verbose_name="Revise", on_delete=models.CASCADE)
    description = fields.Text(string="Description", tracking=True)
    is_generated = fields.Boolean(string="Is Generated", tracking=True, default=False)
    is_active = fields.Boolean(string="Is Active", tracking=True, default=False)
    
class VcsForecastErrorLogs(models.Model):
    _name = 'vcs_web_edi.vcs_forecast_error_logs'
    _description = 'Forecast Error Logs'
    _inherit = ['mail.thread','mail.activity.mixin']
    
    file_name_id = fields.Many2one('vcs_web_edi.vcs_upload_forecast',string='Forecast File ID',tracking=True)# file_name = models.UUIDField(max_length=36, verbose_name="File Forecast")
    row_num = fields.Integer(string="Row", tracking=True)# row_num = models.IntegerField(verbose_name="Row")
    item = fields.Integer(string='Seq',tracking=True)
    part_code = fields.Char(size=255,string="Part Code", tracking=True, required=True)# part_code = models.CharField(max_length=50, verbose_name="Part Code")
    part_no = fields.Char(size=255,string="Part No.", tracking=True, required=True)# part_no = models.CharField(max_length=50, verbose_name="Part No.")
    part_name = fields.Char(size=255,string="Part Name", tracking=True, required=True)# part_name = models.CharField(max_length=50, verbose_name="Part Name")
    supplier = fields.Char(size=255,string="Supplier", tracking=True, required=True)# supplier = models.CharField(max_length=50, verbose_name="Supplier")
    model = fields.Char(size=255,string="Model", tracking=True, required=True)# model = models.CharField(max_length=50, verbose_name="Model")
    rev_0 = fields.Integer(string='Rev. 0',tracking=True)# rev_0 = models.IntegerField(verbose_name="Rev.0",default=0, blank=True, null=True)
    rev_1 = fields.Integer(string='Rev. 1',tracking=True)# rev_1 = models.IntegerField(verbose_name="Rev.1",default=0, blank=True, null=True)
    rev_2 = fields.Integer(string='Rev. 2',tracking=True)# rev_2 = models.IntegerField(verbose_name="Rev.2",default=0, blank=True, null=True)
    rev_3 = fields.Integer(string='Rev. 3',tracking=True)# rev_3 = models.IntegerField(verbose_name="Rev.3",default=0, blank=True, null=True)
    rev_4 = fields.Integer(string='Rev. 4',tracking=True)# rev_4 = models.IntegerField(verbose_name="Rev.4",default=0, blank=True, null=True)
    rev_5 = fields.Integer(string='Rev. 5',tracking=True)# rev_5 = models.IntegerField(verbose_name="Rev.5",default=0, blank=True, null=True)
    rev_6 = fields.Integer(string='Rev. 6',tracking=True)# rev_6 = models.IntegerField(verbose_name="Rev.6",default=0, blank=True, null=True)
    rev_7 = fields.Integer(string='Rev. 7',tracking=True)# rev_7 = models.IntegerField(verbose_name="Rev.7",default=0, blank=True, null=True)
    remark = fields.Text(string="Remark", tracking=True)# remark = models.TextField(verbose_name="Remark", blank=True, null=True)
    is_error = fields.Boolean(string="Is Error", tracking=True, default=False)# is_error = models.BooleanField(verbose_name="Is Error", default=True, blank=True, null=True)
    is_success = fields.Boolean(string="Is Success", tracking=True, default=False)# is_success = models.BooleanField(verbose_name="Is Success", default=False, blank=True, null=True)
    
class VcsForecast(models.Model):
    _name = 'vcs_web_edi.vcs_forecast'
    _description = 'Forecast'
    _inherit = ['mail.thread','mail.activity.mixin']
    
    file_forecast_id = fields.Many2one('vcs_web_edi.vcs_upload_forecast',string='Forecast ID',required=True, tracking=True)# file_forecast_id = models.ForeignKey(UploadForecast, verbose_name="Forecast ID", blank=False, null=False, on_delete=models.CASCADE, editable=False)
    part_model_id = fields.Many2one('vcs_web_edi.vcs_product_group',string='Model ID',required=True, tracking=True)# part_model_id = models.ForeignKey(ProductGroup, verbose_name="Model ID", on_delete=models.SET_NULL, null=True, blank=True)
    supplier_id = fields.Many2one('res.partner',string='Supplier ID',required=True, tracking=True)# supplier_id = models.ForeignKey(Supplier, verbose_name="Supplier ID", on_delete=models.SET_NULL, null=True, blank=True)
    book_id = fields.Many2one('vcs_web_edi.vcs_booking',string='Booking ID',required=True, tracking=True)# book_id = models.ForeignKey(Book, verbose_name="Book ID", blank=True,null=True, on_delete=models.SET_NULL)
    forecast_revise_id = fields.Many2one('vcs_web_edi.vcs_revise_type',string='Revise Type ID', required=True, tracking=True)# forecast_revise_id = models.ForeignKey(EDIReviseType,verbose_name="Revise ID", on_delete=models.SET_NULL,null=True, blank=True)
    forecast_on_month_id = fields.Many2one('vcs_web_edi.vcs_on_month',string='On Month ID', required=True, tracking=True)# forecast_on_month_id = models.ForeignKey(OnMonthList,verbose_name="Request On Month", on_delete=models.SET_NULL,null=True, blank=True)
    forecast_on_year_id = fields.Many2one('vcs_web_edi.vcs_on_year',string='On Year ID', required=True, tracking=True)# forecast_on_year_id = models.ForeignKey(OnYearList,verbose_name="Request On Year", on_delete=models.SET_NULL,null=True, blank=True)
    forecast_no = fields.Char(size=15,string="Forecast No.", tracking=True, required=True)# forecast_no = models.CharField(max_length=15,verbose_name="Request No.", blank=True, null=True)
    forecast_date = fields.Date(string="Forecast Date", tracking=True, default=lambda self: fields.Date.today())# forecast_date = models.DateField(verbose_name="Request Date", default=timezone.now, null=True, blank=True)
    forecast_item = fields.Integer(string="Item", tracking=True, default="0")# forecast_item = models.IntegerField(verbose_name="Item", blank=True,null=True, default="0")
    forecast_qty = fields.Float(string="Qty", tracking=True, default="0")# forecast_qty = models.FloatField(verbose_name="Qty.", blank=True,null=True, default="0")
    forecast_total_qty = fields.Float(string="Total", tracking=True, default="0")# forecast_total_qty = models.FloatField(verbose_name="Total Qty.", blank=True,null=True, default="0")
    forecast_price = fields.Float(string="Price", tracking=True, default="0")# forecast_price = models.FloatField(verbose_name="Price.", blank=True,null=True, default="0")
    forecast_m0 = fields.Float(string="Month 0", tracking=True, default="0")# forecast_m0 = models.FloatField(verbose_name="Month 0", blank=True, null=True, default="0")
    forecast_m1 = fields.Float(string="Month 1", tracking=True, default="0")# forecast_m1 = models.FloatField(verbose_name="Month 1", blank=True, null=True, default="0")
    forecast_m2 = fields.Float(string="Month 2", tracking=True, default="0")# forecast_m2 = models.FloatField(verbose_name="Month 2", blank=True, null=True, default="0")
    forecast_m3 = fields.Float(string="Month 3", tracking=True, default="0")# forecast_m3 = models.FloatField(verbose_name="Month 3", blank=True, null=True, default="0")
    remark = fields.Text(string="Remark", tracking=True)# remark = models.TextField(verbose_name="Remark", blank=True, null=True)
    forecast_by_id = fields.Many2one('res.users',string="User ID", required=True, tracking=True)# forecast_by_id = models.ForeignKey(ManagementUser, verbose_name="Request By ID", blank=True, null=True, on_delete=models.SET_NULL)
    forecast_status = fields.Selection([('0', 'รออนุมัติเปิด PR'),('1', 'อนุมัติเปิด PR'),('2', 'เปิด PR แล้ว'),('3', 'ไม่อนุมัติ'),], string="Status", tracking=True, default="0")# forecast_status = models.CharField(max_length=1, choices=FORECAST_ORDER_STATUS,verbose_name="Request Status", default="0")
    forecast_download_count = fields.Integer(string="Download Count", tracking=True)# forecast_download_count = models.IntegerField(verbose_name="Download Count",  blank=True, null=True, default="0")
    ref_formula_id = fields.Char(size=8,string="Formula ID", tracking=True)# ref_formula_id = models.CharField(max_length=8, verbose_name="Ref. Formula ID", blank=True, null=True)
    is_po = fields.Boolean(string="Is PO", tracking=True, default=False)# is_po = models.BooleanField(verbose_name="Is PO", default=False, blank=True, null=True)
    is_sync = fields.Boolean(string="Is Sync", tracking=True, default=False)# is_sync = models.BooleanField(verbose_name="Is Sync", default=True, blank=True, null=True)

    _sql_constraints = [
        ('uniq_forecast_no', 'unique(forecast_no)', "A stuff already exists with this name. Stuff's name must be unique!"),
    ]
class VcsForecastDetail(models.Model):
    _name = 'vcs_web_edi.vcs_forecast_detail'
    _description = 'Forecast Detail'
    _inherit = ['mail.thread','mail.activity.mixin']
    
    forecast_id = fields.Many2one('vcs_web_edi.vcs_forecast',string='Forecast ID', required=True, tracking=True)# forecast_id = models.ForeignKey(Forecast, verbose_name="Open PDS ID", blank=False, null=False, on_delete=models.CASCADE)
    product_type_id = fields.Many2one('vcs_web_edi.vcs_product_type',string='Product Type ID',required=True,tracking=True)# product_type_id = models.ForeignKey(Product, verbose_name="Product Code", blank=False, null=False, on_delete=models.CASCADE)
    product_id = fields.Many2one('product.template',string='Product ID',required=True,tracking=True)# product_id = models.ForeignKey(Product, verbose_name="Product Code", blank=False, null=False, on_delete=models.CASCADE)
    product_unit_id = fields.Many2one('vcs_web_edi.vcs_product_unit',string='Product Unit ID',required=True,tracking=True)# product_unit_id = models.ForeignKey(Product, verbose_name="Product Code", blank=False, null=False, on_delete=models.CASCADE)
    seq = fields.Integer(string="Seq", tracking=True, default="0")# seq = models.IntegerField(verbose_name="#", blank=True, null=True,default="0")
    request_qty = fields.Float(string="Request Qty", tracking=True, default="0")# request_qty = models.IntegerField(verbose_name="Request Qty.", default="0.0")
    balance_qty = fields.Float(string="Balance Qty", tracking=True, default="0")# balance_qty = models.IntegerField(verbose_name="Total Qty.", default="0.0")
    price = fields.Float(string="Price", tracking=True, default="0")# price = models.FloatField(verbose_name="Price.", blank=True,null=True, default="0")
    month_0 = fields.Integer(string="Month 0", tracking=True, default="0")# month_0 = models.IntegerField(verbose_name="Month 0", blank=True, null=True, default="0")
    month_1 = fields.Integer(string="Month 0", tracking=True, default="0")# month_1 = models.IntegerField(verbose_name="Month 1", blank=True, null=True, default="0")
    month_2 = fields.Integer(string="Month 0", tracking=True, default="0")# month_2 = models.IntegerField(verbose_name="Month 2", blank=True, null=True, default="0")
    month_3 = fields.Integer(string="Month 0", tracking=True, default="0")# month_3 = models.IntegerField(verbose_name="Month 3", blank=True, null=True, default="0")
    request_by_id = fields.Many2one('res.users',string='User ID',tracking=True)
    request_status = fields.Selection([('0', 'รออนุมัติเปิด PR'),('1', 'อนุมัติเปิด PR'),('2', 'เปิด PR แล้ว'),('3', 'ไม่อนุมัติ'),], string="Status", tracking=True, default="0")
    import_model_by_user = fields.Char(string="Request model by user.", tracking=True)
    remark = fields.Text(string="Remark", tracking=True)# remark = models.TextField(verbose_name="Remark", blank=True, null=True)
    ref_formula_id = fields.Char(size=8,string="Formula ID", tracking=True)
    is_selected = fields.Boolean(string="Is Selected", tracking=True, default=False)
    is_sync = fields.Boolean(string="Is Sync", tracking=True, default=False)