#!/usr/bin/env python

"""
setup.py file for SWIG veejay
"""

from distutils.core import setup, Extension

veejay_module = Extension('_veejay',
                           include_dirs = ['/usr/include/veejay'],
                           libraries = ['veejay'],
                           library_dirs = ['/usr/lib'],
                           sources=['veejay.c', 'veejay_wrap.c'],
                           )

setup (name = 'veejay',
       version = '0.1',
       author      = "Joshua Jackson",
       description = """veejay swig wrapper""",
       ext_modules = [veejay_module],
       py_modules = ["veejay"],
       )
