# -*- coding: utf-8 -*-

@auth.requires_login()
def index():
    device_rows = db((db.user_device.user_id == auth.user.id) & (db.devices.id == db.user_device.device_type)).select()
    return dict(rows = device_rows)

@auth.requires(auth.has_membership(role="admin"))
def admin():
    return dict(grid = SQLFORM.smartgrid(db.devices))

@auth.requires_login()
def form():
    id = request.args(0)
    action_add = id == None or id.isdigit() == False
    device_info = None if action_add else db(db.user_device.id == id).select().first()

    if id != None and device_info is None:
        redirect(URL("form"))

    if request.env.request_method == "POST":
        if request.post_vars.action == "Add":
            try:
                device_id = db.user_device.insert(user_id = auth.user.id, device_type = request.post_vars.device_type,
                        name = request.post_vars.name, description = request.post_vars.description)
                db.device_data.insert(user_device_id = device_id)
                response.flash = "Device created successfully"
            except Exception as ex:
                response.flash = "Error creating device. Try again"
        elif request.post_vars.action == "Edit":
            try:
                row = db(db.user_device.id == id).select().first()
                row.update_record(device_type = request.post_vars.device_type,
                        name = request.post_vars.name, description = request.post_vars.description)
                device_info = db(db.user_device.id == id).select().first()
                response.flash = "Device updated successfully"
            except Exception as ex:
                response.flash = "Error editing device. Try again"

    return dict(action_add = action_add, device_info = device_info, devices = db().select(db.devices.ALL))

@auth.requires_login()
def view():
    id = request.args(0)

    if id == None or id.isdigit() == False:
        return dict(user_device = None)

    user_device = db((db.user_device.id == id) & (db.user_device.user_id == auth.user.id)).select()
    user_device = user_device.first() if len(user_device) == 1 else None

    return dict(user_device = user_device)
