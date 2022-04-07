import setuptools
 
setuptools.setup(
  name='baseballdc',
  version='0.0.20',
  description='Baseball Data Center',
  author='Joe Smith',
  author_email='joesmi9.sde@gmail.com',
  url='https://github.com/joesmi9/baseballdc',
  license='MIT', 
  keywords=['baseball', 'baseball analytics', 'baseball reference'],
  package_dir={"": "src"},
  packages=setuptools.find_packages(where="src"),
  install_requires=[''],
  classifiers=[
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 3',
    'Operating System :: Unix',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: Microsoft :: Windows',
  ]
)