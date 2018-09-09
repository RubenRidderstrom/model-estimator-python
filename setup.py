import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
	
setuptools.setup(
	  name='modelestimator',
      version='0.01',
	  author='Ruben Ridderström',
      author_email='ruben.ridderstrom@gmail.com',
      description='Program for estimating amino acid replacement rates',
	  long_description=long_description,
	  long_description_content_type="text/markdown",
      url='https://github.com/RubenRidderstrom/modelestimator',
      license='GPLv3',
      packages=setuptools.find_packages(),
      setup_requires=['pytest-runner'],
	  tests_require=['pytest']
	  )