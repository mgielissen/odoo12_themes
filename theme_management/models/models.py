# -- encoding: utf-8 --
# This module and its content is copyright of Technaureus Info Solutions Pvt. Ltd.
# - © Technaureus Info Solutions Pvt. Ltd 2019. All rights reserved.
import json
from odoo import models, fields, api, SUPERUSER_ID

class website(models.Model):
    _inherit = 'website'

    def get_latest_blog_posts(self):
        print("blog_posts")
        blog_posts = self.env['blog.post'].sudo().search(
        [('website_published', '=', True)], order='id DESC')
        print(blog_posts)
        return blog_posts

    def get_cover_image(self, blog_post):
        print("blog_post")
        return json.loads(blog_post.cover_properties).get('background-image')[4:-1]

class IrModuleModule(models.Model):
    _name = "ir.module.module"
    _description = 'Module'
    _inherit = _name

    @api.model
    def _theme_remove(self, website):
        if website.theme_id.name == "theme_management":
            # default homepage set when un-install theme grocery
            env = api.Environment(self.env.cr, SUPERUSER_ID, {})
            default_website = env.ref('website.default_website', raise_if_not_found=False)
            default_homepage = env.ref('website.homepage_page', raise_if_not_found=False)
            default_website.homepage_id = default_homepage.id
        return super(IrModuleModule, self)._theme_remove(website)
