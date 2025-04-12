from odoo import models, fields, api


class Purchaseage(models.Model):
    _inherit = 'purchase.order'

    age = fields.Integer('Age')
    today= fields.Date('Today')