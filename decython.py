from distutils.core import setup
from Cython.Build import cythonize

setup(
	name = 'SamplerBoxAudio',
	ext_modules = cythonize("samplerbox_audio.pyx")
)