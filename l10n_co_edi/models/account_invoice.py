# -*- coding: utf-8 -*-

import base64
import re

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'
    _name = 'account.invoice'

    type = fields.Selection(selection_add=[("out_payment", "Debit note")])
    l10n_co_send_state = fields.Selection([
        ('new', 'New'),
        ('other', 'Other'),
        ('to_send', 'Not yet send'),
        ('sent', 'Sent, waiting for response'),
        ('invalid', 'Sent, but invalid'),
        ('delivered', 'This invoice is delivered'),
        ('delivered_accepted', 'This invoice is delivered and accepted by destinatory'),
        ('delivered_refused', 'This invoice is delivered and refused by destinatory'),
        ('delivered_expired', 'This invoice is delivered and expired'),
        ('failed_delivery', 'Delivery impossible, ES certify that it has received the invoice and that the file \
                        could not be delivered to the addressee')
    ], 'Send state', default='to_send', copy=False)
    l10n_co_einvoice_id = fields.Many2one('ir.attachment', 'Electronic invoice', copy=False)
    l10n_co_einvoice_name = fields.Char('E invoice name', readonly=True, copy=False)

    @api.multi
    def invoice_validate(self):
        # Clean context from default_type to avoid making attachment
        # with wrong values in subsequent operations
        cleaned_ctx = dict(self.env.context)
        cleaned_ctx.pop('default_type', None)
        self = self.with_context(cleaned_ctx)

        super(AccountInvoice, self).invoice_validate()
        for invoice in self:
            if invoice.company_id.country_id != self.env.ref('base.co'):
                continue
            if invoice.type == 'in_invoice' or invoice.type == 'in_refund':
                invoice.l10n_co_send_state = "other"
                continue

            invoice._check_before_xml_exporting()

            invoice.invoice_generate_xml()
            invoice.l10n_co_send_state = "to_send"
            # invoice.send_pec_mail()

    def _check_before_xml_exporting(self):
        seller = self.company_id
        buyer = self.commercial_partner_id

        if not seller.country_id:
            raise UserError(_("%s must have a country") % seller.display_name)

        if not seller.vat:
            raise UserError(_("%s must have a NIF number") % seller.display_name)
        elif len(seller.vat) > 10:
            raise UserError(_("The maximum length for NIF number is 10. %s have a VAT number too long: %s.")
                            % (seller.display_name, seller.vat))

        if not seller.l10n_co_invoice_authorization:
            raise UserError(_("%s must have a invoice authorization") % seller.display_name)

        if not buyer.vat:
            raise UserError(_("The buyer, %s, or his company must have either a VAT number either a NIF")
                            % buyer.display_name)

    @api.multi
    def invoice_generate_xml(self):
        for invoice in self:
            if invoice.l10n_co_einvoice_id and invoice.l10n_co_send_state not in ['invalid', 'to_send']:
                raise UserError(
                    _("You can't regenerate an E-Invoice when the first one is sent and there are no errors"))
            if invoice.l10n_co_einvoice_id:
                invoice.l10n_co_einvoice_id.unlink()

            report_name = invoice.report_name()
            invoice.l10n_co_einvoice_name = report_name

            # data = b"<?xml version='1.0' encoding='UTF-8'?>" + invoice._export_as_xml()
            description = _('Colombian invoice: %s') % invoice.type
            invoice.l10n_co_einvoice_id = self.env['ir.attachment'].create({
                'name': report_name,
                'res_id': invoice.id,
                'res_model': invoice._name,
                # 'datas': base64.encodestring(data),
                'datas_fname': report_name,
                'description': description,
                'type': 'binary',
            })

            invoice.message_post(
                body=(_("E-Invoice is generated on %s by %s") % (fields.Datetime.now(), self.env.user.display_name))
            )

    @api.multi
    def report_name(self):
        seller = self.company_id
        report_name = ''
        etype = self.type
        # Type
        if etype == 'out_invoice':
            report_name += 'fv'
        elif etype == 'out_refund':
            report_name += 'nc'
        else:
            report_name += 'nd'
        # NIT
        report_name += str(seller.vat.zfill(10))
        # Codigo PT
        report_name += seller.l10n_co_code_pt
        # Digitos año
        if self.date_invoice:
            year = str(self.date_invoice.year)
        else:
            year = str(fields.date.today().year)
        report_name += year[-2:]
        # Consecutivo
        report_name += seller.l10n_co_sequence_id.next_by_id().zfill(8)
        report_name += '.xml'
        return report_name

    def _export_as_xml(self):
        ''' Create the xml file content.
        :return: The XML content as str.
        '''
        self.ensure_one()

        pdf = self.env.ref('account.account_invoices').render_qweb_pdf(self.id)[0]
        pdf = base64.b64encode(pdf)
        pdf_name = re.sub(r'\W+', '', self.number) + '.pdf'

        # Create file content.
        template_values = {
            'record': self,
            'pdf': pdf,
            'pdf_name': pdf_name,
        }
        content = self.env.ref('l10n_co_edi.account_invoice_co_FatturaPA_export').render(template_values)
        return content
