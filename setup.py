from setuptools import setup

setup(name='scIB',
      version='0.1.1',
      description='Benchmark tools for single cell data integration',
      author='Malte Luecken, Maren Buettner, Daniel Strobl, Michaela Mueller',
      author_email='malte.luecken@helmholtz-muenchen.de',
      packages=['scIB'],
      package_data={'scIB': ['resources/*.txt']},
      zip_safe=False,
      license='MIT',
      url='https://github.com/theislab/scib',
      keywords = ['benchmark', 'single cell', 'data integration'], 
      install_requires=[            
          'MulticoreTSNE',
          'anndata',
          'scanpy',
          'fa2',
          'gprofiler-official',
          'anndata',
          'rpy2>=3',
          'bbknn',
          'anndata2ri',
          'scanorama',
      ],
      classifiers=[
         'Development Status :: 3 - Alpha',      
         'Intended Audience :: Developers',      
         'Topic :: Software Development :: Build Tools',
         'License :: OSI Approved :: MIT License',   
         'Programming Language :: Python :: 3',      
         'Programming Language :: Python :: 3.7',
      ])

