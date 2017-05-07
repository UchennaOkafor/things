# -*- coding: utf-8 -*-
from gluon.tools import Auth
from gluon.tools import prettydate

auth = Auth(db)

db.define_table(
    'devices',
    Field('name'),
    Field('description', 'text'),
    Field('picture', 'upload', autodelete=True),
    Field('created_at', default=request.now, writable=False),
    format = '%(name)s', singular='Device', plural='Devices')

db.devices.name.requires = IS_NOT_EMPTY()
db.devices.description.requires = IS_NOT_EMPTY()
db.devices.picture.requires = IS_IMAGE(extensions=('jpeg', 'png'))

db.define_table(
    'user_device',
    Field('name'),
    Field('user_id', db.auth_user),
    Field('device_type', db.devices),
    Field('description', 'text'),
    Field('is_on', 'boolean', default=False),
    Field('created_at', 'datetime', default=request.now, writable=False),
    format = '%(name)s', singular='User device', plural='User devices')

db.user_device.name.requires = IS_NOT_EMPTY()
db.user_device.user_id.requires = IS_IN_DB(db, db.auth_user.id)
db.user_device.device_type.requires = IS_IN_DB(db, db.devices.id)

db.define_table(
    'device_data',
    Field('user_device_id', db.user_device, writable=False, readable=False),
    Field('raw_data', 'text'),
    Field('created_at', 'datetime', default=request.now, writable=False))

db.device_data.user_device_id.requires = IS_IN_DB(db, db.user_device.id)
#db.device_data.raw_data.requires = IS_JSON()

#db.devices.drop()
#db.user_device.drop()
#db.device_data.drop()
