# Config
NODE_ID = ${NODE_ID}


# hour,set 0 to disable
SPEEDTEST = ${SPEEDTEST}
CLOUDSAFE = ${CLOUDSAFE}
ANTISSATTACK = ${ANTISSATTACK}
AUTOEXEC = ${AUTOEXEC}

MU_SUFFIX = '${MU_SUFFIX}'
MU_REGEX = '${MU_REGEX}'

SERVER_PUB_ADDR = '127.0.0.1'  # mujson_mgr need this to generate ssr link
API_INTERFACE = '${API_INTERFACE}'  # glzjinmod, modwebapi

WEBAPI_URL = '${WEBAPI_URL}'
WEBAPI_TOKEN = '${WEBAPI_TOKEN}'

# mudb
MUDB_FILE = 'mudb.json'

# Mysql
MYSQL_HOST = '${MYSQL_HOST}'
MYSQL_PORT = ${MYSQL_PORT}
MYSQL_USER = '${MYSQL_USER}'
MYSQL_PASS = '${MYSQL_PASS}'
MYSQL_DB = '${MYSQL_DB}'

MYSQL_SSL_ENABLE = 0
MYSQL_SSL_CA = ''
MYSQL_SSL_CERT = ''
MYSQL_SSL_KEY = ''

# API
API_HOST = '127.0.0.1'
API_PORT = 80
API_PATH = '/mu/v2/'
API_TOKEN = 'abcdef'
API_UPDATE_TIME = 60

# Manager (ignore this)
MANAGE_PASS = 'ss233333333'
# if you want manage in other server you should set this value to global ip
MANAGE_BIND_IP = '127.0.0.1'
# make sure this port is idle
MANAGE_PORT = 23333
