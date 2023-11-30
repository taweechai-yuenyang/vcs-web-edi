# -*- coding: utf-8 -*-
# from odoo import http


# class VcsWebEdi(http.Controller):
#     @http.route('/vcs_web_edi/vcs_web_edi', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vcs_web_edi/vcs_web_edi/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('vcs_web_edi.listing', {
#             'root': '/vcs_web_edi/vcs_web_edi',
#             'objects': http.request.env['vcs_web_edi.vcs_web_edi'].search([]),
#         })

#     @http.route('/vcs_web_edi/vcs_web_edi/objects/<model("vcs_web_edi.vcs_web_edi"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vcs_web_edi.object', {
#             'object': obj
#         })

