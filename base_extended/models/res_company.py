# -*- coding: utf-8 -*-

from odoo import models, fields, api


class res_company(models.Model):
    _inherit = 'res.company'

    user_number = fields.Integer('Number of users', default=3, help='How many users can the company have')
