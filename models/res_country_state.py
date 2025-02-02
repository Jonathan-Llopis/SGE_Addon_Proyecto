from odoo import models, fields

class ResCountryState(models.Model):
    _inherit = 'res.country.state'
    
    country_id = fields.Many2one('res.country', string='Country', required=True)