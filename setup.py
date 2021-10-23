from setuptools import setup, find_packages
# Change project to project name here 
# Choose relevant license as required, add necessary install_requires 
from our_project.version import __version__
link_to_use = "https://github.com/Nelson-Gon/project/archive/refs/tags/v"+__version__+".zip"
setup(name='project',
      version=__version__,
      description="Python Citations Generator",
      url="http://www.github.com/Nelson-Gon/project",
      download_url=link_to_use,
      author='Nelson Gonzabato',
      author_email='gonzabato@hotmail.com',
      license='MIT',
      keywords="web html academics citation science",
      packages=find_packages(),
      long_description=open('README.md', encoding="utf-8").read(),
      long_description_content_type='text/markdown',
      install_requires=[''],
      python_requires='>=3.6',
      zip_safe=False)
