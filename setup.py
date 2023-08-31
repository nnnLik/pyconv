from setuptools import setup, find_packages

setup(
    name="pyconv",
    version="0.1",
    author="Makhmudov Rasul",
    author_email="rslmakhmudov@gmail.com",
    description="...",
    long_description=open("README.rst").read(),
    url="https://github.com/nnnLik/Converter",
    license="BSD",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="conversion image audio document",
    project_urls={
        "Documentation": "https://github.com/nnnLik/Converter/docs",
        "Source": "https://github.com/nnnLik/Converter",
    },
)
