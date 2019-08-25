# -*- coding: utf-8 -*-
from odoo import http

# class BaseExtended(http.Controller):
#     @http.route('/base_extended/base_extended/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/base_extended/base_extended/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('base_extended.listing', {
#             'root': '/base_extended/base_extended',
#             'objects': http.request.env['base_extended.base_extended'].search([]),
#         })

#     @http.route('/base_extended/base_extended/objects/<model("base_extended.base_extended"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('base_extended.object', {
#             'object': obj
#         })