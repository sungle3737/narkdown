import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()


def get_requirements(fname):
    "Takes requirements from requirements.txt and returns a list."
    with open(fname) as fp:
        reqs = list()
        for lib in fp.read().split("\n"):
            # Ignore pypi flags and comments
            if not lib.startswith("-") or lib.startswith("#"):
                reqs.append(lib.strip())
        return reqs


install_requires = get_requirements("requirements.txt")
setuptools.setup(
    name="narkdown",
    version="1.3.5",
    author="younho9",
    author_email="younho9.choo@gmail.com",
    description="A tool to use Notion as a Markdown editor.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/younho9/narkdown",
    install_requires=install_requires,
    include_package_data=True,
    packages=setuptools.find_packages(),
    keywords=["notion", "github", "markdown"],
    python_requires=">=3.5",
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
