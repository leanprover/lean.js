NAME = 'lean_js'
VERSION = '0.2.0'
DOWNLOADS = ['https://github.com/leanprover/lean/archive/master.tar.gz']
SOURCE_DIR = 'lean-master'
CONFIGURE_CMD = ' '.join([
    'cmake',
    '-DGMP_INCLUDE_DIR:STRING={includes}/gmp',
    '-DGMP_LIBRARIES:STRING={libs}/libgmp.so',
    '-DMPFR_INCLUDES:STRING={includes}/mpfr',
    '-DMPFR_LIBRARIES:STRING={libs}/libmpfr.so',
    '-DLUA_INCLUDE_DIR:STRING={includes}/lua',
    '-DLUA_LIBRARIES:STRING={libs}/liblua.so',
    '-DCMAKE_TOOLCHAIN_FILE={component_dir}/cmake-emcc-toolchain.txt',
    '-DCMAKE_BUILD_TYPE=EMSCRIPTEN',
    '-DTCMALLOC=OFF',
    '-DMULTI_THREAD=OFF',
    '-DIGNORE_SORRY=ON',
    '-DCMAKE_CXX_FLAGS="-v -U__SSE2_MATH__ --ignore-dynamic-linking -U__GNUG__"',
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
