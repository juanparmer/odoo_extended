# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResCompany(models.Model):
    _name = 'res.company'
    _inherit = 'res.company'

    def _default_sequence(self):
        return self.env.ref('l10n_co_edi.ir_sequence_l10n_co')

    l10n_co_email = fields.Char('email ei')
    # Name XML
    l10n_co_code_pt = fields.Char('technology provider code', default='000', help='If your own software, use 000',
                                  size=3, copy=False)
    l10n_co_sequence_id = fields.Many2one('ir.sequence', 'shipping sequence', default=_default_sequence, readonly=True,
                                          copy=False)
    # Invoice Control
    l10n_co_invoice_authorization = fields.Char('Invoice authorization', copy=False)
    l10n_co_ap_sdate = fields.Date('Start date', copy=False, help="Start date authorization period")
    l10n_co_ap_edate = fields.Date('End date', copy=False, help="End date authorization period")
    l10n_co_ai_prefix = fields.Char('Prefix', copy=False, help="Prefix authorized invoices")
    l10n_co_ai_from = fields.Char('From Range', copy=False, help="Range from authorized invoices")
    l10n_co_ai_to = fields.Char('To Range', copy=False, help="Range to authorized invoices")

    _sql_constraints = [
        ('l10n_co_code_pt',
         "CHECK(l10n_co_code_pt IS NULL OR LENGTH(l10n_co_code_pt) != 3)",
         "technology provider code must have 3 characters."),
    ]
