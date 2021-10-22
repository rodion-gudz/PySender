from setuptools import setup

setup(
    name='PySender',
    version='0.1.63',
    packages=['PySender'],
    url='',
    license='',
    author='lavender',
    author_email='services@lavender.ml',
    description='PyQt app to send REST API requests',
    install_requires=[
        'PyQt6',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'PySender = PySender:main'
        ]
    },
)
