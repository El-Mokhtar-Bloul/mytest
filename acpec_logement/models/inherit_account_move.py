# -*- coding: utf-8 -*-
from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    subscription_id = fields.Many2one(comodel_name='sale.subscription', string="Contrat logement", copy=True)

