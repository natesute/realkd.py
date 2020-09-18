from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='realkd',
    version='0.1.1',
    packages=['realkd'],
    url='https://github.com/marioboley/realkd.py',
    license='MIT',
    author='Mario Boley',
    author_email='mario.boley@gmail.com',
    description='Methods for knowledge discovery and interpretable machine learning.',
    long_description=long_description,
    python_requires='>=3.6',
    install_requires=['sortedcontainers>=2.1.0',
                      'pandas>=0.25',
                      'numpy>=1.16.1',
                      'matplotlib',
                      'sortednp>=0.3.0'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ]
)
