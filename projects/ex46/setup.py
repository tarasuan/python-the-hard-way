try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Work from Python the Hard Way ex46',
    'author': 'Tara Suan',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'tarasuan@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex46'],
    'scripts': ['bin/bin_example.py'],
    'name': 'ex46'
}

setup(**config)