# -*- coding: utf-8 -*-
#
# Copyright (C) 2016-2020 CERN.
#
# Marshmallow-Utils is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Marshmallow fields."""

from .contrib import Function, Method
from .edtfdatestring import EDTFDateString
from .generated import GenFunction, GenMethod
from .isodate import ISODateString
from .isolanguage import ISOLangString
from .links import Link, Links
from .localized_edtfdatestring import LocalizedEDTFDateString
from .nestedattr import NestedAttribute
from .sanitizedhtml import ALLOWED_HTML_ATTRS, ALLOWED_HTML_TAGS, SanitizedHTML
from .sanitizedunicode import SanitizedUnicode
from .trimmed import TrimmedString

__all__ = (
    'ALLOWED_HTML_ATTRS',
    'ALLOWED_HTML_TAGS',
    'EDTFDateString',
    'Function',
    'LocalizedEDTFDateString',
    'GenFunction',
    'GenMethod',
    'ISODateString',
    'ISOLangString',
    'Link',
    'Links',
    'Method',
    'NestedAttribute',
    'SanitizedHTML',
    'SanitizedUnicode',
    'TrimmedString',
)
