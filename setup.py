from distutils.core import setup

LONG_DESCRIPTION = None
try:
    LONG_DESCRIPTION = open('README.md').read()
except:
    pass

setup(
    name = 'Python-Printr',
    packages = ['printr'],
    version = '0.0.1',
    description = 'Python module to allow a print line to be updated after printing',
    long_description = LONG_DESCRIPTION,
    author = 'Jake Howard',
    author_email = 'me@theorangeone.net',
    url = 'https://github.com/RealOrangeOne/Printr',
    license='MIT',
    platforms=['any']
)