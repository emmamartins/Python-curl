###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###


import sys

VERSION = (2, 0, '', '', 0)

if VERSION[3] and VERSION[4]:
	VERSION_TEXT = '{0}.{1}'.format(*VERSION)
else:
	VERSION_TEXT = '{0}.{1}'.format(*VERSION[0:3])

VERSION_EXTRA = ''
LICENSE = 'MIT' #MIT
EDITION = ''  # Added in package names, after the version
KEYWORDS = "oop, module, python, framework, web, app, curl, api, protocols, network "

PYVERSION_MA = sys.version_info.major
PYVERSION_MI = sys.version_info.minor
