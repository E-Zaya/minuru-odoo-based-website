# -*- coding: utf-8 -*-
from odoo import fields, models


class MinuruApplication(models.Model):
    _name = "minuru.application"
    _description = "Minuru Expedition Application"
    _order = "submitted_at desc, id desc"

    name = fields.Char(required=True)
    email = fields.Char()
    phone = fields.Char()
    country = fields.Char()
    age = fields.Integer()
    group_size = fields.Char()
    expedition = fields.Char()
    preferred_month = fields.Char()
    vip_service = fields.Char()
    offroad_experience = fields.Char()
    driving_experience = fields.Char()
    physical_fitness = fields.Char()
    expectations = fields.Text()
    special_requests = fields.Text()
    risk_accepted = fields.Boolean()
    source_url = fields.Char()
    user_agent = fields.Char()
    submitted_at = fields.Datetime(default=fields.Datetime.now, readonly=True)
    state = fields.Selection(
        [
            ("new", "New"),
            ("contacted", "Contacted"),
            ("confirmed", "Confirmed"),
            ("declined", "Declined"),
        ],
        default="new",
        required=True,
    )

    def action_mark_contacted(self):
        self.write({"state": "contacted"})

    def action_mark_confirmed(self):
        self.write({"state": "confirmed"})

    def action_mark_declined(self):
        self.write({"state": "declined"})
