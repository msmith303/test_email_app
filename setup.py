from setuptools import setup

setup(
   name='outside_email_test_app',
   version='1.0',
   description='A test module for the Outside Analytics email application',
   author='Mike Smith',
   author_email='mike.smith303@gmail.com',
   packages=['outside_email_test_app'],
   install_requires=['selenium', 'behave'], #external packages as dependencies
   scripts=[]
)
