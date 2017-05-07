# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# Customize your APP title, subtitle and menus here
# ----------------------------------------------------------------------------------------------------------------------

response.logo = A(B('ioThings'), XML('&trade;&nbsp;'), _class="navbar-brand", _href= URL(request.application, 'default', 'index'))
response.title = request.application.replace('_', ' ').title()
response.subtitle = ''

# ----------------------------------------------------------------------------------------------------------------------
# read more at http://dev.w3.org/html5/markup/meta.name.html
# ----------------------------------------------------------------------------------------------------------------------
response.meta.author = myconf.get('app.author')
response.meta.description = myconf.get('app.description')
response.meta.keywords = myconf.get('app.keywords')
response.meta.generator = myconf.get('app.generator')

# ----------------------------------------------------------------------------------------------------------------------
# your http://google.com/analytics id
# ----------------------------------------------------------------------------------------------------------------------
response.google_analytics_id = None

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [[T('Home'), False,  URL(request.application, 'default', 'index')]]

if auth.is_logged_in():
    response.menu.append([T('My Devices'), False,  URL(request.application, 'devices', 'index')])
    if auth.has_membership(role="admin"):
        response.menu.append([T('Manage Devices'), False,  URL(request.application, 'devices', 'admin')])

DEVELOPMENT_MENU = False

if "auth" in locals():
    auth.wikimenu()
