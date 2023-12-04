# -*- coding: utf-8 -*-
{
    'name': "VCS Web EDI",
    'author': "Taweechai Yuenyang",
    "email": "taweechai.yuenyang@outlook.com",
    'website': 'https://github.com/taweechai-yuenyang/vcs-web-edi',
    'license': 'Other OSI approved licence',# license คือ หมวดหมู่หน่วยงานของโมดูล
    'summary': 'จัดการข้อมูล Web EDI',# summary คือ คำอธิบายสั้นๆ ของโมดูล
    'description': 'จัดการข้อมูล Web EDI ของบริษัทในเคลือของ VCS Group.',# description คือ คำอธิบายยาวของโมดูล
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'VCS Category',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base','web','mail','product'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/vcs_product_unit.xml',
        'demo/vcs_product_group.xml',
        'demo/vcs_product_type.xml',
        'demo/vcs_ref_type.xml',
        'demo/vcs_whs.xml',
        'demo/vcs_booking.xml',
        'demo/vcs_line_notifies.xml',
        'demo/vcs_revise_type.xml',
        'demo/vcs_on_month.xml',
        'demo/vcs_on_year.xml',
        'demo/vcs_product.xml',
    ],
    "application": True,
    'installable': True,# installable คือ ระบุว่าโมดูลสามารถติดตั้งได้หรือไม่
    'auto_install': False,# auto_install คือ ระบุว่าโมดูลจะติดตั้งโดยอัตโนมัติหรือไม่
}

