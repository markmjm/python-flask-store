from werkzeug.security import safe_str_cmp
from user import User

users = [
    User(1, 'bob', 'bobpassword'),
    User(2, 'user2', 'abcxyz'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):  #once a jwt is obtained, then in next sent it in next request to identity
    user_id = payload['identity']
    return userid_table.get(user_id, None)