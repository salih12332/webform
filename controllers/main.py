from odoo.http import request, Controller, route
class WebFormController(Controller):
    @route('/webform', auth='public', website=True)
    def web_form(self, **kwargs):
        return request.render('webform.web_form_template')
    @route('/webform/submit', type='http', auth='public', website=True)
    def web_form_submit(self, **post):
        request.env['custom.web.form.booking'].sudo().create({
                    'name': post.get('name'),
                    'phone': post.get('phone'),
                    'email': post.get('email'),
                })
        return request.redirect('thank-you-page')