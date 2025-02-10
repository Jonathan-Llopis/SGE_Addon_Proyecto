{
    "name": "Gestión Zoo",
    "version": "0.1",
    "category": "Zoo",
    "summary": "Gestión de zoológicos con funcionalidades específicas.",
    "description": """
    Módulo para la gestión de zoológicos:
    - Gestión de animales
    """,
    "author": "Jonathan Llopis",
    "license": "LGPL-3",
    "application": True,
    "depends": ["base", 'web'], 
    "data": [
        "security/ir.model.access.csv",
        "views/gestion_zoo_views.xml",
        "views/gestion_zoo_animal_views.xml",
        "views/gestion_zoo_especie_views.xml",
        "views/gestion_zoo_habitats_views.xml",
        "views/gestion_zoo_raza_views.xml",
        "views/gestion_zoo_menu.xml",
    ],

    "installable": True,
    "auto_install": False,
}
