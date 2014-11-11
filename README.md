lean.js
=======

LIVE DEMO: https://leanprover.github.com/live

This is a project to aid porting [Lean](http://leanprover.github.io/)
code to Javascript using an amazing tool called
[Emscripten](https://github.com/kripken/emscripten). It includes an
Emscripten build for [GMP](http://gmplib.org/),
[MPFR](http://www.mpfr.org/), and [LUA](http://lua.org) (dependencies
of Lean), which may be of use in their own right. This repository is
based on [cgaljs](https://github.com/marcosscriven/cgaljs).


Note that this package only works on **32-bit** virtual machines. We
have tested it on Ubuntu-14.04 (32-bit) machines.

We host the latest version of compiled javascript at
[gh-pages](https://github.com/leanprover/lean.js/tree/gh-pages) branch
of this repository. You can link the compiled javascript from your
HTML code:

```html
<script src="https://leanprover.github.io/lean.js/lean.js" type="text/javascript" charset="utf-8"></script>
```


Required Packages (on Ubuntu-14.04)
-----------------------------------

```bash
sudo apt-get update
sudo apt-get install build-essential cmake python2.7 nodejs default-jre git wget m4
sudo apt-get install libgmp-dev libmpfr-dev liblua5.2-dev gcc
sudo apt-get install nodejs-legacy    # If the executable of node.js is `nodejs` instead of `node`
wget https://s3.amazonaws.com/mozilla-games/emscripten/releases/emsdk-portable.tar.gz
tar xvf emsdk-portable.tar.gz
cd emsdk_portable
./emsdk update
./emsdk install latest
./emsdk activate latest
```

Build lean.js
--------------

Make sure that you have the following line on your `~/.bashrc`.

```bash
source ~/PATH/TO/emsdk_portable/emsdk_set_env.sh
```

Execute the following script to checkout and build lean.js.
```bash
git clone https://github.com/leanprover/lean.js
cd lean.js
make
```

 - The generated ``lean.js`` file is located at ``build/lean_js/source/lean-master/shell`` directory.
 - ``make push`` will destructively update the ``gh-pages`` branch of ``origin`` repository.
