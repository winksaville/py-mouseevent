from setuptools import setup

setup(name='mouseevent',
      version='0.1',
      description='trivial package that pretends to create mouse events',
      url='http://github.com/winksaville/py-mouseevent',
      author='Wink Saville',
      author_email='wink@saville.com',
      license='MIT',
      package_data={'mouseevent': ['py.typed']},
      packages=['mouseevent'],
      zip_safe=False)
