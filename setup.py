from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='pythonapp',
      version='0.0.1',
      description='Example Python application with test suite',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        
      ],
      keywords='python example test',
      license='MIT',
      packages=['pythonapp'],
      install_requires=[
          'termcolor',
      ],
      test_suite='tests',
      tests_require=['xmlrunner'],
      entry_points={
          'console_scripts': ['pythonapp-msg=pythonapp.command_line:main'],
      },
      include_package_data=True,
      zip_safe=False)

