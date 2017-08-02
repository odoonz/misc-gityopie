# -*- coding: utf-8 -*-
# Copyright 2017 Graeme Gellatly
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    partner_latitude = fields.Float(
        string='Geo Latitude',
        digits=(16, 5),
        related='partner_shipping_id.partner_latitude',
    )
    partner_longitude = fields.Float(
        string='Geo Longitude',
        digits=(16, 5),
        related='partner_shipping_id.partner_longitude',
    )
