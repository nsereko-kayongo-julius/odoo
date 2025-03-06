
from odoo import models, fields, api, exceptions


class RealEstate(models.Model):
    _name = 'real_estate_property'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'real estate property for advertisement'

    name = fields.Char('Estate Name', required=True, translate=True, tracking=True,)
    description = fields.Text('Estate Description', required=True, translate=True, tracking=True,)
    postcode = fields.Char('Estate Postcode',tracking=True,)
    date_availability = fields.Date('Estate Available On')
    expected_price = fields.Float('Estate Expected Price' )
    selling_price = fields.Float('Estate Selling Price')
    bedrooms = fields.Integer('Bedrooms')
    living_area = fields.Integer('Living Area')
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage', default=True, tracking=True,)
    garden_area = fields.Integer('Garden Area')
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('north','North'),('south','South'),('east','East'),('west','West')]
        )
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")

    total_area = fields.Integer('Total Area', compute='_compute_total_area')
    state= fields.Selection(        
        [('new','New property'),('cancel', 'Cancel'),('sold','Sold')],        
        default='new', string='Status'
    )

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    def action_cancel(self):
        for record in self:
            if record.state == 'sold':
                raise exceptions.UserError('This property is already sold it cannot be cancelled')
            record.state = 'cancel'
        return True
    
    def action_sold(self):
        for record in self:
            if record.state == 'cancel':
                raise exceptions.UserError('This property is already cancelled it cannot be sold')
            record.state = 'sold'
        return True
    