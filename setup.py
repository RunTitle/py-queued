from setuptools import setup, find_packages

setup(
    name="Queued",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'boto>=2.38.0'
    ],
    test_suite='queued.tests',
    # metadata for upload to PyPI
    author="Stephen Durham",
    author_email="sdurham@runtitle.com",
    description="Amazon SQS and SNS integration library for python",
    license="PSF",
    keywords="Amazon SQS SNS",
    url="http://example.com/py-queued/",   # project home page, if any
)
