from setuptools import setup, find_packages

version = '0.1.0'

setup(name="helga-newrelic",
      version=version,
      description=('IRC bot using twisted'),
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules'],
      keywords='irc bot newrelic helga',
      author='Shaun Duncan',
      author_email='shaun.duncan@gmail.com',
      url='https://github.com/shaunduncan/helga',
      license='MIT',
      packages=find_packages(),
      install_requires = [
          'requests==2.2.1',
      ],
      entry_points = dict(
          helga_plugins=[
              'newrelic = helga_newrelic.plugins:NewRelicStats',
          ],
          helga_webhooks=[
              'newrelic = helga_newrelic.webhooks:newrelic',
          ],
      ),
)
