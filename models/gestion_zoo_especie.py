# -*- coding: utf-8 -*-

from odoo import models, fields, api

class GestionZooEspecie(models.Model):
    _name = "gestion.zoo.especie"
    _description = "Gestión Zoo Especie"

    nombre_vulgar = fields.Char(required=True)
    nombre_cientifico = fields.Char(required=True)
    peligro_extincion = fields.Boolean(default=False, string="Peligro Extinción")
    dieta = fields.Selection(selection=(("canrivora","Carnívora"),
                                        ("herbivora", "Herbívora"),
                                        ("omnivora","Omnívora")), required=True)
    grado_peligro = fields.Selection(selection=((1, "Seguro"),
                                                (2,"Riesgo Bajo"),
                                                (3, "Riesgo Moderado"),
                                                (4, "Peligroso"),
                                                (5,"Altamente Peligroso"),
                                                (6, "Peligro Crítico/Ecológico")),  required=True)
    
    familia = fields.Selection(selection=(  ('mamifero', 'Mamíferos'),
                                            ('ave', 'Aves'),
                                            ('reptil', 'Reptiles'),
                                            ('anfibio', 'Anfibios'),
                                            ('pez', 'Peces'),
                                            ('insecto', 'Insectos'),
                                            ('aracnido', 'Arácnido'),
                                            ('crustaceo', 'Crustáceo'),
                                            ('molusco', 'Molusco')))
     
    _sql_constraints = [
            ('nombre_vulgar_subfamily_unique', 'unique(nombre_vulgar)', 'El nombre vulgar debe ser único'),
            ('nombre_cientifico_subfamily_unique', 'unique(nombre_cientifico)', 'El nombre cientifico debe ser único'),
    ]
        
        # Relacions proposades:
            #(M-1)Familia, (M-1) SubFamilia, (M-1)Peligro 