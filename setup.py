from setuptools import find_packages, setup

setup(
    name='bytesep',
    version='0.2.0',
    description='Music source separation',
    author='ByteDance',
    url="https://github.com/bytedance/music_source_separation",
    license='Apache 2.0',
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.10',
    install_requires=[
        'torch>=2.8.0,<2.9.0',
        'torchaudio>=2.8.0,<2.9.0',
        'torchvision>=0.23.0,<0.24.0',
        'pytorch-lightning==2.4.0',
        'torchmetrics>=1.4.0',
        'numpy>=1.24,<3',
        'scipy>=1.10',
        'librosa>=0.10.2',
        'museval==0.4.0',
        'h5py>=3.10',
        'torchlibrosa>=0.1.0',
        'matplotlib>=3.8',
        'musdb==0.4.0',
        'samplerate==0.1.0'
    ],
    zip_safe=False
)
