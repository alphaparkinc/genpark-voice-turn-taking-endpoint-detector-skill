from setuptools import setup, find_packages

setup(
    name="genpark-voice-turn-taking",
    version="1.0.0",
    description="Deterministic zero-dependency real-time voice VAD & semantic turn-taking endpoint detector.",
    long_description=open("README.md", encoding="utf-8").read() if __import__("os").path.exists("README.md") else "Deterministic zero-dependency real-time voice VAD & semantic turn-taking endpoint detector.",
    long_description_content_type="text/markdown",
    author="GenPark AI Engineering",
    author_email="engineering@genpark.ai",
    url="https://github.com/Alpha-Park/genpark-voice-turn-taking-endpoint-detector-skill",
    py_modules=["client", "mcp_server"],
    python_requires=">=3.9",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
