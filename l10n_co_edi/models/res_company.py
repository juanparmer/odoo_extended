# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResCompany(models.Model):
    _name = 'res.company'
    _inherit = 'res.company'

    def _default_sequence(self):
        return self.env.ref('l10n_co_edi.ir_sequence_l10n_co')

    l10n_co_email = fields.Char('email ei')
    l10n_co_code_pt = fields.Char('technology provider code', default='000', help='If your own software, use 000',
                                  size=3)
    l10n_co_sequence_id = fields.Many2one('ir.sequence', 'shipping sequence', default=_default_sequence, readonly=True,
                                          copy=False)
    l10n_co_invoice_authorization = fields.Char('Invoice authorization', copy=False)

    _sql_constraints = [
        ('l10n_co_code_pt',
         "CHECK(l10n_co_code_pt IS NULL OR LENGTH(l10n_co_code_pt) != 3)",
         "technology provider code must have 3 characters."),
    ]
