from setuptools import setup, find_packages

setup(
    name="api_test",
    version="0.1",
    author="me",
    description="API test",
    url="https://github.com/ksks2211/api-test",
    packages=find_packages(),
    install_requires=["requests","python-dotenv","elasticsearch"],
)