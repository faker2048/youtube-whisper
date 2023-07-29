from setuptools import setup, find_packages

setup(
    name="ytws",
    version="0.1.0",
    description="YouTube Whisper - A YouTube Downloader with Transcription",
    author="faker2048",
    author_email="nspyia2002@gmail.com",
    url="https://github.com/faker2048/youtube-whisper",
    packages=find_packages(include=["src", "src.*"]),
    install_requires=[
        "click==8.1.6",
        "faster_whisper==0.7.1",
        "loguru==0.7.0",
        "yt_dlp==2023.7.6",
    ],
    entry_points="""
        [console_scripts]
        ytws=src.cli.main:main
    """,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
)