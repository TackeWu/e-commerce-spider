# 描述
##### Language : Python 2.7
##### Framework : Scrapy 1.4

# Note:
###  运行前先在setting.json中配置cookies和query词
```bash
-a          : 爬取京东，淘宝，天猫所有数据
-n 数字组合 : 0表示京东,1表示淘宝,2表示天猫
              如“-n 01”表示爬取京东、淘宝
python version : 2.7
Note：
    1、如果爬不到数据(没有报错)，请在setting.json中替换成自己的cooike
    2、setting.json可以自己定义query词
```  



# 运行方式
```bash
./init.sh
./run.sh -a
```