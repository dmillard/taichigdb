from setuptools import setup, find_packages

setup(name='taichigdb',
      version='1.0',
      packages=find_packages(),
      scripts=['bin/taichigdb_register_printers'],
      install_requires=['numpy'],
      author="David Millard",
      author_email="dmillard@usc.edu",
      description='GDB pretty printers for taichi types',
      long_description=open('README.rst', 'r').read(),
      license="MPL2",
      keywords="taichi gdb",
      url="https://github.com/dmillard/taichigdb",
      project_urls={
          "Source Code": "https://github.com/dmillard/taichigdb",
          "Bug Tracker": "https://github.com/dmillard/taichigdb/issues",
      })
