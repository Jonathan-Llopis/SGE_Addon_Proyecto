# -*- coding: utf-8 -*-

from odoo import models, fields, api

class GestionZooEspecie(models.Model):
    _name = "gestion.zoo.especie"
    _description = "Gestión Zoo Especie"

    nombre_vulgar = fields.Char(required=True)
    nombre_cientifico = fields.Char(required=True)
    peligro_extincion = fields.Boolean(default=False, string="Peligro Extinción")
    dieta = fields.Selection(selection=(("carnivora","Carnívora"),
                                        ("herbivora", "Herbívora"),
                                        ("omnivora","Omnívora")), required=True, default = "carnivora")
    grado_peligro = fields.Selection(selection=((1, "Seguro"),
                                                (2,"Riesgo Bajo"),
                                                (3, "Riesgo Moderado"),
                                                (4, "Peligroso"),
                                                (5,"Altamente Peligroso"),
                                                (6, "Peligro Crítico/Ecológico")),  required=True, default = 1)
    
    familia = fields.Selection(selection=(  ('mamifero', 'Mamíferos'),
                                            ('ave', 'Aves'),
                                            ('reptil', 'Reptiles'),
                                            ('anfibio', 'Anfibios'),
                                            ('pez', 'Peces'),
                                            ('insecto', 'Insectos'),
                                            ('aracnido', 'Arácnido'),
                                            ('crustaceo', 'Crustáceo'),
                                            ('molusco', 'Molusco')), default = "mamifero")
    color_dieta = fields.Integer(
        string="Color Dieta", compute="_compute_color_dieta", store=True
    )
    color_grado_peligro = fields.Integer(
        string="Color Grado Peligro", compute="_compute_color_grado_peligro", store=True
    )
    color_familia = fields.Integer(
        string="Color Familia", compute="_compute_color_familia", store=True
    )
    
    _sql_constraints = [
            ('nombre_vulgar_subfamily_unique', 'unique(nombre_vulgar)', 'El nombre vulgar debe ser único'),
            ('nombre_cientifico_subfamily_unique', 'unique(nombre_cientifico)', 'El nombre cientifico debe ser único'),
    ]
        
        # Relacions proposades:
            #(M-1)Familia, (M-1) SubFamilia, (M-1)Peligro 
            
    @api.depends('dieta')
    def _compute_color_dieta(self):
        for record in self:
            if record.dieta == 'carnivora':
                record.color_dieta = 2  
            elif record.dieta == 'herbivora':
                record.color_dieta = 10 
            elif record.dieta == 'omnivora':
                record.color_dieta = 6
            else:
                record.color_dieta = 0

    @api.depends('grado_peligro')
    def _compute_color_grado_peligro(self):
        for record in self:
            color_map = {
                1: 10, 
                2: 3,
                3: 6,
                4: 5,
                5: 2,
                6: 9
            }
            record.color_grado_peligro = color_map.get(record.grado_peligro, 0)

    @api.depends('familia')
    def _compute_color_familia(self):
        for record in self:
            color_map = {
                'mamifero': 1,
                'ave': 2,
                'reptil': 3,
                'anfibio': 4,
                'pez': 6,
                'insecto': 7,
                'aracnido': 9,
                'crustaceo': 8,
                'molusco': 5,
            }
            record.color_familia = color_map.get(record.familia, 0)