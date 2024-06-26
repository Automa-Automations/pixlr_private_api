from setuptools import setup, find_packages

setup(
    name="pixlr_private_api",
    version="0.0.2",
    description="A Python Package to Generate Images with http://pixlr.com programmatically.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Automa-Automations/pixlr-private-api",
    author="Simon Ferns",
    author_email="business@simonferns.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    keywords="temp-email automation email",
    packages=find_packages(),
    install_requires=["requests", "temp_email_automa"],
)
