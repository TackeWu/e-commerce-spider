#!/bin/bash
Miniconda2_dir="$HOME/miniconda2"
DATA_DIR="./data"
LOGS_DIR="./logs"
date=$(date "+%m_%d")

if [ ! -d $DATA_DIR ];then
    mkdir "$DATA_DIR"
fi

if [ ! -d $LOGS_DIR ];then
    mkdir "$LOGS_DIR"
fi

if [ $# == 0 ];then
    echo "请输入参数,’-h’查看帮助"
fi

jd_spider(){
    echo "正在爬取京东数据......"
    jd_log_dir="./logs/jd_run_$date.log"
    $Miniconda2_dir/bin/scrapy crawl jd_spider > $jd_log_dir 2>&1
    echo "京东数据爬取完成"
    echo -e "\n"

}

tm_spider(){
    echo "正在爬取天猫数据......"
    tm_log_dir="./logs/tm_run_$date.log"
    $Miniconda2_dir/bin/scrapy crawl tm_spider > $tm_log_dir 2>&1
    echo "天猫数据爬取完成"
    echo -e "\n"
}

tb_spider(){
    echo "正在爬取淘宝数据......"
    tb_log_dir="./logs/tb_run_$date.log"
    $Miniconda2_dir/bin/scrapy crawl tb_spider > $tb_log_dir 2>&1
    echo "淘宝数据爬取完成"
    echo -e "\n"
}


array_name=(jd_spider tb_spider tm_spider)

while getopts ":af:hf:n:" arg
do
    case $arg in
        h)
            echo "-a          : 爬取京东，淘宝，天猫所有数据"
            echo "-n 数字组合 : 0表示京东,1表示淘宝,2表示天猫"
            echo "              如“-n 01”表示爬取京东、淘宝"
            echo "python version : 2.7"
            echo "Note："
            echo "    1、如果爬不到数据(没有报错)，请在setting.json中替换成自己的cooike"
            echo "    2、setting.json可以自己定义query词"
            ;;
        a)
            ${array_name[0]}
            ${array_name[1]}
            ${array_name[2]}
            ;;
        n)
            is_jd=$(echo $2 | grep "0")
            is_tb=$(echo $2 | grep "1")
            is_tm=$(echo $2 | grep "2")
            if [ "$is_jd" != "" ];then
                 ${array_name[0]}
            fi
            if [ "$is_tb" != "" ];then
                 ${array_name[1]}
            fi
            if [ "$is_tm" != "" ];then
                 ${array_name[2]}
            fi
            ;;

        ?)
            echo "输入参数错误,’-h’查看帮助"

            ;;
     esac
done