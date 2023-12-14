import re

from odoo import models, fields, api
from odoo.exceptions import ValidationError



# Ajouter les données fiscales à partner (client or fournisseur)
class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Position Fiscale
    position_fiscale = fields.Many2one(
        comodel_name='account.fiscal.position',
        string='Position Fiscale'
    )

    # Numéro du registre de commerce.
    nrc = fields.Char(
        string='N° RC'
    )

    # Numéro d’Identification Fiscal
    nif = fields.Char(
        string='N.I.F'
    )

    # Numéro d’Article
    ai = fields.Char(
        string='A.I'
    )

    # Numéro d’Identification Statistique
    nis = fields.Char(
        string='N.I.S'
    )

    # Fax number
    fax = fields.Char(
        string='Fax'
    )
