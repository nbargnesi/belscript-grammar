#!/usr/bin/env bash
echo "Expecting BEL Script on stdin..."
set -x verbose
java -cp antlr-3.4.jar:. Main
