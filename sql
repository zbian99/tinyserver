CREATE TABLE info (
    学号 VARCHAR(255) PRIMARY KEY,
    姓名 VARCHAR(255) NOT NULL,
    联系方式 VARCHAR(255) NOT NULL,
    本人性别 VARCHAR(255) NOT NULL,
    交友性别意向 VARCHAR(255) NOT NULL,
    年龄 VARCHAR(255) NOT NULL,
    你的年级 VARCHAR(255) NOT NULL,
    你希望TA的年级 VARCHAR(255) NOT NULL,
    身份类别 VARCHAR(255) NOT NULL,
    你希望对方是 VARCHAR(255) NOT NULL,
    你的星座 VARCHAR(255) NOT NULL,
    你希望TA的星座 VARCHAR(255) NOT NULL,
    你的兴趣爱好 VARCHAR(255) NOT NULL,
    自我介绍 VARCHAR(255) NOT NULL,
    你的身高 VARCHAR(255) NOT NULL,
    你希望TA的身高 VARCHAR(255) NOT NULL,
    你的体重 VARCHAR(255) NOT NULL,
    你希望TA的体型 VARCHAR(255) NOT NULL,
    你的家乡所在地 VARCHAR(255) NOT NULL,
    你希望TA家乡所在地 VARCHAR(255) NOT NULL,
    你希望未来在哪里发展 VARCHAR(255) NOT NULL,
    你希望和TA一起做的事 VARCHAR(255) NOT NULL,
    你的MBTI类型 VARCHAR(255),
    你的照片 VARCHAR(255),
    密码 VARCHAR(255) NOT NULL
);

LOAD DATA INFILE '/var/lib/mysql-files/test1.csv'
INTO TABLE info
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;



CREATE TABLE test (
    学号 VARCHAR(255) PRIMARY KEY,
    姓名 VARCHAR(255) NOT NULL
 );


 pip install -i https://pypi.tuna.tsinghua.edu.cn/simple mysql-connector-python