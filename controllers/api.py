# -*- coding: utf-8 -*-

def devices():
    return db(db.devices).select().as_json()

def active_devices():
    devices = db(db.user_device.is_on == True).select(db.user_device.id, db.user_device.device_type)

    for device in devices:
        device.device_type = db(db.devices.id == device.device_type).select(db.devices.name).first().name

    return devices.as_json()

@auth.requires_login()
def device_data():
    return db(db.device_data.user_device_id == request.vars.user_device_id).select(db.device_data.raw_data, db.device_data.created_at).as_json()

@auth.requires_login()
def device_power():
    try:
        device_id = request.post_vars.device_id
        is_on = request.post_vars.is_on

        row = db(db.user_device.id == device_id).select().first()
        row.update_record(is_on = is_on)
    except Exception as ex:
        raise HTTP(500, "BAD REQUEST")

    raise HTTP(200, "OK")

@auth.requires_login()
def device_delete():
    try:
        device_id = request.post_vars.device_id
        db(db.user_device.id == device_id).delete()
    except Exception as ex:
        raise HTTP(500, "BAD REQUEST")

    raise HTTP(200, "OK")

#if device is on
#accept json
