# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.user import User
from .api.user_login import UserLogin
from .api.user_logout import UserLogout
from .api.user_verifyEmail_username import UserVerifyemailUsername
from .api.u_username import UUsername


url_prefix = 'back'

routes = [
    dict(resource=User, urls=[r"/user"], endpoint='user'),
    dict(resource=UserLogin, urls=[r"/user/login"], endpoint='user_login'),
    dict(resource=UserLogout, urls=[r"/user/logout"], endpoint='user_logout'),
    dict(resource=UserVerifyemailUsername, urls=[r"/user/verifyEmail/(?P<username>[^/]+?)"], endpoint='user_verifyEmail_username'),
    dict(resource=UUsername, urls=[r"/u/(?P<username>[^/]+?)"], endpoint='u_username'),
]

def load_uris(config):
    try:
        config.update_uri(routes, url_prefix)
    except:
        pass