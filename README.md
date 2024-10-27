 

<h4 align="center">

 
[![PyPI Downloads](https://img.shields.io/pypi/dm/NepTrain?logo=pypi&logoColor=white&color=blue&label=PyPI)](https://pypi.org/project/NepTrain)
[![Requires Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python&logoColor=white)](https://python.org/downloads)
 
</h4>

 
[pull request]: https://github.com/aboys-cb/NepTrain/pulls
[github issue]: https://github.com/aboys-cb/NepTrain/issues
[github discussion]: https://github.com/aboys-cb/NepTrain/discussions

 
## 安装

Python包索引[PyPI]中的版本始终是相对无bug的最新稳定版本，可以通过`pip安装`:

[pypi]: https://pypi.org/project/NepTrain

```sh
pip install NepTrain
```

如果你想在主分支上使用最新未发布的更改，你可以直接从GitHub安装:

```sh
pip install -U git+https://github.com/aboys-cb/NepTrain
```
 

 
## 使用方式
### 暂时还没把自动训练连接起来

首先先初始化下 会在当前目录下创建提交脚本
```sh
NepTrain init
```
修改`vim ~/.NepTrain` 修改赝势文件路径
以下命令是一个简单的实例

针对结构或者结构文件生成微扰训练集

0.03的晶格形变+0.1的原子扰动
```sh
NepTrain perturb Cs16Ag8Bi8I48.vasp --num 200 --cell 0.03 -d 0.1 -o train.xyz
```



计算VASP单点能
```sh
NepTrain vasp demo.xyz -np 64 --directory ./cache -g --incar=./INCAR --kpoints 35 -o ./result/result.xyz
```
 
 
 