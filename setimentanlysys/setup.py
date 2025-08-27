from setuptools import setup, find_packages

setup(
    name="sentiment_app",          # Your package name
    version="0.1.0",               # Version
    packages=find_packages(),      # Automatically find packages in your project
    include_package_data=True,     # Include files like .txt, .csv, .pkl
    install_requires=[             # Dependencies
        "fastapi",
        "uvicorn",
        "pandas",
        "scikit-learn",
        "numpy"
    ],
    entry_points={
        "console_scripts": [
            "run-backend=backend.app:main",   # Optional: create a command to run app
        ],
    },
)
