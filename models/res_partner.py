# -*- encoding: utf-8 -*-

from odoo import models, fields, api, _
import logging

class Partner(models.Model):
    _inherit = "res.partner"

    nombre_facturacion_fel = fields.Char('Nombre facturación FEL', copy=False)
    frases_fel = fields.Text('Frases', copy=False, help="Las frases dependen del RTU de la empresa, para agregarlas debe separar por una coma (TipoFrase,CodigoEscenario) en caso de tener más de una frase precione Eneter e ingrese la nueva frase.")
