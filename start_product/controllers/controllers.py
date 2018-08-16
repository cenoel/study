# -*- coding: utf-8 -*-
from odoo import http

# class StartProduct(http.Controller):
#     @http.route('/start_product/start_product/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/start_product/start_product/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('start_product.listing', {
#             'root': '/start_product/start_product',
#             'objects': http.request.env['start_product.start_product'].search([]),
#         })

#     @http.route('/start_product/start_product/objects/<model("start_product.start_product"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('start_product.object', {
#             'object': obj
#         })