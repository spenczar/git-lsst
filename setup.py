from setuptools import setup

install_requires = ['jira', 'PyGithub', 'giturlparse']

dev_requires = ['mypy', 'flake8', 'flake8-mypy', 'black']

setup(name='git-lsst',
      version="0.2.1",
      description="Git plugin for working on LSST",
      url='https://github.com/spenczar/git-lsst',
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
          "Development Status :: 3 - Alpha",
          "Operating System :: POSIX :: Linux",
      ],
      author='Spencer Nelson',
      author_email='swnelson@uw.edu',
      license='MIT',
      install_requires=install_requires,
      extras_require={"dev": dev_requires},
      scripts=["git-lsst"],
      zip_safe=False)
