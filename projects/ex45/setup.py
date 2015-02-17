try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'ex45',
    'author': 'Tara Suan',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'tarasuan@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex45'],
    'scripts': [],
    'name': 'ex45'
}

setup(**config)