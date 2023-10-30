#!/bin/bash
set -euo pipefail

cd ~
mkdir -p .tree-sitter
cd .tree-sitter
mkdir -p build
mkdir -p repos
cd repos

clone_pull () {
    REPO="https://github.com/$2.git"
    if ! [ -d "$1" ]; then
        git clone "$REPO"
    else
        cd "$1"
        git pull
        cd ..
    fi
}

if [ -d "tree-sitter-c_sharp" ]; then
  mv tree-sitter-c_sharp tree-sitter-c-sharp
fi

clone_pull tree-sitter-scala "tree-sitter/tree-sitter-scala"
clone_pull tree-sitter-c "tree-sitter/tree-sitter-c"
clone_pull tree-sitter-ruby "tree-sitter/tree-sitter-ruby"
clone_pull tree-sitter-go "tree-sitter/tree-sitter-go"
clone_pull tree-sitter-graph "tree-sitter/tree-sitter-graph"
clone_pull tree-sitter-rust "tree-sitter/tree-sitter-rust"
clone_pull tree-sitter-embedded-template "tree-sitter/tree-sitter-embedded-template"
clone_pull tree-sitter-cpp "tree-sitter/tree-sitter-cpp"
clone_pull tree-sitter-ocaml "tree-sitter/tree-sitter-ocaml"
clone_pull tree-sitter-php "tree-sitter/tree-sitter-php"
clone_pull tree-sitter-haskell "tree-sitter/tree-sitter-haskell"
clone_pull tree-sitter-c-sharp "tree-sitter/tree-sitter-c-sharp"
clone_pull tree-sitter-html "tree-sitter/tree-sitter-html"
clone_pull tree-sitter-python "tree-sitter/tree-sitter-python"
clone_pull tree-sitter-bash "tree-sitter/tree-sitter-bash"
clone_pull tree-sitter-typescript "tree-sitter/tree-sitter-typescript"
clone_pull tree-sitter-json "tree-sitter/tree-sitter-json"
clone_pull tree-sitter-julia "tree-sitter/tree-sitter-julia"
clone_pull tree-sitter-java "tree-sitter/tree-sitter-java"
clone_pull tree-sitter-javascript "tree-sitter/tree-sitter-javascript"
clone_pull tree-sitter-jsdoc "tree-sitter/tree-sitter-jsdoc"
clone_pull tree-sitter-css "tree-sitter/tree-sitter-css"
clone_pull tree-sitter-ql-dbscheme "tree-sitter/tree-sitter-ql-dbscheme"
clone_pull tree-sitter-regex "tree-sitter/tree-sitter-regex"
clone_pull tree-sitter-verilog "tree-sitter/tree-sitter-verilog"
clone_pull tree-sitter-ql "tree-sitter/tree-sitter-ql"
clone_pull tree-sitter-tsq "tree-sitter/tree-sitter-tsq"
clone_pull tree-sitter-fluent "tree-sitter/tree-sitter-fluent"
clone_pull tree-sitter-toml "tree-sitter/tree-sitter-toml"
clone_pull tree-sitter-swift "alex-pinkus/tree-sitter-swift"
clone_pull tree-sitter-agda "tree-sitter/tree-sitter-agda"

mv tree-sitter-c-sharp tree-sitter-c_sharp

# Requires: npm install tree-sitter
cd tree-sitter-swift
npx tree-sitter generate --abi 14
cd ..

echo Done
