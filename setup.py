# -*- coding: utf-8 -*-


"""NUSL theses data model."""

from setuptools import find_packages, setup

readme = open('README.md').read()

tests_require = [
]

extras_require = {
}

setup_requires = [
    'pytest-runner>=2.6.2',
]

install_requires = [
    'requests',
    'oarepo-taxonomies >= 2.4.1, <3.0.0'
]

packages = find_packages()

setup(
    name='nr-taxonomies',
    version="1.0.0a1",
    description=__doc__,
    long_description=readme,
    # keywords='nusl Invenio theses',
    license='MIT',
    author='Daniel Kopecký',
    author_email='Daniel.Kopecky@techlib.cz',
    # url='',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        # 'flask.commands': [
        #     'my-command=flask_my_extension.commands:cli'
        # ]
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    # classifiers=[
    #     'Environment :: Web Environment',
    #     'Intended Audience :: Developers',
    #     'License :: OSI Approved :: MIT License',
    #     'Operating System :: OS Independent',
    #     'Programming Language :: Python',
    #     'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    #     'Topic :: Software Development :: Libraries :: Python Modules',
    #     'Programming Language :: Python :: 3',
    #     'Programming Language :: Python :: 3.7',
    #     'Development Status :: 3 - Planning',
    # ],
)
