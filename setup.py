from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='pysysctllib',
  version='0.0.1',
  author='hlnikniky',
  author_email='orekhovs09@gmail.com',
  description='Simple libary for control status of systemctl service',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/Sesdear/Python-Systemctl-Libary',
  packages=find_packages(),
  install_requires=[],
  classifiers=[
    'Programming Language :: Python',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='systemctl service control status',
  project_urls={
    'GitHub': 'https://github.com/Sesdear/Python-Systemctl-Libary'
  },
  python_requires='>=3.6'
)