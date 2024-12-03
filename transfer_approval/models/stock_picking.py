from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.exceptions import AccessError



class StockPicking(models.Model):
    _inherit = 'stock.picking'

    approval_state = fields.Selection([
        ('draft', 'Draft'),
        ('waiting_approval', 'Waiting Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string='Approval State', default='draft')

    def action_approve_transfer(self):
        if self.env.user.has_group('stock.group_stock_manager'):
            self.approval_state = 'approved'
        else:
            raise AccessError("You don't have the rights to approve this transfer.")

    @api.model
    def _get_picking_domain(self):
        if self.env.user.has_group('warehouse.group_warehouse_keeper'):
            return [('location_dest_id', 'in', self.env.user.allowed_location_ids.ids)]
        return []
