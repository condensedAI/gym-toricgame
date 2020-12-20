from setuptools import setup

setup(name='gym_toricgame',
      version='0.0.1',
      install_requires=['gym'],
      packages=['gym_toricgame'],
      package_dir={'gym_toricgame': 'mypkg'},
      package_data={'gym_toricgame': ['envs/toricgame']},)
