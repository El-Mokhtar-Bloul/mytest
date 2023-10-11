# -*- coding: utf-8 -*-
from odoo import models, fields

class AcpecLogementReportWizard(models.TransientModel):
    _name = 'acpec.logement.report.wizard'
    _description = 'acpec.logement.report.wizard'

    date_from = fields.Date(string='Date début',)
    date_to = fields.Date(string='Date fin',)
    logement_ids = fields.Many2many(
        comodel_name='sale.subscription',  # Replace with the actual model name
        relation='sale_subscription_acpec_logement_wiz_rel',
        column1='subscription_id',
        column2='logement_wiz_id',
        string='Contrats de Logements'
    )

    company_id = fields.Many2one('res.company', string='Company', required=True, readonly=True,
                                 default=lambda self: self.env.company)
    def generate_report(self):  
        data = {
            'date_from':self.date_from,
            'date_to':self.date_to,
            'logement_ids':self.logement_ids.ids,
            'company_id':self.company_id.id
        }
        return self.env.ref('acpec_logement.action_raport_abonnement').report_action(self, data=data)
        #raise models.ValidationError("%s"%data)
        