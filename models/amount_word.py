# -*- coding: utf-8 -*-
from odoo import api, fields, models
from datetime import datetime


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # @api.multi
    def _compute_amount_in_word(self):
        for rec in self:
            rec.num_word = str(rec.currency_id.amount_to_text(rec.amount_total))

    num_word = fields.Char(compute='_compute_amount_in_word')


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    # @api.multi
    def _compute_amount_in_word(self):
        for rec in self:
            rec.num_word = str(rec.currency_id.amount_to_text(rec.amount_total))

    num_word = fields.Char(compute='_compute_amount_in_word')


class InvoiceOrder(models.Model):
    _inherit = 'account.move'

    # @api.multi
    def _compute_amount_in_word(self):
        for rec in self:
            rec.num_word = str(rec.currency_id.amount_to_text(rec.amount_total))

    num_word = fields.Char(compute='_compute_amount_in_word')
