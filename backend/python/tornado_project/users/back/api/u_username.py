# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class UUsername(ApiHandler):

    def get(self, username):
        print(username)
        return {'username': f'{username}-from-back'}, 200, None

    def put(self, username):
        print(self.form)

        return {}, 200, None
