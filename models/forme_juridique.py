from odoo import models,fields


class FormeJuridique(models.Model):
    _name = 'forme.juridique'

    name = fields.Char(
        string="Nom",
        required=True
    )

    code = fields.Char(
        string="Code"
    )