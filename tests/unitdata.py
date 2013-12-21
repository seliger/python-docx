# encoding: utf-8

"""
Test data builders for unit tests
"""

from docx.oxml.shared import nsdecls, oxml_fromstring


class BaseBuilder(object):
    """
    Provides common behavior for all data builders.
    """
    nsdecls = ' %s' % nsdecls('w')

    def __init__(self):
        """Establish instance variables with default values"""
        self._empty = False
        self._indent = 0
        self._nsdecls = ''

    @property
    def element(self):
        """Return element based on XML generated by builder"""
        return oxml_fromstring(self.xml)

    @property
    def is_empty(self):
        return True

    def with_indent(self, indent):
        """Add integer *indent* spaces at beginning of element XML"""
        self._indent = indent
        return self

    def with_nsdecls(self):
        self._nsdecls = self.nsdecls
        return self
