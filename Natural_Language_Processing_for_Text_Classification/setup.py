from setuptools import setup, find_packages

setup(
    name="Credit Card Fraud Detector",
    version="0.0.1",
    author="Md Zahid Hasan",
    author_email='mdzhasancz@gmail.com',
    description='A machine learning project for credit card fraud detection',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/hasan-zahid/Credit_Card_Fraud_Detection",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'scikit-learn',
        'scipy',
        'seaborn',
        'jupyter',
        'django',
    ],
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.12',
)
