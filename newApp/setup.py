import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="new_app",
    version="0.0.1",

    description="An empty CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "new_app"},
    packages=setuptools.find_packages(where="new_app"),

    install_requires=[
        "aws-cdk.core==1.105.0",
        "aws_cdk.aws_s3",
        "aws_cdk.aws_ecs_patterns",
        "aws_cdk.aws_elasticloadbalancingv2",
        "aws_cdk.aws_ec2"
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
