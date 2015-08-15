from distutils.core import setup, Extension

setup(
  ext_modules = [
    Extension('_example', ["example_wrap.cxx",'example.cpp'],
      library_dirs=[],
      libraries=[],
      extra_compile_args=[],
      extra_link_args=[])
  ])
