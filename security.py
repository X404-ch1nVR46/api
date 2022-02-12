from users import Users

users = [
    Users(1,'user1','passcode123'),
    Users(2,'user2','passcode234')
]

# Username mapping to instantly access username of a user from teh authneticate function for JWT
username_mapping = { u.username : u for u in users}

# Username mapping to instantly access userid of a user from the identity function for JWT
userid_mapping = {u.id : u for u in users}

# Authentication Handler
def authenticate(username, password):
    user = username_mapping.get(username,None)
    if user and user.password == password:
        return user

# Identity Handler
def identity(payload):
    userid = payload['identity']
    return userid_mapping.get(userid, None)