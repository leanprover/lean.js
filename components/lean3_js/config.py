NAME = 'lean3_js'
VERSION = '0.3.0'
DOWNLOADS = ['https://github.com/leanprover/lean/archive/lean3.tar.gz']
SOURCE_DIR = 'lean-lean3'
CONFIGURE_CMD = ' '.join([
    'cmake',
    '-DGMP_INCLUDE_DIR:STRING={includes}/gmp',
    '-DGMP_LIBRARIES:STRING={libs}/libgmp.so',
    '-DMPFR_INCLUDES:STRING={includes}/mpfr',
    '-DMPFR_LIBRARIES:STRING={libs}/libmpfr.so',
    '-DCMAKE_TOOLCHAIN_FILE={component_dir}/cmake-emcc-toolchain.txt',
    '-DCMAKE_BUILD_TYPE=EMSCRIPTEN',
    '-DTCMALLOC=OFF',
    '-DMULTI_THREAD=OFF',
    '-DIGNORE_SORRY=ON',
    '-DCMAKE_CXX_FLAGS="-v -U__SSE2_MATH__ --ignore-dynamic-linking -U__GNUG__"',
    'src/'
])
MAKE_CMD = 'emmake make'
ARTIFACTS =  {
    'includes': [
        {'source':'CGAL-%s/include/' % VERSION, 'name':'cgal'}
    ],
    'libs': [
        {'source': 'CGAL-%s/lib/libCGAL.so' % VERSION,'name':'libcgal.so'},
        {'source': 'CGAL-%s/lib/libCGAL_Core.so' % VERSION,'name':'libcgal_core.so'},
    ]
}
