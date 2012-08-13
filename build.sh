#!/usr/bin/env bash
set -x verbose
java -cp antlr-3.4.jar org.antlr.Tool BELScript_v1.g || exit 1
java -cp antlr-3.4.jar org.antlr.Tool BELScript_C_v1.g || exit 1
java -cp antlr-3.4.jar org.antlr.Tool BELScript_Python_v1.g || exit 1
javac -cp antlr-3.4.jar *.java || exit 1

