INSTALL_PREFIX=/var/www/html/

all: lean.js lean3.js
	echo "done"

lean.js: libs/libgmp.so libs/libmpfr.so libs/liblua.so build/lean/source/lean-master/shell/lean build/lean/source/lean-master/library.tar.gz
	python build_all.py lean_js
	rm -rf build/lean_js/source/lean-master/shell/library
	cd build/lean_js/source/lean-master/shell && tar xvfz ../../../../lean/source/lean-master/library.tar.gz
	rm -rf build/lean_js/source/lean-master/shell/lean.*
	emmake make -C build/lean_js/source/lean-master/ || emmake make -C build/lean_js/source/lean-master/ || emmake make -C build/lean_js/source/lean-master/

lean3.js: libs/libgmp.so libs/libmpfr.so build/lean3/source/lean-lean3/shell/lean build/lean3/source/lean-lean3/library.tar.gz
	python build_all.py lean3_js
	rm -rf build/lean3_js/source/lean-lean3/shell/library
	cd build/lean3_js/source/lean-lean3/shell && tar xvfz ../../../../lean3/source/lean-lean3/library.tar.gz
	rm -rf build/lean3_js/source/lean-lean3/shell/lean.*
	emmake make -C build/lean3_js/source/lean-lean3/ || emmake make -C build/lean3_js/source/lean-lean3/ || emmake make -C build/lean3_js/source/lean-lean3/

build/lean/source/lean-master/shell/lean:
	python build_all.py lean

build/lean3/source/lean-lean3/shell/lean:
	python build_all.py lean3

build/lean/source/lean-master/library.tar.gz: build/lean/source/lean-master/shell/lean
	cp .project build/lean/source/lean-master/library
	cd build/lean/source/lean-master/library && find . -name "*.olean" -delete
	cd build/lean/source/lean-master/library && ../bin/linja clean && ../bin/linja
	cd build/lean/source/lean-master && tar cvfz library.tar.gz `find library -name "*.olean"`

build/lean/source/lean-master/hott.tar.gz: build/lean/source/lean-master/shell/lean
	cp .project build/lean/source/lean-master/hott
	cd build/lean/source/lean-master/hott && find . -name "*.olean" -delete
	cd build/lean/source/lean-master/hott && ../bin/linja clean && ../bin/linja -X
	cd build/lean/source/lean-master && tar cvfz hott.tar.gz `find hott -name "*.olean"`

build/lean3/source/lean-lean3/library.tar.gz: build/lean3/source/lean-lean3/shell/lean
	cp .project build/lean3/source/lean-lean3/library
	cd build/lean3/source/lean-lean3/library && find . -name "*.olean" -delete
	cd build/lean3/source/lean-lean3/library && ../bin/linja clean && ../bin/linja
	cd build/lean3/source/lean-lean3 && tar cvfz library.tar.gz `find library -name "*.olean"`

libs/libgmp.so:
	python build_all.py gmp

libs/libmpfr.so:
	python build_all.py mpfr

libs/liblua.so:
	python build_all.py lua

push:
	git checkout gh-pages
	git reset --hard origin/gh-pages~
	cp build/lean_js/source/lean-master/shell/lean.js lean.js
	git add lean.js
	git commit -m "Update `date -R`"
	git push --force origin gh-pages:gh-pages
	git checkout master

push3:
	git checkout gh-pages
	git reset --hard origin/gh-pages~
	cp build/lean3_js/source/lean-lean3/shell/lean.js lean3.js
	git add lean3.js
	git commit -m "Update `date -R`"
	git push --force origin gh-pages:gh-pages
	git checkout lean3

clean:
	rm -rf build libs includes

.PHONY: all gmp mpfr lua lean lean3 lean3.js lean.js clean
