# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Pedidos(models.Model):
     _name = 'upoelectro.pedidos'
     _description = 'Upoelectro pedidos'

     fechaPedido = fields.Datetime('Fecha del pedido',required=True,autodate=True)
     cantidadTotal = fields.Integer("Importe Total")
     pagado = fields.Boolean('Pagado', default=False)

     pagos_ids = fields.One2many("upoelectro.pagos","pedido_id",String="Pagos Confirmados")
     cliente_id = fields.Many2one("upoelectro.clientes",string="Cliente")