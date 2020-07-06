# -*- coding: utf-8 -*-
#This module and its content is copyright of Technaureus Info Solutions Pvt.Ltd.
# - © Technaureus Info Solutions Pvt. Ltd 2019. All rights reserved.
{
  'name':'Theme Management',
  'description': 'Odoo website template of management consultancy.',
  'version':'1.0',
  'author':'Technaureus Info Solutions Pvt.Ltd.',
  'website':'https://www.technaureus.com',
  'sequence':1,

  'data': [
      'views/f_h_management.xml',
      'views/homepage_management.xml'


  ],
    'images':['static/description/theme_management_screenshot.jpg'],
    'category': 'Theme/Creative',
  'depends': ['website', 'website_theme_install', 'website_blog'],
}