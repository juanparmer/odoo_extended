# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class res_users(models.Model):
    _inherit = 'res.users'

    @api.multi
    def create(self, vals):
        self.users_validation()
        return super(res_users, self).create(vals)

    @api.multi
    def write(self, vals):
        self.user_admin()
        if 'active' in vals:
            self.users_validation()
        return super(res_users, self).write(vals)

    @api.multi
    def unlink(self):
        self.user_admin()
        return super(res_users, self).unlink()

    @api.multi
    def users_validation(self):
        obj_ru = self.env['res.users']
        obj_imm = self.env['ir.module.module']
        user = self.env.user
        rus = obj_ru.search([('active', '=', 'True'), ('share', '=', False)])
        rus_num = len(rus)
        imm_web = obj_imm.search([('name', '=', 'website'), ('state', '=', 'installed')])
        imm_wsa = obj_imm.search([('name', '=', 'website_sale'), ('state', '=', 'installed')])
        rus_num = rus_num + 1 if imm_web else rus_num
        rus_num = rus_num + 1 if imm_wsa else rus_num
        num_rus = user.company_id.user_number
        if rus_num > num_rus:
            if user.id != 2:
                raise ValidationError("Your contract only allows you to have %s active users" % num_rus)

    @api.multi
    def user_admin(self):
        for user in self:
            if user.id == 2:
                if self.env.user.id != 2:
                    raise ValidationError("You cannot modify the admin user")
