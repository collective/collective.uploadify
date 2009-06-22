# -*- coding: utf-8 -*-
#
# File: upload.py
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

__author__ = 'Ramon Bartl <ramon.bartl@inquant.de>'
__docformat__ = 'plaintext'

import logging
import mimetypes
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.filerepresentation.interfaces import IFileFactory

logger = logging.getLogger("collective.uploadify")

UPLOAD_JS = """
    $(document).ready(function() {
        $('#uploader').fileUpload({
            'uploader'    : '%(portal_url)s/++resource++uploader.swf',
            'script'      : '%(url)s/@@upload_file',
            'cancelImg'   : '%(portal_url)s/++resource++cancel.png',
            'multi'       :  %(multi)s,
            'folder'      : '%(url)s',
        });
    });
"""


class UploadView(BrowserView):
    """ The Upload View
    """

    template = ViewPageTemplateFile("upload.pt")

    def __call__(self):
        return self.template()


class UploadFile(BrowserView):
    """ Upload a file
    """

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        file_name = self.request.form.get("Filename", "")
        file_data = self.request.form.get("Filedata", None)
        content_type = mimetypes.guess_type(file_name)[0]

        if file_data:
            factory = IFileFactory(self.context)
            logger.info("uploading file: filename=%s, content_type=%s" % (file_name, content_type))
            f = factory(file_name, content_type, file_data)
            logger.info("file url: %s" % f.absolute_url())
            return f.absolute_url()


class UploadInit(BrowserView):
    """ Initialize uploadify js
    """

    def __call__(self):
        context = self.context
        portal_url = getToolByName(context, 'portal_url')()

        settings = dict(portal_url = portal_url,
                        multi = 'true',
                        url = context.absolute_url(),
                       )

        return UPLOAD_JS % settings


class UploadCheck(BrowserView):
    """ Upload Check
    """
    def __call__(self):
        pass


# vim: set ft=python ts=4 sw=4 expandtab :
