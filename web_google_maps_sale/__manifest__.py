# -*- coding: utf-8 -*-
# Copyright 2017 Graeme Gellatly
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Web Google Maps Sale',
    'description': """
        Adds map view for partner_shipping_id to sale order""",
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Graeme Gellatly',
    'website': 'https://o4sb.com',
    'depends': [
        'web_google_maps',
        'sale',
    ],
    'data': [
        'views/sale_order.xml',
    ],
    'demo': [
    ],
}
