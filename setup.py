from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in resiina/__init__.py
from resiina import __version__ as version

setup(
	name="resiina",
	version=version,
	description="An app for TKO-äly\'s needs.",
	author="Mitja Karhusaari <mitja.karhusaari@helsinki.fi>",
	author_email="-",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
