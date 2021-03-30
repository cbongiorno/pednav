from setuptools import setup

setup(	name='pednav',
      	version='0.2',
      	packages=['pednav'],
	install_requires=[	'numpy>=1.14.2','python-igraph>=0.8.0'],
	#scripts=['bin/bahc','bin/svhc_benchmark','bin/svhc_plot'],
	author='Christian Bongiorno',
	author_email='christian.bongiorno@centralesupelec.fr',
	license='GPL',
	zip_safe=False

      )

