import os

NAME = 'mpfr'
VERSION = '3.1.1'
DOWNLOADS = ['http://www.mpfr.org/mpfr-current/mpfr-%s.tar.bz2' % VERSION]
SOURCE_DIR = 'mpfr-%s' % VERSION
CONFIGURE_CMD = 'emconfigure ./configure --with-gmp-include={includes}/gmp --with-gmp-lib={libs}/libgmp.so'
MAKE_CMD = 'emmake make -j4'
CONFIG_PATCHES = [
    {
        'file': 'configure',
        'patch': 'configure.patch'
    }
]
ARTIFACTS =  {
    'includes': [{
                     'source':os.path.join('mpfr-%s' % VERSION, 'src'),
                     'name':'mpfr'
                 }],
    'libs': [{
                 'source': os.path.join('mpfr-%s' % VERSION, 'src', '.libs', 'libmpfr.so'),
                 'name':'libmpfr.so'
             }]
}





