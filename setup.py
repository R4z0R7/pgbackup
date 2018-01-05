from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    description='Database backups locally or to AWS S3',
    author='Borislav Iliev Todorov',
    author_email='borislavtodorov1990@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'}, 
    install_requires=[]
)
