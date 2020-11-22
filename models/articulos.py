# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Articulos(models.Model):
     _name = 'upoelectro.articulos'
     _description = 'Upoelectro articulos'
     
     name = fields.Integer('Identificador',required=True,help="Identificador del almacen")
     stock = fields.Integer("Stock")
     nombre = fields.Char("Nombre",required=True,help="Nombre del producto")
     tipoProducto = fields.Selection([('procesador','Procesador'),
                                     ('ram','RAM'),
                                     ('placabase','Placa base'),
                                     ('tarjetagrafica','Tarjeta Gráfica'),],
                                     'Tipo de producto')
     descripcion = fields.Char("Descripcion",required=True,help="Descripcion del producto")
     especificaciones = fields.Char("Especificaciones",required=True,help="Especificaciones del producto")
     
     almacenes_ids = fields.Many2many("upoelectro.almacenes",string="Almacenes")
