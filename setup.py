from setuptools import setup

setup(name='frechetdist',
      version='1.0.0.dev0',
      description='Calculate discrete Frechet distance',
      url='https://github.com/ekgordon/discrete_frechet',
      author='Ethan Gordon',
      author_email='ekgordon@cs.washington.edu',
      license='Apache License 2.0',
      packages=['frechetdist'],
      setup_requires=["pytest-runner"],
      tests_require=["pytest"],
      install_requires=[
          'numpy',
      ],
      zip_safe=False)