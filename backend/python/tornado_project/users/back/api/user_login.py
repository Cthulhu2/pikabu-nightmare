# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class UserLogin(ApiHandler):

    def get(self):
        print(self.args)

        return None, 200, {}
