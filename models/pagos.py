# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Pagos(models.Model):
     _name = 'upoelectro.pagos'
     _description = 'Upoelectro pagos'

     fecha = fields.Datetime('Fecha de pago',required=True,autodate=True)
     cantidad = fields.Integer("Importe")
     
     pedido_id = fields.Many2one("upoelectro.pedidos",String="Pedido")
     