from odoo import models, fields

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    
    compras_zoo=fields.Many2one("gestion.zoo", required=True)