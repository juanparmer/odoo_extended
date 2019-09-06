# -*- coding: utf-8 -*-
from odoo import http

# class BaseVatCo(http.Controller):
#     @http.route('/base_vat_co/base_vat_co/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/base_vat_co/base_vat_co/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('base_vat_co.listing', {
#             'root': '/base_vat_co/base_vat_co',
#             'objects': http.request.env['base_vat_co.base_vat_co'].search([]),
#         })

#     @http.route('/base_vat_co/base_vat_co/objects/<model("base_vat_co.base_vat_co"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('base_vat_co.object', {
#             'object': obj
#         })