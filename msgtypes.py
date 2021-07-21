from direct.distributed.MsgTypes import *

# STATESERVER message types
STATESERVER_OBJECT_GENERATE_WITH_REQUIRED = 2001
STATESERVER_OBJECT_GENERATE_WITH_REQUIRED_OTHER = 2003
STATESERVER_OBJECT_UPDATE_FIELD = 2004
STATESERVER_OBJECT_UPDATE_FIELD_MULTIPLE = 2005
STATESERVER_OBJECT_DELETE_RAM = 2007
STATESERVER_OBJECT_SET_ZONE = 2008
STATESERVER_OBJECT_CHANGE_ZONE = 2009
STATESERVER_OBJECT_NOTFOUND = 2015
STATESERVER_QUERY_OBJECT_ALL = 2020
STATESERVER_QUERY_ZONE_OBJECT_ALL = 2021
STATESERVER_OBJECT_LOCATE = 2022
STATESERVER_OBJECT_LOCATE_RESP = 2023
STATESERVER_OBJECT_QUERY_FIELD = 2024 # See 2062
STATESERVER_QUERY_OBJECT_ALL_RESP = 2030
STATESERVER_SHARD_REST = 2061
STATESERVER_ADD_AI_RECV = 2045
STATESERVER_QUERY_ZONE_OBJECT_ALL_DONE = 2046
STATESERVER_OBJECT_CREATE_WITH_REQUIRED_CONTEXT = 2050
STATESERVER_OBJECT_CREATE_WITH_REQUIR_OTHER_CONTEXT = 2051
STATESERVER_OBJECT_CREATE_WITH_REQUIRED_CONTEXT_RESP = 2052
STATESERVER_OBJECT_CREATE_WITH_REQUIR_OTHER_CONTEXT_RESP = 2053
STATESERVER_OBJECT_DELETE_DISK = 2060
STATESERVER_OBJECT_QUERY_FIELD_RESP = 2062 # See 2024
STATESERVER_OBJECT_ENTERZONE_WITH_REQUIRED_OTHER = 2066
STATESERVER_OBJECT_ENTER_AI_RECV = 2067
STATESERVER_OBJECT_LEAVING_AI_INTEREST = 2033 # This is the new name for 2033
STATESERVER_OBJECT_ENTER_OWNER_RECV = 2068 # new obj with owner
STATESERVER_OBJECT_CHANGE_OWNER_RECV = 2069 # obj has new owner
STATESERVER_OBJECT_SET_OWNER_RECV = 2070 # ???
STATESERVER_OBJECT_QUERY_FIELDS = 2080
STATESERVER_OBJECT_QUERY_FIELDS_RESP = 2081
STATESERVER_OBJECT_QUERY_FIELDS_STRING = 2082
STATESERVER_OBJECT_QUERY_MANAGING_AI = 2083 # Should not be received by python code (it's for roger's server) 
STATESERVER_BOUNCE_MESSAGE = 2086
STATESERVER_QUERY_OBJECT_CHILDREN_LOCAL = 2087
STATESERVER_QUERY_OBJECT_CHILDREN_LOCAL_DONE = 2089
STATESERVER_QUERY_OBJECT_CHILDREN_RESP = 2087       

# CONTROL messages
CONTROL_MESSAGE =               4001
CONTROL_SET_CHANNEL =           2001
CONTROL_REMOVE_CHANNEL =        2002
CONTROL_SET_CON_NAME =          2004
CONTROL_SET_CON_URL =           2005
CONTROL_ADD_RANGE   =         2008
CONTROL_REMOVE_RANGE  =       2009
CONTROL_ADD_POST_REMOVE   =   2010 # ADD A MESSAGE TO THE CLOSING EVENT ON A DIRECTOR SOCKET
CONTROL_CLEAR_POST_REMOVE =   2011 # CLEAR ALL THE EVENTS..

# CLIENT messages
CLIENT_LOGIN = 1
CLIENT_LOGIN_RESP = 2
CLIENT_GET_AVATARS = 3
CLIENT_GO_GET_LOST = 4
CLIENT_GET_AVATARS_RESP = 5
CLIENT_CREATE_AVATAR = 6
CLIENT_CREATE_AVATAR_RESP = 7
CLIENT_GET_FRIEND_LIST = 10
CLIENT_GET_FRIEND_LIST_RESP = 11
CLIENT_GET_AVATAR_DETAILS = 14
CLIENT_GET_AVATAR_DETAILS_RESP = 15
CLIENT_LOGIN_2 = 16
CLIENT_LOGIN_2_RESP = 17
CLIENT_OBJECT_UPDATE_FIELD = 24
CLIENT_OBJECT_UPDATE_FIELD_RESP = 24
CLIENT_OBJECT_DISABLE = 25
CLIENT_OBJECT_DISABLE_RESP = 25
CLIENT_OBJECT_DISABLE_OWNER = 26
CLIENT_OBJECT_DISABLE_OWNER_RESP = 26
CLIENT_OBJECT_DELETE = 27
CLIENT_OBJECT_DELETE_RESP = 27
CLIENT_SET_ZONE_CMU = 29
CLIENT_REMOVE_ZONE = 30
CLIENT_SET_AVATAR = 32
CLIENT_CREATE_OBJECT_REQUIRED = 34
CLIENT_CREATE_OBJECT_REQUIRED_RESP = 34
CLIENT_CREATE_OBJECT_REQUIRED_OTHER = 35
CLIENT_CREATE_OBJECT_REQUIRED_OTHER_RESP = 35
CLIENT_CREATE_OBJECT_REQUIRED_OTHER_OWNER = 36
CLIENT_CREATE_OBJECT_REQUIRED_OTHER_OWNER_RESP = 36
CLIENT_REQUEST_GENERATES = 36
CLIENT_DISCONNECT = 37
CLIENT_GET_STATE_RESP = 47
CLIENT_DONE_INTEREST_RESP = 48
CLIENT_DELETE_AVATAR = 49
CLIENT_DELETE_AVATAR_RESP = 5
CLIENT_HEARTBEAT = 52
CLIENT_FRIEND_ONLINE = 53
CLIENT_FRIEND_OFFLINE = 54
CLIENT_REMOVE_FRIEND = 56
CLIENT_CHANGE_PASSWORD = 65
CLIENT_SET_NAME_PATTERN = 67
CLIENT_SET_NAME_PATTERN_ANSWER = 68
CLIENT_SET_WISHNAME = 70
CLIENT_SET_WISHNAME_RESP = 71
CLIENT_SET_WISHNAME_CLEAR = 72
CLIENT_SET_SECURITY = 73
CLIENT_SET_DOID_RANGE = 74
CLIENT_GET_AVATARS_RESP2 = 75
CLIENT_CREATE_AVATAR2 = 76
CLIENT_SYSTEM_MESSAGE = 78
CLIENT_SET_AVTYPE = 80
CLIENT_GET_PET_DETAILS = 81
CLIENT_GET_PET_DETAILS_RESP = 82
CLIENT_ADD_INTEREST = 97
CLIENT_REMOVE_INTEREST = 99
CLIENT_OBJECT_LOCATION = 102
CLIENT_LOGIN_3 = 111
CLIENT_LOGIN_3_RESP = 110
CLIENT_GET_FRIEND_LIST_EXTENDED = 115
CLIENT_GET_FRIEND_LIST_EXTENDED_RESP = 116
CLIENT_SET_FIELD_SENDABLE = 120
CLIENT_SYSTEMMESSAGE_AKNOWLEDGE = 123
CLIENT_CHANGE_GENERATE_ORDER = 124
CLIENT_LOGIN_TOONTOWN = 125
CLIENT_LOGIN_TOONTOWN_RESP = 126  

# CLIENT token types
CLIENT_LOGIN_2_GREEN = 1       # Disney's GoReg subscription token, not used.
CLIENT_LOGIN_2_PLAY_TOKEN = 2  # VR Studio PlayToken.
CLIENT_LOGIN_2_BLUE = 3        # The international GoReg token.
CLIENT_LOGIN_3_DISL_TOKEN = 4  # SSL encoded blob from DISL system.

# DBSERVER messages
DBSERVER_MAKE_FRIENDS = 1017
DBSERVER_MAKE_FRIENDS_RESP = 1031
DBSERVER_REQUEST_SECRET = 1025
DBSERVER_REQUEST_SECRET_RESP = 1026
DBSERVER_SUBMIT_SECRET = 1027
DBSERVER_SUBMIT_SECRET_RESP = 1028
DBSERVER_CREATE_STORED_OBJECT = 1003
DBSERVER_CREATE_STORED_OBJECT_RESP = 1004
DBSERVER_DELETE_STORED_OBJECT = 1008
DBSERVER_GET_STORED_VALUES = 1012
DBSERVER_GET_STORED_VALUES_RESP = 1013
DBSERVER_SET_STORED_VALUES = 1014
DBSERVER_GET_ESTATE = 1040
DBSERVER_GET_ESTATE_RESP = 1041

# CLIENT AGENT messages
CLIENT_AGENT_OPEN_CHANNEL = 3104
CLIENT_AGENT_CLOSE_CHANNEL = 3105
CLIENT_AGENT_SET_INTEREST = 3106
CLIENT_AGENT_REMOVE_INTEREST = 3107