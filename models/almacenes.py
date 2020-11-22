# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Almacenes(models.Model):
     _name = 'upoelectro.almacenes'
     _description = 'Upoelectro almacenes'

     
     name = fields.Char('Direccion Almacen',required=True,help="Direccion del almacen")
     capacidad = fields.Integer("Capacidad")
     
     articulos_ids = fields.Many2many("upoelectro.articulos",String="Articulos")