from setuptools import setup

from version import __version__


setup(
    name="flake8-fstring",
    py_modules=["flake8_fstring"],
    version=__version__,
    description=open("README.md").readlines()[4],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    keywords="fstring linting flake8",
    author="Aaron Heesakkers",
    author_email="aaronheesakkers@gmail.com",
    url="http://github.com/aars/flake8-fstring",
    license="Freely Distributable",
    zip_safe=False,
    entry_points={"flake8.extension": ["SLF001 = flake8_fstring:Linter"]},
    install_requires=["flake8"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: Freely Distributable",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
)
