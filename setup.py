from setuptools import setup, find_packages
from os.path import dirname, realpath, join

CURRENT_DIR = dirname(realpath(__file__))

with open(join(CURRENT_DIR, "README.rst")) as long_description_file:
    long_description = long_description_file.read()


setup(
    name="Flask-Simple-Captcha",
    version="0.1.0",
    url="https://github.com/shonenada/flask-captcha",
    author="Yaoda Liu",
    author_email="shonenada@gmail.com",
    description="Captcha for Flask",
    long_description=long_description,
    zip_safe=False,
    packages=find_packages(exclude=["docs"]),
    include_package_data=True,
    platforms="any",
    install_requires=[
        "Flask>=0.10",
        "PIL>=1.1.7",
        "wheezy.captcha==0.1.29"
    ],
    classifiers=[
        "Framework :: Flask",
        "Environment :: Web Environment",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ]
)
