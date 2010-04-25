# -*- coding: utf-8 -*-
#
# File: test_views.py
#
# Copyright (c) InQuant GmbH
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

__author__    = """Ramon Bartl <ramon.bartl@inquant.de>"""
__docformat__ = 'plaintext'

import unittest

from collective.uploadify.tests.base import TestCase


class TestViews(TestCase):
    """ Test View Class
    """

    def afterSetUp(self):
        self.setRoles(('Manager', ))


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestViews))
    return suite

# vim: set ft=python ts=4 sw=4 expandtab :
