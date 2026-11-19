"""
Setup and Build Configuration
VoxTranslate Pro - Developed by Krishna
"""

from setuptools import setup, find_packages

setup(
    name="voxtranslate-pro",
    version="2.5.0",
    description="Real-Time AI Voice, Speech & Document Translator",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Krishna",
    author_email="krishna.developer@example.com",
    url="https://github.com/krishna/real-time-voice-translator",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.110.0",
        "uvicorn>=0.28.0",
        "customtkinter>=5.2.0",
        "sounddevice>=0.5.0",
        "numpy>=1.24.0",
        "SpeechRecognition>=3.10.0",
        "deep-translator>=1.11.0",
        "gTTS>=2.5.0",
        "pyttsx3>=2.90",
        "pymupdf>=2.0.0",
        "beautifulsoup4>=4.12.0",
        "requests>=2.31.0",
    ],
    entry_points={
        "console_scripts": [
            "voxtranslate=main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
    ],
    python_requires=">=3.9",
)
