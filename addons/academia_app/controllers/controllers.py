#-*- coding: utf-8 -*-
from odoo import http


class AcademiaApp(http.Controller):
    @http.route('/academia_app/academia_app', auth='public')
    def index(self, **kw):
        return http.request.render('academia_app.navbar_toggler')

    #     })
    #
    # @http.route('/academia_app/academia_app/objects', auth='public')
    # def list(self, **kw):
    #     return http.request.render('academia_app.listing', {
    #         'root': '/academia_app/academia_app',
    #         'objects': http.request.env['academia_app.academia_app'].search([]),
    #     })
    #
    # @http.route('/academia_app/academia_app/objects/<model("academia_app.academia_app"):obj>', auth='public')
    # def object(self, obj, **kw):
    #     return http.request.render('academia_app.object', {
    #         'object': obj
    #     })

