from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

# ajouter les données fiscales à ma société/entreprise (my company)

class ResCompany(models.Model):
    _inherit = ['res.company']

    fax = fields.Char(
        string="Fax",
        size=64
    )

    capital_social = fields.Float(
        string="Capitale Social",
        digits='Account',
        required=True
    )

    # Numéro du registre de commerce
    nrc = fields.Char(
        string="N° RC"
    )

    # Numéro d’Identification Fiscal
    nif = fields.Char(
        string="N.I.F"
    )

    # Numéro d’Article
    ai = fields.Char(
        string="A.I"
    )

    # Numéro d’Identification Statistique
    nis = fields.Char(
        string="N.I.S"
    )

    # Forme juridique
    forme_juridique_company = fields.Many2one(
        comodel_name='forme.juridique',
        string='Forme Juridique'
    )



class BaseDocumentLayout(models.TransientModel):
    _inherit = 'base.document.layout'

    capital_social = fields.Float(related='company_id.capital_social', readonly=True)
    fax = fields.Char(related='company_id.fax', readonly=True)
    nrc = fields.Char(related='company_id.nrc', readonly=True)
    nif = fields.Char(related='company_id.nif', readonly=True)
    ai = fields.Char(related='company_id.ai', readonly=True)
    nis = fields.Char(related='company_id.nis', readonly=True)
    currency_id = fields.Many2one(related='company_id.currency_id', readonly=True)
    street = fields.Char(related='company_id.street', readonly=True)
    street2 = fields.Char(related='company_id.street2', readonly=True)
    zip = fields.Char(related='company_id.zip', readonly=True)
    city = fields.Char(related='company_id.city', readonly=True)
    state_id = fields.Many2one(related='company_id.state_id', readonly=True)
    country_id = fields.Many2one(related='company_id.country_id', readonly=True)