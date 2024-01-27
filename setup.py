from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in figo_care/__init__.py
from figo_care import __version__ as version

setup(
	name="figo_care",
	version=version,
	description="Figo Care Plus Ltd Customization In ERPNext. This Company Base On Tanzania",
	author="InshaSiS Technologies",
	author_email="hidayat@inshasis.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
