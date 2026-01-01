from setuptools import setup

import os

PACKAGE_VERSION = os.getenv("PACKAGE_VERSION", "0.0.1")

setup(
    name="near_jsonrpc_client",
    version=PACKAGE_VERSION,
    description="A Python client for interacting with NEAR Protocol's JSON-RPC API, supporting both sync and async "
                "requests with Pydantic models",
    packages=["near_jsonrpc_client", "near_jsonrpc_models"],
    install_requires=[
        "pydantic>=2.0",
        "httpx>=0.24",
    ],
    python_requires=">=3.11",
)
