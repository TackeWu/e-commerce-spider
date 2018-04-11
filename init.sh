#!/bin/bash
VENV=virtualenv
OPT='-p python'
VENVNAME=`basename "$PWD"`
VENVPATH="$HOME/venv/$VENVNAME"

echo "using $VENV"

DEPENDENCIES=(
    scrapy requests
)

$VENV $OPT $VENVPATH
. $VENVPATH/bin/activate
for DEP in ${DEPENDENCIES[*]};do
    pip install   $DEP -i https://pypi.douban.com/simple
done
deactivate