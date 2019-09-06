# -*- coding: utf-8 -*-

from odoo import models, fields, api


class res_partner(models.Model):
    _inherit = 'res.partner'

    @api.multi
    def check_vat_co(self, vat):
        return True
