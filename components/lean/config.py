NAME = 'lean'
VERSION = '0.2.0'
DOWNLOADS = ['https://github.com/leanprover/lean/archive/master.tar.gz']
SOURCE_DIR = 'lean-master'
CONFIGURE_CMD = ' '.join([
    'cmake',
    '-DCMAKE_BUILD_TYPE=Release',
    '-DCMAKE_CXX_COMPILER=g++',
    '-DTCMALLOC=OFF',
    '-DIGNORE_SORRY=ON',
    'src/'
])
MAKE_CMD = 'emmake make -j'
ARTIFACTS =  {
    'includes': [
        {'source':'CGAL-%s/include/' % VERSION, 'name':'cgal'}
    ],
    'libs': [
        {'source': 'CGAL-%s/lib/libCGAL.so' % VERSION,'name':'libcgal.so'},
        {'source': 'CGAL-%s/lib/libCGAL_Core.so' % VERSION,'name':'libcgal_core.so'},
    ]
}
