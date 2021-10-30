from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name='PySender',
    version='0.2.11',
    packages=['PySender', 'PySender.ui'],
    license='MIT',
    author='lavender',
    author_email='support@lavender.ml',
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
    project_urls={
        "Homepage": "https://github.com/fast-geek/PySender",
        "Donate": "https://lavtg.ml/donat",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
