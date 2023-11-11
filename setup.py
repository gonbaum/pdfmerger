from setuptools import setup, find_packages

setup(
    name='pdf_merger',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'PyPDF2==2.12.1',
    ],
    entry_points={
        'console_scripts': [
            'pdf-merger=pdf_merger.main:main',
        ],
    },
)