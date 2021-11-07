from setuptools import setup

from PySender.__version__ import __version__

with open("README.md") as f:
    long_description = f.read()

setup(
    name='PySender',
    version=__version__,
    packages=['PySender', 'PySender.ui'],
    include_package_data=True,
    license='MIT',
    author='lavender',
    author_email='support@lavender.ml',
    description='PyQt app to send REST API requests',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='python pyqt rest api',
    url='https://github.com/fast-geek/PySender',
    python_requires='>=3.6.1',
    package_data={'PySender': ['res/icon.png']},
    install_requires=[
        'PyQt5',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'PySender = PySender:main'
        ]
    },
    project_urls={
        "Homepage": "https://github.com/fast-geek/PySender",
        "Donate": "https://lavtg.ml/donat",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
