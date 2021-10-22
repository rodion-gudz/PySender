from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name='PySender',
    version='0.1.66',
    packages=['PySender'],
    url='https://github.com/fast-geek/PySender',
    license='MIT',
    author='lavender',
    author_email='services@lavender.ml',
    description='PyQt app to send REST API requests',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='python pyqt rest api',
    python_requires='>=3.6.1',
    install_requires=[
        'PyQt5',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'PySender = PySender:main'
        ]
    },
)
