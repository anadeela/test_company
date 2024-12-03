# -*- coding: utf-8 -*-
# from odoo import http


# class TransferApproval(http.Controller):
#     @http.route('/transfer_approval/transfer_approval', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/transfer_approval/transfer_approval/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('transfer_approval.listing', {
#             'root': '/transfer_approval/transfer_approval',
#             'objects': http.request.env['transfer_approval.transfer_approval'].search([]),
#         })

#     @http.route('/transfer_approval/transfer_approval/objects/<model("transfer_approval.transfer_approval"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('transfer_approval.object', {
#             'object': obj
#         })
