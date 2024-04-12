from database import DB


def get_connection(username, password):
    try:
        db = DB()
        us_name = db.view(table='admin_key', objects='username, password', where='username', value=username)
        name, password1 = us_name[0]
        if name == username and password == password1:
            return True
        else:
            return False
    except IndexError:
        return False
