from odoo import models, fields, api


class RealEstate(models.Model):
    _name = 'estate.property.type'
    _description = 'real estate property type'

    name = fields.Char('Property Type', required=True, translate=True)