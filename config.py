import datetime

DEBUG = True
TESTING = False
SECRET_KEY = 'qwertyuio*&$#@#$%xcvbnmJHGFD6454654'

# Mongo Conexion
MONGODB_DB = 'marketplace'
MONGODB_HOST = 'mongodb+pymongo://localhost:27017/marketplace'
# MONGODB_PORT = 27017
# MONGODB_USERNAME = 'webapp'
# MONGODB_PASSWORD = 'pwd123'

# JWT Token
JWT_SECRET_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6Ikpva' \
                               'G4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'
JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=1)


