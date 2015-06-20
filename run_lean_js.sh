#!/bin/bash

function print_usage {
    echo "USAGE: $0 <path/to/lean.js> <path/to/test.lean>";
}

# Check # of args
if [ $# -ne 2 ] ; then
    print_usage;
    exit 1;
fi

LEAN_JS_FILENAME=$1
TEST_FILENAME=$2

# Check LEAN_JS_FILENAME and TEST_FILENAME exist
if [ ! -f ${LEAN_JS_FILENAME} ] ; then
    echo "error: ${LEAN_JS_FILENAME} is not found."
    print_usage;
    exit 1
fi
if [ ! -f ${TEST_FILENAME} ] ; then
    echo "error: ${TEST_FILENAME} is not found."
    print_usage;
    exit 1
fi

TMP_JS=`mktemp ./tmp_XXXX`
mv ${TMP_JS} ${TMP_JS}.js
TMP_JS=${TMP_JS}.js
TMP_OUT=`mktemp ./tmp_out_XXXX`

# Copy prefix script
cat << EOF >> "${TMP_JS}"
var Module = {};
Module['noExitRuntime'] = true;
Module.TOTAL_MEMORY=64 * 1024 * 1024;
EOF

# Copy lean.js script
cat "${LEAN_JS_FILENAME}" >> "${TMP_JS}"

# Copy postfix script
cat << EOF >> "${TMP_JS}"
Module.lean_init();
Module.lean_import_module('standard');
fs.readFile("${TEST_FILENAME}", 'utf8', function(err, data) {
    FS.writeFile("${TEST_FILENAME}", data, {encoding: 'utf8'});
    Module.lean_process_file("${TEST_FILENAME}");
});
EOF

# Run node and exit
node "${TMP_JS}" 2>&1 | tee ${TMP_OUT}
grep "^FLYCHECK_BEGIN ERROR" ${TMP_OUT} > /dev/null 2>&1 
[ $? == 0 ] && RET=1 || RET=0
rm -- "${TMP_JS}" "${TMP_OUT}"
exit ${RET}
