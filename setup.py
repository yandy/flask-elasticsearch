from setuptools import setup


with open('README.md') as fp:
    long_description = fp.read()

setup(
    name='Flask-ElasticSearch',
    version='0.1',
    download_url='https://github.com/kazoup/flask-elasticsearch/',
    license='BSD',
    author='Peter Flood - Kazoup',
    author_email='peter.flood@kazoup.com',
    description='ElasticSearch for Flask',
    long_description=long_description,
    py_modules=['flask_elasticsearch'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'elasticsearch',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
