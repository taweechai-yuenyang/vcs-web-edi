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
    ref_type_id = fields.Many2one('vcs_web_edi.vcs_ref_type', string="Ref. Type ID", tracking=True) # order_type_id = fields.Many2one(RefType, string="Type ID", on_delete=models.SET_NULL, null=True)
    product_type = fields.Many2one('vcs_web_edi.vcs_product_type', string="Product Type ID", tracking=True) # filter_product_type = models.ManyToManyField(ProductType, , string="Filter Product Type ID",null=True)
    name = fields.Char(size=255,string="Name", tracking=True, required=True)
    code = fields.Char(size=50,string="Code", tracking=True, required=True)
    prefix = fields.Char(size=50,string="Code", tracking=True) # prefix = fields.Char(size=250, string="Prefix")
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
    from_factory_id = fields.Many2one('vcs_web_edi.vcs_whs', string="From Whs ID", tracking=True) # order_type_id = fields.Many2one(RefType, string="Type ID", on_delete=models.SET_NULL, null=True)
    to_factory_id = fields.Many2one('vcs_web_edi.vcs_whs', string="To Whs ID", tracking=True) # filter_product_type = models.ManyToManyField(ProductType, , string="Filter Product Type ID",null=True)
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
    
    file_forecast = fields.Binary(string='Upload Forecast', required=True,tracking=True)# file_forecast = models.FileField(upload_to="static/forecasts",string="File Forecast")
    forecast_date = fields.Date(string="Forecast Date", tracking=True, default=lambda self: fields.Date.today())# forecast_date = fields.Date(string="Date", default=timezone.now)
    forecast_month_id = fields.Many2one('vcs_web_edi.vcs_on_month',string='On Month',required=True, tracking=True)# forecast_month = fields.Many2one(OnMonthList, string="Month", on_delete=models.CASCADE)
    forecast_year_id = fields.Many2one('vcs_web_edi.vcs_on_year',string='On Year',required=True, tracking=True)# forecast_year = fields.Many2one(OnYearList, string="Year", on_delete=models.CASCADE)
    forecast_book_id = fields.Many2one('vcs_web_edi.vcs_booking',string='Booking ID',required=True, tracking=True)# forecast_book_id = fields.Many2one(Book, string="Book ID", on_delete=models.CASCADE)
    forecast_revise_id = fields.Many2one('vcs_web_edi.vcs_revise_type',string='Revise Type ID',required=True, tracking=True)# forecast_revise_id = fields.Many2one(EDIReviseType, string="Revise", on_delete=models.CASCADE)
    description = fields.Text(string="Description", tracking=True)
    is_generated = fields.Boolean(string="Is Generated", tracking=True, default=False)
    is_active = fields.Boolean(string="Is Active", tracking=True, default=False)
    
class VcsForecastErrorLogs(models.Model):
    _name = 'vcs_web_edi.vcs_forecast_error_logs'
    _description = 'Forecast Error Logs'
    _inherit = ['mail.thread','mail.activity.mixin']
    
    file_name_id = fields.Many2one('vcs_web_edi.vcs_upload_forecast',string='Forecast File ID',tracking=True)# file_name = models.UUIDField(size=36, string="File Forecast")
    row_num = fields.Integer(string="Row", tracking=True)# row_num = fields.Integer(string="Row")
    item = fields.Integer(string='Seq',tracking=True)
    part_code = fields.Char(size=255,string="Part Code", tracking=True, required=True)# part_code = fields.Char(size=50, string="Part Code")
    part_no = fields.Char(size=255,string="Part No.", tracking=True, required=True)# part_no = fields.Char(size=50, string="Part No.")
    part_name = fields.Char(size=255,string="Part Name", tracking=True, required=True)# part_name = fields.Char(size=50, string="Part Name")
    supplier = fields.Char(size=255,string="Supplier", tracking=True, required=True)# supplier = fields.Char(size=50, string="Supplier")
    model = fields.Char(size=255,string="Model", tracking=True, required=True)# model = fields.Char(size=50, string="Model")
    rev_0 = fields.Integer(string='Rev. 0',tracking=True)# rev_0 = fields.Integer(string="Rev.0",default=0)
    rev_1 = fields.Integer(string='Rev. 1',tracking=True)# rev_1 = fields.Integer(string="Rev.1",default=0)
    rev_2 = fields.Integer(string='Rev. 2',tracking=True)# rev_2 = fields.Integer(string="Rev.2",default=0)
    rev_3 = fields.Integer(string='Rev. 3',tracking=True)# rev_3 = fields.Integer(string="Rev.3",default=0)
    rev_4 = fields.Integer(string='Rev. 4',tracking=True)# rev_4 = fields.Integer(string="Rev.4",default=0)
    rev_5 = fields.Integer(string='Rev. 5',tracking=True)# rev_5 = fields.Integer(string="Rev.5",default=0)
    rev_6 = fields.Integer(string='Rev. 6',tracking=True)# rev_6 = fields.Integer(string="Rev.6",default=0)
    rev_7 = fields.Integer(string='Rev. 7',tracking=True)# rev_7 = fields.Integer(string="Rev.7",default=0)
    remark = fields.Text(string="Remark", tracking=True)# remark = fields.Char(string="Remark")
    is_error = fields.Boolean(string="Is Error", tracking=True, default=False)# is_error = fields.Boolean(string="Is Error", default=True)
    is_success = fields.Boolean(string="Is Success", tracking=True, default=False)# is_success = fields.Boolean(string="Is Success", default=False)
    
class VcsForecast(models.Model):
    _name = 'vcs_web_edi.vcs_forecast'
    _description = 'Forecast'
    _inherit = ['mail.thread','mail.activity.mixin']
    
    file_forecast_id = fields.Many2one('vcs_web_edi.vcs_upload_forecast',string='Forecast ID',required=True, tracking=True)# file_forecast_id = fields.Many2one(UploadForecast, string="Forecast ID", blank=False, null=False, on_delete=models.CASCADE, editable=False)
    part_model_id = fields.Many2one('vcs_web_edi.vcs_product_group',string='Model ID',required=True, tracking=True)# part_model_id = fields.Many2one(ProductGroup, string="Model ID", on_delete=models.SET_NULL,  )
    supplier_id = fields.Many2one('res.partner',string='Supplier ID',required=True, tracking=True)# supplier_id = fields.Many2one(Supplier, string="Supplier ID", on_delete=models.SET_NULL,  )
    book_id = fields.Many2one('vcs_web_edi.vcs_booking',string='Booking ID',required=True, tracking=True)# book_id = fields.Many2one(Book, string="Book ID", , on_delete=models.SET_NULL)
    forecast_revise_id = fields.Many2one('vcs_web_edi.vcs_revise_type',string='Revise Type ID', required=True, tracking=True)# forecast_revise_id = fields.Many2one(EDIReviseType,string="Revise ID", on_delete=models.SET_NULL, )
    forecast_on_month_id = fields.Many2one('vcs_web_edi.vcs_on_month',string='On Month ID', required=True, tracking=True)# forecast_on_month_id = fields.Many2one(OnMonthList,string="Request On Month", on_delete=models.SET_NULL, )
    forecast_on_year_id = fields.Many2one('vcs_web_edi.vcs_on_year',string='On Year ID', required=True, tracking=True)# forecast_on_year_id = fields.Many2one(OnYearList,string="Request On Year", on_delete=models.SET_NULL, )
    forecast_no = fields.Char(size=15,string="Forecast No.", tracking=True, required=True)# forecast_no = fields.Char(size=15,string="Request No.")
    forecast_date = fields.Date(string="Forecast Date", tracking=True, default=lambda self: fields.Date.today())# forecast_date = fields.Date(string="Request Date", default=timezone.now,  )
    forecast_item = fields.Integer(string="Item", tracking=True, default="0")# forecast_item = fields.Integer(string="Item", , default="0")
    forecast_qty = fields.Float(string="Qty", tracking=True, default="0")# forecast_qty =fields.Float(string="Qty.", , default="0")
    forecast_total_qty = fields.Float(string="Total", tracking=True, default="0")# forecast_total_qty =fields.Float(string="Total Qty.", , default="0")
    forecast_price = fields.Float(string="Price", tracking=True, default="0")# forecast_price =fields.Float(string="Price.", , default="0")
    forecast_m0 = fields.Float(string="Month 0", tracking=True, default="0")# forecast_m0 =fields.Float(string="Month 0", default="0")
    forecast_m1 = fields.Float(string="Month 1", tracking=True, default="0")# forecast_m1 =fields.Float(string="Month 1", default="0")
    forecast_m2 = fields.Float(string="Month 2", tracking=True, default="0")# forecast_m2 =fields.Float(string="Month 2", default="0")
    forecast_m3 = fields.Float(string="Month 3", tracking=True, default="0")# forecast_m3 =fields.Float(string="Month 3", default="0")
    remark = fields.Text(string="Remark", tracking=True)# remark = fields.Char(string="Remark")
    forecast_by_id = fields.Many2one('res.users',string="User ID", required=True, tracking=True)# forecast_by_id = fields.Many2one(ManagementUser, string="Request By ID", on_delete=models.SET_NULL)
    forecast_status = fields.Selection([('0', 'รออนุมัติเปิด PR'),('1', 'อนุมัติเปิด PR'),('2', 'เปิด PR แล้ว'),('3', 'ไม่อนุมัติ'),], string="Status", tracking=True,default="0")# forecast_status = fields.Char(size=1, choices=FORECAST_ORDER_STATUS,string="Request Status", default="0")
    forecast_download_count = fields.Integer(string="Download Count", tracking=True)# forecast_download_count = fields.Integer(string="Download Count",  ,  default="0")
    ref_formula_id = fields.Char(size=8,string="Formula ID", tracking=True)# ref_formula_id = fields.Char(size=8, string="Ref. Formula ID")
    is_po = fields.Boolean(string="Is PO", tracking=True, default=False)# is_po = fields.Boolean(string="Is PO", default=False)
    is_sync = fields.Boolean(string="Is Sync", tracking=True, default=False)# is_sync = fields.Boolean(string="Is Sync", default=True)

    _sql_constraints = [
        ('uniq_forecast_no', 'unique(forecast_no)', "A stuff already exists with this name. Stuff's name must be unique!"),
    ]
class VcsForecastDetail(models.Model):
    _name = 'vcs_web_edi.vcs_forecast_detail'
    _description = 'Forecast Detail'
    _inherit = ['mail.thread','mail.activity.mixin']
    
    forecast_id = fields.Many2one('vcs_web_edi.vcs_forecast',string='Forecast ID', required=True, tracking=True)# forecast_id = fields.Many2one(Forecast, string="Open PDS ID", blank=False, null=False, on_delete=models.CASCADE)
    product_type_id = fields.Many2one('vcs_web_edi.vcs_product_type',string='Product Type ID',required=True,tracking=True)# product_type_id = fields.Many2one(Product, string="Product Code", blank=False, null=False, on_delete=models.CASCADE)
    product_id = fields.Many2one('product.template',string='Product ID',required=True,tracking=True)# product_id = fields.Many2one(Product, string="Product Code", blank=False, null=False, on_delete=models.CASCADE)
    product_unit_id = fields.Many2one('vcs_web_edi.vcs_product_unit',string='Product Unit ID',required=True,tracking=True)# product_unit_id = fields.Many2one(Product, string="Product Code", blank=False, null=False, on_delete=models.CASCADE)
    seq = fields.Integer(string="Seq", tracking=True, default="0")# seq = fields.Integer(string="#",default="0")
    request_qty = fields.Float(string="Request Qty", tracking=True, default="0")# request_qty = fields.Integer(string="Request Qty.", default="0.0")
    balance_qty = fields.Float(string="Balance Qty", tracking=True, default="0")# balance_qty = fields.Integer(string="Total Qty.", default="0.0")
    price = fields.Float(string="Price", tracking=True, default="0")# price =fields.Float(string="Price.", , default="0")
    month_0 = fields.Integer(string="Month 0", tracking=True, default="0")# month_0 = fields.Integer(string="Month 0", default="0")
    month_1 = fields.Integer(string="Month 1", tracking=True, default="0")# month_1 = fields.Integer(string="Month 1", default="0")
    month_2 = fields.Integer(string="Month 2", tracking=True, default="0")# month_2 = fields.Integer(string="Month 2", default="0")
    month_3 = fields.Integer(string="Month 3", tracking=True, default="0")
    request_by_id = fields.Many2one('res.users',string='User ID',tracking=True)
    request_status = fields.Selection([('0', 'รออนุมัติเปิด PR'),('1', 'อนุมัติเปิด PR'),('2', 'เปิด PR แล้ว'),('3', 'ไม่อนุมัติ'),], string="Status", tracking=True, default="0")
    import_model_by_user = fields.Char(string="Request model by user.", tracking=True)
    remark = fields.Text(string="Remark", tracking=True)# remark = fields.Char(string="Remark")
    ref_formula_id = fields.Char(size=8,string="Formula ID", tracking=True)
    is_selected = fields.Boolean(string="Is Selected", tracking=True, default=False)
    is_sync = fields.Boolean(string="Is Sync", tracking=True, default=False)
    
class VcsPDS(models.Model):
    _name = 'vcs_web_edi.vcs_pds'
    _description = 'PDS'
    _inherit = ['mail.thread','mail.activity.mixin']
    
    approve_by_id = fields.Many2one('res.users',string='Approve By', required=True, tracking=True)# approve_by_id = fields.Many2one(ManagementUser, string="Approve By ID", on_delete=models.SET_NULL)
    forecast_id = fields.Many2one('vcs_web_edi.vcs_forecast',string='Approve By', required=True, tracking=True)# forecast_id = fields.Many2one(Forecast, string="PR No.", blank=False, null=False, on_delete=models.CASCADE, editable=False)
    supplier_id = fields.Many2one('res.partner',string='Supplier ID', required=True, tracking=True)# supplier_id = fields.Many2one(Supplier, string="Supplier ID", on_delete=models.SET_NULL)
    part_model_id = fields.Many2one('vcs_web_edi.vcs_product_group',string='Part Model ID', required=True, tracking=True)# part_model_id = fields.Many2one(ProductGroup, string="Model ID", on_delete=models.SET_NULL,  )
    pds_date = fields.Date(string="PDS Date", tracking=True)# pds_date = fields.Date(string="PDS Date")
    delivery_date = fields.Date(string="Delivery Date", tracking=True)# pds_delivery_date = fields.Date(string="Delivery Date")
    pds_no = fields.Char(string="PDS No.", required=True, tracking=True)# pds_no = fields.Char(size=15,string="PDS No.")
    revise_id = fields.Many2one('vcs_web_edi.vcs_revise_type',string='Revise ID', required=True, tracking=True)# pds_revise_id = fields.Many2one(EDIReviseType,string="Revise ID", on_delete=models.SET_NULL, )
    on_month_id = fields.Many2one('vcs_web_edi.vcs_on_month',string='On Month ID', required=True, tracking=True)# pds_on_month_id = fields.Many2one(OnMonthList,string="Request On Month", on_delete=models.SET_NULL, )
    on_year_id = fields.Many2one('vcs_web_edi.vcs_on_year',string='On Year ID', required=True, tracking=True)# pds_on_year_id = fields.Many2one(OnYearList,string="Request On Year", on_delete=models.SET_NULL, )
    item = fields.Integer(string="Item", tracking=True, default="0")# item = fields.Integer(string="Item")
    qty = fields.Integer(string="Qty", tracking=True, default="0")# qty = fields.Integer(string="Qty")
    balance_qty = fields.Integer(string="Balance Qty", tracking=True, default="0")# balance_qty = fields.Integer(string="Total Qty", default="0")
    summary_price = fields.Float(string="Summary Price", tracking=True, default="0")# summary_price =fields.Float(string="Summary Price", default="0")
    remark = fields.Text(string="Remark", tracking=True)# remark = fields.Char(string="Remark")
    status = fields.Selection([(0, "รอเปิด PO"),(1, "เปิด PO บางส่วน"),(2, "เสร็จสมบูรณ์"),(3, "-"),(4, "-")], string="Status", tracking=True, default="0")# pds_status = fields.Char(size=1, choices=FORECAST_PDS_STATUS,string="PDS Status", default="0")
    download_count = fields.Integer(string="Download Count", tracking=True, default="0")# pds_download_count = fields.Integer(string="Download Count")
    ref_formula_id = fields.Char(size=8,string="Formula ID", tracking=True)
    is_activate = fields.Boolean(string="Is Active", tracking=True, default=False)
    
    _sql_constraints = [
        ('uniq_pds_no', 'unique(pds_no)', "A stuff already exists with this name. Stuff's name must be unique!"),
    ]
    
class VcsPDSDetail(models.Model):
    _name = 'vcs_web_edi.vcs_pds_detail'
    _description = 'PDS Detail'
    _inherit = ['mail.thread','mail.activity.mixin']
    
    pds_header_id = fields.Many2one('vcs_web_edi.vcs_pds', string="PDS ID", required=True, tracking=True)
    forecast_detail_id = fields.Many2one('vcs_web_edi.vcs_forecast_detail', string="PDS Detail", required=True, tracking=True)
    seq = fields.Integer(string="Seq.", tracking=True, default="0")
    qty = fields.Integer(string="Qty", tracking=True, default="0")
    balance_qty = fields.Integer(string="Total Qty", tracking=True, default="0")
    price = fields.Float(string="Price", tracking=True, default="0")
    remark = fields.Text(string="Remark", tracking=True)
    ref_formula_id = fields.Char(size=8, tracking=True, string="Formula ID")
    is_select = fields.Boolean(string="Is Select", default=True)
    is_active = fields.Boolean(string="Is Active", default=False)
    
class VcsReportPDSHeader(models.Model):
    _name = 'vcs_web_edi.vcs_report_pds_header'
    _description = 'Report PDS Header'
    _inherit = ['mail.thread','mail.activity.mixin']
    
    delivery_date = fields.Char(size=50,string="Delivery Date", required=True, tracking=True)# ParmDeliveryDate
    sup_code = fields.Char(size=50, string="Sup. Code", required=True, tracking=True)# ParmSupCode
    sup_name = fields.Char(size=255, string="Sup. Name", required=True, tracking=True)# ParmSumName
    sup_telephone = fields.Char(size=50, string="Sup. Telephone", tracking=True)# ParmSupTelephone
    pds_no = fields.Char(size=50,string="PDS No.", required=True, tracking=True)# ParmPDSNo
    issue_date = fields.Char(size=50, string="Issue Date", required=True, tracking=True)# ParmIssueDate
    issue_time = fields.Char(size=50, string="Issue Time", tracking=True)# ParmTime
    approve_by_id = fields.Binary(string="Approve By ID",tracking=True)
    issue_by_id = fields.Binary(string="Issue By ID",tracking=True)
    is_active = fields.Boolean(string="Is Active", tracking=True, default=False)
    
    _sql_constraints = [
        ('uniq_report_pds_no', 'unique(pds_no)', "A stuff already exists with this name. Stuff's name must be unique!"),
    ]
    
class VcsReportPDSDetail(models.Model):
    _name = 'vcs_web_edi.vcs_report_pds_detail'
    _description = 'Report PDS Detail'
    _inherit = ['mail.thread','mail.activity.mixin']
    
    pds_no = fields.Many2one('vcs_web_edi.vcs_report_pds_header', string="PDS Header", required=True, tracking=True)
    seq = fields.Integer(string="Seq.", required=True, tracking=True)
    part_model = fields.Char(size=50, string="Part Model", required=True, tracking=True)
    part_code = fields.Char(size=50, string="Part Code", required=True, tracking=True)
    part_name = fields.Char(size=255, string="Part Name", required=True, tracking=True)
    packing_qty = fields.Integer(string="Packing", tracking=True, default="0")# itemPartPack
    total = fields.Integer(string="Total", tracking=True, default="0")# itemTotal
    is_active = fields.Boolean(string="Is Active", tracking=True, default=False)
    
class VcsConfirmInvoiceHeader(models.Model):
    _name = 'vcs_web_edi.vcs_confirm_invoice_header'
    _description = 'Confirm Invoice Header'
    _inherit = ['mail.thread','mail.activity.mixin']
    
    approve_by_id = fields.Many2one('res.users', string="Approve By ID", required=True, tracking=True)
    pds_id = fields.Many2one('vcs_web_edi.vcs_pds', string="PR No.", required=True, tracking=True)
    supplier_id = fields.Many2one('res.partner', string="Supplier ID", required=True, tracking=True)
    part_model_id = fields.Many2one('vcs_web_edi.vcs_product_group', string="Model ID", required=True, tracking=True)
    purchase_no = fields.Char(size=15, string="PO No.", required=True, tracking=True)
    inv_date = fields.Date(string="Invoice Date", required=True, tracking=True)
    inv_delivery_date = fields.Date(string="Delivery Date", required=True, tracking=True)
    inv_no = fields.Char(size=15, string="Invoice No.", required=True, tracking=True)
    item = fields.Integer(string="Item", required=True, tracking=True)
    qty = fields.Integer(string="Qty", required=True, tracking=True)
    confirm_qty = fields.Integer(string="Confirm Qty", tracking=True,default="0")
    summary_price =fields.Float(string="Summary Price", tracking=True, default="0")
    remark = fields.Char(string="Remark",tracking=True)
    inv_status = fields.Selection([("0", "รอยืนยัน"),("1", "ยืนยันแล้ว"),("2", "จัดส่งไม่ครบ")], string="Inv Status", tracking=True,default="0")
    ref_formula_id = fields.Char(size=8, string="Formula ID", tracking=True)
    is_download_count = fields.Integer(string="Download Count", tracking=True, default="0")# itemTotal
    is_active = fields.Boolean(string="Is Active", tracking=True, default=False)
    
class VcsConfirmInvoiceDetail(models.Model):
    _name = 'vcs_web_edi.vcs_confirm_invoice_detail'
    _description = 'Confirm Invoice Detail'
    _inherit = ['mail.thread','mail.activity.mixin']
    
    invoice_header_id = fields.Many2one('vcs_web_edi.vcs_confirm_invoice_header', string="PDS ID", required=True, tracking=True)
    pds_detail_id = fields.Many2one('vcs_web_edi.vcs_report_pds_detail', string="PDS Detail", required=True, tracking=True)
    seq = fields.Integer(string="Seq.",tracking=True, default="0")
    qty = fields.Integer(string="Qty",tracking=True, default="0")
    confirm_qty = fields.Integer(string="Confirm Qty", required=True, tracking=True, default="0")
    total_qty = fields.Integer(string="Total Qty", required=True, tracking=True, default="0")
    balance_qty = fields.Integer(string="Total Qty", required=True, tracking=True, default="0")
    price = fields.Float(string="Summary Price", tracking=True, default="0")
    remark = fields.Char(string="Remark",tracking=True)
    ref_formula_id = fields.Char(size=8, string="Formula ID", tracking=True)
    is_Select = fields.Boolean(string="Is Select", tracking=True, default=False)
    is_active = fields.Boolean(string="Is Active", tracking=True, default=False)
    
class VcsPrintTag(models.Model):
    _name = 'vcs_web_edi.vcs_print_tag'
    _description = 'Print Tag'
    _inherit = ['mail.thread','mail.activity.mixin']
    
    parm_id = fields.Integer(string="Print TAG ID",required=True,tracking=True)
    seq = fields.Integer(string="Seq", tracking=True, default="0")
    purchase_id = fields.Char(size=36,string="Purchase ID",required=True,tracking=True)
    purchase_no = fields.Char(size=50,string="PO No.",required=True,tracking=True)
    part_no = fields.Char(size=255,string="Part No.",required=True,tracking=True)
    part_name = fields.Char(size=255,string="Part Name",required=True,tracking=True)
    part_model = fields.Char(size=255,string="Part Model",required=True,tracking=True)
    qty = fields.Integer(string="Qty",required=True,tracking=True)
    unit = fields.Char(size=25, string="Unit",required=True,tracking=True)
    lot_no = fields.Char(size=50, string="LotNo.", tracking=True)
    customer_name = fields.Char(size=50, string="Customer",required=True,tracking=True)
    print_date = fields.Char(size=10, string="Print Date",tracking=True)
    qr_code = fields.Char(size=255, string="QR Code", tracking=True)
    is_active = fields.Boolean(string="Is Active", default=False, tracking=True)
    
class VcsReceiveHeader(models.Model):
    _name = 'vcs_web_edi.vcs_receive_header'
    _description = 'Receive Header'
    _inherit = ['mail.thread','mail.activity.mixin']
    
    receive_by_id = fields.Many2one('res.users', string="Receive By ID",required=True,tracking=True)
    confirm_invoice_id = fields.Many2one('vcs_web_edi.vcs_confirm_invoice_header', string="PO No.",required=True,tracking=True)
    supplier_id = fields.Many2one('res.partner', string="Supplier ID",required=True,tracking=True)
    part_model_id = fields.Many2one('vcs_web_edi.vcs_product_group', string="Model ID",required=True,tracking=True)
    purchase_no = fields.Char(size=15,string="PO No.",tracking=True)
    receive_no = fields.Char(size=15,string="Receive No.",tracking=True)
    receive_date = fields.Date(string="Invoice Date",tracking=True)
    inv_delivery_date = fields.Date(string="Delivery Date",tracking=True)
    inv_no = fields.Char(size=15,string="Invoice No.",tracking=True)
    item = fields.Integer(string="Item")
    qty = fields.Integer(string="Qty")
    summary_price = fields.Float(string="Summary Price",tracking=True, default="0")
    remark = fields.Text(string="Remark",tracking=True)
    receive_status = fields.Selection([("0", "รอรับ"),("1", "รับแล้ว")], string="Receive Status",tracking=True, default="0")
    ref_formula_id = fields.Char(size=8, string="Formula ID", tracking=True)
    is_active = fields.Boolean(string="Is Active", tracking=True, default=False)
    
class VcsReceiveDetail(models.Model):
    _name = 'vcs_web_edi.vcs_receive_detail'
    _description = 'Receive Detail'
    _inherit = ['mail.thread','mail.activity.mixin']
    
    receive_header_id = fields.Many2one('vcs_web_edi.vcs_receive_header', string="Receive ID",required=True, tracking=True)
    confirm_detail_id = fields.Many2one('vcs_web_edi.vcs_confirm_invoice_detail', string="Confirm Detail",required=True, tracking=True)
    seq = fields.Integer(string="Seq", tracking=True)
    qty = fields.Integer(string="Qty", tracking=True)
    summary_price = fields.Float(string="Summary Price",tracking=True, default="0")
    remark = fields.Text(string="Remark",tracking=True)
    receive_status = fields.Selection([("0", "รอรับ"),("1", "รับแล้ว")], string="Receive Status",tracking=True, default="0")
    ref_formula_id = fields.Char(size=8, string="Formula ID", tracking=True)
    is_active = fields.Boolean(string="Is Active", tracking=True, default=False)
