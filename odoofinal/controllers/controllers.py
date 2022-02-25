# -*- coding: utf-8 -*-
# from odoo import http


# class odoofinal(http.Controller):
#     @http.route('/odoofinal/odoofinal/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoofinal/odoofinal/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoofinal.listing', {
#             'root': '/odoofinal/odoofinal',
#             'objects': http.request.env['odoofinal.odoofinal'].search([]),
#         })

#     @http.route('/odoofinal/odoofinal/objects/<model("odoofinal.odoofinal"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoofinal.object', {
#             'object': obj
#         })
