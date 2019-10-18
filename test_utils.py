import sys

STATIC_METHOD_AUTO_SPEC = sys.version_info[:3] >= (3, 7, 4)
""" Python support autospec of static methods on versions (3.7.4 and 3.8)

See: https://bugs.python.org/issue23078
"""
