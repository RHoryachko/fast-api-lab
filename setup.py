from setuptools import setup, find_packages

setup(
    name="library_api",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi==0.88.0",
        "uvicorn==0.20.0",
        "pydantic==1.10.2",
        "starlette==0.22.0",
    ],
) 