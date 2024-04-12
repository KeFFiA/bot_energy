import sqlite3

from database_utils.classes import DB

dictionary = {
    "objects": "username, password",
    "types": 'object1, object2',
    'some': 'object10, object20'
}


# for i in dictionary:
#     print(dictionary[i])

# for i in dictionary:
#     if i == 'objects':
#         obj = dictionary[i]
#         print('objects:', obj)
#     elif i == 'types':
#         types = dictionary[i]
#         print('obj + types:', obj, types)
#     else:
#         print('error')


###############################

def view(table, where, value):
    print('table:', table)
    print('where:', where)
    print('value:', value)


# view(table='table', where='where', value='a, b, c')


def db(objects, wheres, values):
    connect = sqlite3.connect('database/Energy.db')
    cursor = connect.cursor()
    values = values.split(sep=', ')
    wheres = wheres.split(sep=', ')
    for i in range(len(values)):
        cursor.execute(f"UPDATE admin_key SET {objects}='{values[i]}' WHERE {objects}='{wheres[i]}'")
    connect.commit()


def view():
    connect = sqlite3.connect('database/Energy.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM admin_key WHERE username="KeFFiA"')
    result = cursor.fetchall()
    return result


# print(db(objects='username', values='KeFFiA, aaaaaa', wheres='KeFFaa, aaaaaaaaaaaaaaaaaa'))
# print(view())


def user_exists(user_id: str) -> bool:
    db = DB()
    try:
        check_user_id = db.view(table='users', objects='user_id', where='user_id', value=f'{str(user_id)}')[0]
        print(check_user_id)
    except:
        return True
    for i in check_user_id:
        try:
            if user_id in i:
                return False
            else:
                return True
        except:
            return True


print(user_exists('409445811'))
