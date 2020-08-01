# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class User(ApiHandler):

    def post(self):
        print(self.json)

        return None, 200, None