# -*- coding: utf-8 -*-

from odoo import models, fields, api

class GestionZoo(models.Model):
    _name = "gestion.zoo"
    _description = "Gestión Zoo"

    nombre = fields.Char()
    ciudad = fields.Char()
    extension = fields.Float(string="Extensión")
    unidad_extension = fields.Selection(selection=(("m", "Metros Cuadrados"), ("h", "Hectárea")),
                                        string="Unidad de Extensión", default="m")
    tipo = fields.Selection(selection=(("tradicional", "Tradicional"), ("safari", "Safari"), ("especializado","Especializado"), ("bioparque", "Bioparque"), 
                                       ("acuario", "Acuario"), ))
   
    
    @api.onchange('unidad_extension', 'extension')
    def _onchange_(self):
        if self.extension:
            if self.unidad_extension == 'm':
                 self.extension == self.extension*10000
            elif self.unidad_extension == 'h':
                self.extension == self.extension/10000
    # Relacions proposades:
        # (M-1)Provincia, (M-1)Pais, (1-M)Animal
        
