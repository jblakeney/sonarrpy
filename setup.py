from distutils.core import setup

setup(
    name="sonarrpy",
    packages=["sonarrpy"],
    version="0.1.0",
    license="MIT",
    description="This is an unofficially supported client for interacting with the Sonarr API.",
    author="Jeff Blakeney",
    author_email="jblakeneypypi@gmail.com",
    url="https://github.com/jblakeney/sonarrpy",
    keywords=["Sonarr", "NZBDrone"],
    install_requires=["requests"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
)
