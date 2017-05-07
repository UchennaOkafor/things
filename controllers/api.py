# -*- coding: utf-8 -*-

def devices():
    return db(db.devices).select().as_json()

def device_data():
    return db(db.device_data.user_device_id == request.vars.user_device_id).select(db.device_data.raw_data, db.device_data.created_at).as_json()

def active_devices():
    return db(db.user_device.is_on == True).select().as_json()

def simulate_device():
    return False

def test_method():
    return False

def device_power():
    try:
        device_id = request.post_vars.device_id
        is_on = request.post_vars.is_on

        row = db(db.user_device.id == device_id).select().first()
        row.update_record(is_on = is_on)
    except Exception as ex:
        raise HTTP(500, "BAD REQUEST")

    raise HTTP(200, "OK")

def device_delete():
    try:
        device_id = request.post_vars.device_id
        db(db.user_device.id == device_id).delete()
    except Exception as ex:
        raise HTTP(500, "BAD REQUEST")

    raise HTTP(200, "OK")

#if device is on
#accept json
