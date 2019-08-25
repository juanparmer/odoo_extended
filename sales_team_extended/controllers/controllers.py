# -*- coding: utf-8 -*-
from odoo import http

# class SalesTeamExtended(http.Controller):
#     @http.route('/sales_team_extended/sales_team_extended/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales_team_extended/sales_team_extended/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales_team_extended.listing', {
#             'root': '/sales_team_extended/sales_team_extended',
#             'objects': http.request.env['sales_team_extended.sales_team_extended'].search([]),
#         })

#     @http.route('/sales_team_extended/sales_team_extended/objects/<model("sales_team_extended.sales_team_extended"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales_team_extended.object', {
#             'object': obj
#         })