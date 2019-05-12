from distutils.core import setup

setup(
    name="nzbclients",
    packages=["nzbclients"],
    version="0.1.0",
    license="MIT",
    description="A library of unofficial library of clients for interacting with programs that download NZB files.",
    author="Jeff Blakeney",
    author_email="jblakeneypypi@gmail.com",
    url="https://github.com/jblakeney/nzbclients",
    keywords=["Radarr", "SABnzbd", "Sonarr", "NZBDrone"],
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
