from setuptools import setup, find_packages
import os

PACKAGE_VERSION = os.getenv("PACKAGE_VERSION", "0.1.0")

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="near-jsonrpc-client",
    version=PACKAGE_VERSION,
    description="A typed Python client for the NEAR JSON-RPC API with Pydantic models and async HTTP support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(include=["near_jsonrpc_client*", "near_jsonrpc_models*"]),
    install_requires=[
        "httpx>=0.24",
        "pydantic>=2.0",
    ],
    python_requires=">=3.9"
)
