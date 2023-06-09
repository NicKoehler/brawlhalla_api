from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="brawlhalla_api",
    version="0.1.0",
    packages=find_packages(exclude=["tests"]),
    description="Unofficial Brawlhalla API implementation",
    author="NicKoehler",
    author_email="grillinicola@proton.me",
    url="https://github.com/nickoehler/brawlhalla_api",
    license="MIT",
    install_requires=[
        "httpx==0.23.3",
    ],
)
