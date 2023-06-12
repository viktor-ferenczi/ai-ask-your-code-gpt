#!/bin/bash
set -euo pipefail

cd ~
mkdir -p .tree-sitter
cd .tree-sitter
mkdir -p build
mkdir -p repos
cd repos

clone_pull () {
if ! [ -d $1 ]; then
    git clone https://github.com/tree-sitter/$1.git
else
    cd $1
    git pull
    cd ..
fi
}

clone_pull tree-sitter-scala
clone_pull tree-sitter-c
clone_pull tree-sitter-ruby
clone_pull tree-sitter-go
clone_pull tree-sitter-graph
clone_pull tree-sitter-rust
clone_pull tree-sitter-embedded-template
clone_pull tree-sitter-cpp
clone_pull tree-sitter-ocaml
clone_pull tree-sitter-php
clone_pull tree-sitter-haskell
clone_pull tree-sitter-c-sharp
clone_pull tree-sitter-html
clone_pull tree-sitter-python
clone_pull tree-sitter-bash
clone_pull tree-sitter-typescript
clone_pull tree-sitter-json
clone_pull tree-sitter-julia
clone_pull tree-sitter-java
clone_pull tree-sitter-javascript
clone_pull tree-sitter-jsdoc
clone_pull tree-sitter-css
clone_pull tree-sitter-ql-dbscheme
clone_pull tree-sitter-regex
clone_pull tree-sitter-verilog
clone_pull tree-sitter-ql
clone_pull tree-sitter-tsq
clone_pull tree-sitter-fluent
clone_pull tree-sitter-toml
clone_pull tree-sitter-swift
clone_pull tree-sitter-agda

mv tree-sitter-c-sharp tree-sitter-c_sharp

echo Done
