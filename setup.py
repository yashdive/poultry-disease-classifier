import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
__version__ = "0.0.1"

REPO_NAME = "poultry-disease-classifier"
AUTHOR_USER_NAME = "yash"
SRC_REPO = "henalyze"
AUTHOR_EMAIL = "yashdive190@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for CNN app",
    long_description=long_description,
    long_description_context = "text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)