# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class UserVerifyemailUsername(ApiHandler):

    def get(self, username):
        print(self.args)

        return None, 200, None