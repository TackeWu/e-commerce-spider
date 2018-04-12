#!/bin/bash
Miniconda2_file="$HOME/Miniconda2-4.4.10-Linux-x86_64.sh"
Miniconda2_dir="$HOME/miniconda2"
if [ -f $Miniconda2_file ];then
    rm  $Miniconda2_file
fi
wget -P $HOME https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda2-4.4.10-Linux-x86_64.sh
if [ -d $Miniconda2_dir ];then
    rm -r $Miniconda2_dir
fi
bash $Miniconda2_file
rm $Miniconda2_file

echo "using $Miniconda2_dir"

source $Miniconda2_dir/bin/activate
DEPENDENCIES=(
    scrapy requests
)

for DEP in ${DEPENDENCIES[*]};do
    pip install   $DEP -i https://pypi.douban.com/simple
done
source $Miniconda2_dir/bin/deactivate