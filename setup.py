import setuptools

setuptools.setup(
    name="ukiyo-credit-model",
    version="0.0.1",
    description="IFRS 9 Credit Risk Model by Ukiyo Software Ltd",
    author="Ukiyo Software",
    author_email="devteam@ukiyosoftware.com",
    url="www.ukiyosoftware.com",
    packages=setuptools.find_packages(exclude=["test*", "notebooks"]),
    python_requires=">=3.10",
    package_data={"": ["**/*.yaml"]},
    zip_safe=False,
)
