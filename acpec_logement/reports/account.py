from odoo import models, api
from odoo.exceptions import ValidationError


class LogementAnalyseXlsx(models.AbstractModel):
	_name = 'report.acpec_logement.template_raport_abonnement'
	_description = 'Reports des accounts'

	@api.model
	def _get_report_values(self, docids, data = None):
		logement_ids = data.get("logement_ids")
		date_from = data.get('date_from', False) or '1900-01-01'
		date_to = data.get('date_to', False) or '3000-01-01'
		company = data.get('company_id', False)
		domain_dep = [('date', '>=', date_from), ('date', '<=', date_to)]
		domain_rev = [('date', '>=', date_from), ('date', '<=', date_to)]
		if company :
			domain_dep += [('company_id', '=',company )]
			domain_rev += [('company_id', '=',company )]
		if logement_ids:
			domain_dep += [('subscription_id', 'in', logement_ids )]
			domain_rev +=	[('invoice_line_ids.subscription_id', 'in', logement_ids)]

		expense_move_ids = self.env['account.move'].search(domain_dep)

		invoice_ids = self.env['account.move'].search(domain_rev)

		liste = []
		liste_subscriptions = expense_move_ids.mapped('subscription_id') | invoice_ids.mapped('invoice_line_ids.subscription_id')
		for s in liste_subscriptions:
			exp = expense_move_ids.filtered(lambda e: e.subscription_id == s)
			inv = invoice_ids.filtered(lambda e: e.invoice_line_ids.subscription_id == s)
			valus = {
				'subscription': s.display_name,
				'partner': s.partner_id.name,
				'total_rev': sum(f.amount_total for f in inv),
				'total_dep': sum(f.amount_total for f in exp),
				'difference': sum(f.amount_total for f in inv) - sum(f.amount_total for f in exp)
			}
			liste.append(valus)

		#for move in expense_move_ids:
		#raise ValidationError("%s"%liste)

		return {
			'doc_ids': docids,
			'liste': liste,
			'date_from': data.get("date_from"),
			'date_to': data.get("date_to"),
            'company_id':self.env.company
		}
