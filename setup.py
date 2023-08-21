from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in sowaanerp_saas/__init__.py
from sowaanerp_saas import __version__ as version

setup(
	name="sowaanerp_saas",
	version=version,
	description="App to Manage SowaanERP SaaS model",
	author="SowaanERP",
	author_email="info@sowaan.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
