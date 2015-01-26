NAME = 'lua'
VERSION = '5.2.0'
#DOWNLOADS = ['http://www.lua.org/ftp/lua-%s.tar.gz' % (VERSION)]
DOWNLOADS = ['https://leanprover.github.io/lean.js/lua-%s.tar.gz' % (VERSION)]
SOURCE_DIR = 'lua-%s' % VERSION
SOURCE_PATCHES = [
    { 'file': 'Makefile', 'patch': 'Makefile.patch' },
    { 'file': 'src/Makefile', 'patch': 'src.Makefile.patch' }
]
CONFIGURE_CMD = 'emmake make emscripten -j'
MAKE_CMD = 'emmake make local'
ARTIFACTS =  {
    'includes': [{
        'source':'lua-%s/install/include' % VERSION,
        'name':'lua'
    }],
    'libs': [{
        'source': 'lua-%s/install/lib/liblua.so' % VERSION,
        'name'  : 'liblua.so'
    }]
}
