# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class CrmProjectStages(models.Model):
    _name = 'crm.project.application.stages'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "name"

    name = fields.Char()


class CrmProjectBiddersRole(models.Model):
    _name = 'crm.project.application.role'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "name"

    name = fields.Char()


class CrmProject(models.Model):
    _name = 'crm.project.application'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char()
    description = fields.Text()
    stage_id = fields.Many2one('crm.project.application.stages', 'Stage')
    start_date = fields.Date(default=fields.Date.today())
    end_date = fields.Date()
    amount = fields.Float()

    application_line_ids = fields.One2many('project.application.line', 'crm_project_application_id', copy=True)
    contractor_line_ids = fields.One2many('contractor.lines', 'crm_project_application_id', copy=True)


class CrmProjectLines(models.Model):
    _name = 'project.application.line'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    crm_project_application_id = fields.Many2one('crm.project.application')
    name = fields.Char()
    start_date = fields.Date(default=fields.Date.today())
    end_date = fields.Date()
    description = fields.Text()


class WinnerLines(models.Model):
    _name = 'contractor.lines'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "contractor_id"

    crm_project_application_id = fields.Many2one('crm.project.application')
    application_id = fields.Many2one('project.application.line')
    contractor_id = fields.Many2one('res.partner')
    role_id = fields.Many2one('crm.project.application.role')
    involved_contact_id = fields.Many2one('res.partner', 'Involved Contact')

    # @api.onchange('is_bidder')
    # def onchange_is_bidder(self):
    #     bidders = []
    #     for record in self:
    #         bidder_id = self.env['bidder.lines'].search([('crm_project_id.id', '=', record.project_number)])
    #         print(bidder_id)
    #         for bidder in bidder_id:
    #             bidders.append(bidder.bidder_id.id)
    #     domain = {'company_id': [('id', 'in', bidders)]}
    #     return {'domain': domain}

    # @api.onchange('company_id')
    # def onchange_company_id(self):
    #     for record in self:
    #         bidders = self.env['bidder.lines'].search([('crm_project_id.id', '=', record.project_number),
    #                                                    ('bidder_id', '=', self.company_id.id)], limit=1)
    #         # print(bidders)
    #         record.company_role_id = bidders.bidder_role_id.id


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    crm_project_application_id = fields.Many2one('crm.project.application', 'Project')
    application_id = fields.Many2one('project.application.line')
    contractor_id = fields.Many2one('contractor.lines')
