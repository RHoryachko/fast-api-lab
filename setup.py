from setuptools import setup, find_packages

setup(
    name="library_api",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.109.0",
        "uvicorn>=0.27.0",
        "pydantic>=2.6.0",
        "starlette>=0.36.0",
    ],
) 