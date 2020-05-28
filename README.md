# FastAPI Web

- [FastAPI](https://fastapi.tiangolo.com/zh/)

## Configure

[Mac下conda环境操作、conda换源、pip换源_python_Awt_FuDongLai的博客-CSDN博客](https://blog.csdn.net/Awt_FuDongLai/article/details/105878916)

### Conda

```bash
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/

mkdir .pip
cd .pip
vim pip.conf

[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host=pypi.tuna.tsinghua.edu.cn

conda create -n py36 python=3.6
source activate py36
```

### Package

```bash
pip install fastapi
pip install uvicorn
# for mongodb
pip install pymongo
```

## MongoDB Tutorial

- [MongoDB 教程 | 菜鸟教程](https://www.runoob.com/mongodb/mongodb-tutorial.html)

### Create Database

```bash
mongo

# create feedback database
use feedback

# create feeds collection
db.createCollection("feeds")

show collections

# remove all documents
db.feeds.remove({})
```

## 🚀 Usage

```bash
uvicorn main:app --reload
```

### Swagger UI

- [Swagger UI](http://127.0.0.1:8000/docs)

## Author

👤 **Zhihao Zhang**

- Github: [@zzh1991](https://github.com/zzh1991)

## Show your support

Please ⭐️ this repository if this project helped you!

## 📝 License

Copyright © 2020 [zzh1991](https://github.com/zzh1991).<br />
This project is [MIT](https://github.com/zzh1991/fastapi-web/blob/master/LICENSE) licensed.