# -*- coding: utf-8 -*-
from odoo import http

# class ThemeManagement(http.Controller):
#     @http.route('/theme_management/theme_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/theme_management/theme_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('theme_management.listing', {
#             'root': '/theme_management/theme_management',
#             'objects': http.request.env['theme_management.theme_management'].search([]),
#         })

#     @http.route('/theme_management/theme_management/objects/<model("theme_management.theme_management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('theme_management.object', {
#             'object': obj
#         })