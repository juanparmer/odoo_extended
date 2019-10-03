# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class electronic_invoice(models.Model):
#     _name = 'electronic_invoice.electronic_invoice'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100