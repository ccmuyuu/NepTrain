# CsPbI3

## 准备工作
:::{note}
首先我们创建个工作路径叫CsPbI3.后面的操作都默认在这个目录下。
:::

我们这里以立方相的$CsPbI_3$为例介绍整个自动化训练框架的使用
首先我们从[Materials Project](https://next-gen.materialsproject.org/materials/mp-1069538?chemsys=Cs-Pb-I)下载cif文件。
然后在VESTA扩包[3,3,2]作为后面的训练的初始结构,文件名为`CsPbI3.vasp`。
扩包后的结构如下
```text
Cs1 Pb1 I3
1.0
       18.8254261017         0.0000000000         0.0000000000
        0.0000000000        18.8254261017         0.0000000000
        0.0000000000         0.0000000000        12.5502843857
   Cs   Pb    I
   18   18   54
Direct
     0.166666672         0.166666672         0.250000000
     0.166666672         0.166666672         0.750000000
     0.166666672         0.500000000         0.250000000
     0.166666672         0.500000000         0.750000000
     0.166666672         0.833333313         0.250000000
     0.166666672         0.833333313         0.750000000
     0.500000000         0.166666672         0.250000000
     0.500000000         0.166666672         0.750000000
     0.500000000         0.500000000         0.250000000
     0.500000000         0.500000000         0.750000000
     0.500000000         0.833333313         0.250000000
     0.500000000         0.833333313         0.750000000
     0.833333313         0.166666672         0.250000000
     0.833333313         0.166666672         0.750000000
     0.833333313         0.500000000         0.250000000
     0.833333313         0.500000000         0.750000000
     0.833333313         0.833333313         0.250000000
     0.833333313         0.833333313         0.750000000
     0.000000000         0.000000000         0.000000000
     0.000000000         0.000000000         0.500000000
     0.000000000         0.333333343         0.000000000
     0.000000000         0.333333343         0.500000000
     0.000000000         0.666666687         0.000000000
     0.000000000         0.666666687         0.500000000
     0.333333343         0.000000000         0.000000000
     0.333333343         0.000000000         0.500000000
     0.333333343         0.333333343         0.000000000
     0.333333343         0.333333343         0.500000000
     0.333333343         0.666666687         0.000000000
     0.333333343         0.666666687         0.500000000
     0.666666687         0.000000000         0.000000000
     0.666666687         0.000000000         0.500000000
     0.666666687         0.333333343         0.000000000
     0.666666687         0.333333343         0.500000000
     0.666666687         0.666666687         0.000000000
     0.666666687         0.666666687         0.500000000
     0.000000000         0.000000000         0.250000000
     0.000000000         0.000000000         0.750000000
     0.000000000         0.333333343         0.250000000
     0.000000000         0.333333343         0.750000000
     0.000000000         0.666666687         0.250000000
     0.000000000         0.666666687         0.750000000
     0.333333343         0.000000000         0.250000000
     0.333333343         0.000000000         0.750000000
     0.333333343         0.333333343         0.250000000
     0.333333343         0.333333343         0.750000000
     0.333333343         0.666666687         0.250000000
     0.333333343         0.666666687         0.750000000
     0.666666687         0.000000000         0.250000000
     0.666666687         0.000000000         0.750000000
     0.666666687         0.333333343         0.250000000
     0.666666687         0.333333343         0.750000000
     0.666666687         0.666666687         0.250000000
     0.666666687         0.666666687         0.750000000
     0.000000000         0.166666672         0.000000000
     0.000000000         0.166666672         0.500000000
     0.000000000         0.500000000         0.000000000
     0.000000000         0.500000000         0.500000000
     0.000000000         0.833333313         0.000000000
     0.000000000         0.833333313         0.500000000
     0.333333343         0.166666672         0.000000000
     0.333333343         0.166666672         0.500000000
     0.333333343         0.500000000         0.000000000
     0.333333343         0.500000000         0.500000000
     0.333333343         0.833333313         0.000000000
     0.333333343         0.833333313         0.500000000
     0.666666687         0.166666672         0.000000000
     0.666666687         0.166666672         0.500000000
     0.666666687         0.500000000         0.000000000
     0.666666687         0.500000000         0.500000000
     0.666666687         0.833333313         0.000000000
     0.666666687         0.833333313         0.500000000
     0.166666672         0.000000000         0.000000000
     0.166666672         0.000000000         0.500000000
     0.166666672         0.333333343         0.000000000
     0.166666672         0.333333343         0.500000000
     0.166666672         0.666666687         0.000000000
     0.166666672         0.666666687         0.500000000
     0.500000000         0.000000000         0.000000000
     0.500000000         0.000000000         0.500000000
     0.500000000         0.333333343         0.000000000
     0.500000000         0.333333343         0.500000000
     0.500000000         0.666666687         0.000000000
     0.500000000         0.666666687         0.500000000
     0.833333313         0.000000000         0.000000000
     0.833333313         0.000000000         0.500000000
     0.833333313         0.333333343         0.000000000
     0.833333313         0.333333343         0.500000000
     0.833333313         0.666666687         0.000000000
     0.833333313         0.666666687         0.500000000


```

## 生成微扰训练集
我们先生成10000个微扰训练集，3%的形变，0.2Å的原子微扰。
:::{tip}
这里选择加入-f避免微扰生成非物理结构，根据键长过滤下！
:::
```shell
NepTrain perturb CsPbI3.vasp -n 10000 -c 0.03 -d 0.2 -f
<!-- 输出如下： -->
Current structure:Cs18Pb18I54 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:01
```
脚本会输出perturb.xyz。我们在使用select从10000个中抽取100个作为最初的训练集。
:::{note}
- 要根据select的输出调整-d参数，或者直接输入-d 0 ，但选择效果可能不是最佳
- 如果没有势函数默认使用SOAP获取描述符，SOAP描述符的间距都比较大，所以要调整-d。
:::
```shell
NepTrain select perturb.xyz -max 100 -d 1
<!-- 输出如下： -->
[2024-12-28 18:15:21.436949] --  Reading trajectory perturb.xyz
[2024-12-28 18:15:28.985300] --  The file base does not exist.
[2024-12-28 18:15:28.986175] --  The file ./nep.txt does not exist.
[2024-12-28 18:15:28.986671] --  An invalid path for nep.txt was provided, using SOAP descriptors instead.
[2024-12-28 18:15:29.454689] --  Start generating structure descriptor, please wait
[2024-12-28 18:16:18.169325] --  Starting to select points, please wait...
[2024-12-28 18:16:24.492264] --  Obtained 100 structures.
[2024-12-28 18:16:25.800733] --  The point selection distribution chart is saved to ./selected.png.
[2024-12-28 18:16:25.801237] --  The selected structures are saved to ./selected.xyz.
```
然后运行以下命令，准备工作完毕！
```shell
mv selected.xyz train.xyz
<!-- 这个删除是非必要的 -->
rm selected_perturb.xyz.xyz perturb.xyz selected.png
```
## 初始化任务
:::{tip}
所有的模板文件都可以自行保存，如果有就会跳过
:::
首先，我们使用以下命令进行初始化
```shell
NepTrain init
<!-- 输出如下： -->
[2024-12-29 10:08:27.298365] --  For existing files, we choose to skip; if you need to forcibly generate and overwrite, please use -f or --force.
[2024-12-29 10:08:27.302688] --  Create the directory ./structure, please place the expanded structures that need to run MD into this folder!
[2024-12-29 10:08:27.312968] --  Please check the queue information and environment settings in sub_vasp.sh!
[2024-12-29 10:08:27.317307] --  Please check the queue information and environment settings in sub_gpu.sh!
[2024-12-29 10:08:27.320868] --  You need to check and modify the vasp_job and vasp.cpu_core in the job.yaml file.
[2024-12-29 10:08:27.321411] --  You also need to check and modify the settings for GPUMD active learning in job.yaml!
[2024-12-29 10:08:27.336706] --  Detected that there is no train.xyz in the current directory; please check the directory structure!
[2024-12-29 10:08:27.337630] --  If there is a training set but the filename is not train.xyz, please unify the job.yaml.
[2024-12-29 10:08:27.345471] --  Create run.in; you can modify the ensemble settings! Temperature and time will be modified by the program!
[2024-12-29 10:08:27.351823] --  Initialization is complete. After checking the files, you can run `NepTrain train job.yaml` to proceed.
```
将`CsPbI3.vasp`放到程序创建的`structure`目录:
```shell
mv CsPbI3.vasp structure
``` 
我们来看下现在的目录：
```text
├── job.yaml
├── run.in
├── structure/
│   └── CsPbI3.vasp
├── sub_gpu.sh
├── sub_vasp.sh
└── train.xyz
```
### 修改提交脚本
sub_gpu.sh 是提交NEP以及GPUMD的脚本，sub_vasp.sh是提交VASP的脚本。
在这里我们只需要修改队列信息和初始化环境的命令即可。
修改后如下
```shell
#! /bin/bash
#SBATCH --job-name=NepTrain
#SBATCH --nodes=1
#SBATCH --partition=cpu
#SBATCH --ntasks-per-node=64 
#You can place some environment loading commands here.
source ~/.bashrc
conda activate NepTrain
$@ 
```
```shell
#! /bin/bash
#SBATCH --job-name=NepTrain-gpu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
source ~/.bashrc
conda activate NepTrain
$@
```
### 修改MD模板[可选]
默认的run.in是npt的，一般来说只需要修改`ensemble`即可，程序会自动替换温度。
我们这里不做修改。
### 修改NEP训练参数
默认情况下，程序不强制要求传入nep.in。程序会自动根据训练集生成一个最简单的nep.in。
如果需要修改超参数，请将自己的nep.in放在这个目录即可。 
### 修改任务细节
在job.yaml中，我们尽可能地通过注释解释了每个参数。并且大部分参数都是不需要调整的。
我们在这里不会详细的解释每个参数，只演示怎么根据自己体系修改。

#### 修改VASP计算细节
:::{tip}
`cpu_core`要和sub_vasp.sh申请的核数统一
:::
为了加速单点计算，我们通过`vasp_job`设置任务数量，程序会按照这个数量切分任务。
这个根据自己的计算资源决定。

此外，所有的计算细节都通过`INCAR`指定，可以自行创建一个`INCAR`放在这个目录下。
我们还需要修改k点。我们这里选用kspacing的形式。修改后如下
```yaml
vasp:

  cpu_core: 64
  kpoints_use_gamma: true  #ASE defaults to using M-point k-mesh, but here we default to using the gamma-centered grid; this can be set to false.

  incar_path: ./INCAR

  use_k_stype: kspacing
  #--ka
  kpoints:
    - 20 #a
    - 20 #b
    - 20 #c
  kspacing: 0.1
```
#### 修改迭代细节
目前的程序迭代次数是根据主动学习的时间确定的。
我们选择开启键长过滤
我们设置MD温度范围0-300k,迭代时间分别为10ps、100ps、500ps、1000ps。
:::{tip}
`step_times`并不要求是一个递进的关系，比如可以10 100 100 500 500 这种重复性的检测。
如果在第二次的100ps中，没有抽取到结构，除了多做一个md的时间，并不会重复训练。
:::
修改后如下
```yaml
gpumd:
#Time for iterative progressive learning in units of picoseconds.
#The first active learning is at 10ps, the second at 100ps, with a total of four active learning sessions.
  step_times:
    - 10
    - 100
    - 500
    - 1000
#Each time active learning is performed, all structures in model_path will undergo molecular dynamics (MD) simulations at the following temperatures, followed by sampling.
  temperature_every_step:
    - 50
    - 100
    - 150
    - 200
    - 250
    - 300
  model_path: ./structure
  run_in_path: ./run.in
  filter_by_bonds: true  #Enable bond length detection, and determine structures with bond lengths below 60% of the equilibrium model bond lengths as non-physical structures.
```
额外的说一句yaml语法。
   ```yaml
    gpumd:
    #Time for iterative progressive learning in units of picoseconds.
    #The first active learning is at 10ps, the second at 100ps, with a total of four active learning sessions.
      step_times:
        - 10
        - 100
        - 500
        - 1000
   ```
   等价于
   ```yaml
    gpumd:
    #Time for iterative progressive learning in units of picoseconds.
    #The first active learning is at 10ps, the second at 100ps, with a total of four active learning sessions.
      step_times: [10, 100, 500, 1000]
   ```
#### 修改抽样细节
我们设置每次迭代最多选取80个结构.最小距离为0.01
```yaml
select:
  #After completing this round of MD, a maximum of max_selected structures will be selected from all trajectories.
  max_selected: 80
  min_distance: 0.01   #Hyperparameters for farthest point sampling
```
完整的修改后的job.yaml如下
```yaml
version: 1.4.3
queue: slurm #Select the queuing system, divided into Slurm and local.
vasp_job: 10 #The number of tasks submitted when calculating single-point energy with VASP.
#所有任务提交的根目录
work_path: ./cache  #Root directory for all task submissions.
current_job: vasp  #If the current_job has three states: nep, gpumd, vasp, and if train.xyz has not been calculated, set it to vasp; otherwise, directly set it to use nep to train the potential function, or use gpumd.
generation: 1  #Marking resume tasks.
init_train_xyz: ./train.xyz  #Initial training set; if not calculated, set current_job to vasp.
init_nep_txt: ./nep.txt  #If current_job is set to gpumd, a potential function must be provided; otherwise, it can be ignored.
nep:
  #Does it support restarting? If true, the potential function for the next step will continue from this step for nep_restart_step steps.
  #The program will automatically set lambda_1 to 0.
  #If false, retrain from scratch every time.
  nep_restart: true
  nep_restart_step: 20000
  #Optional; if you need to modify the number of steps, simply provide a file in the current path.
  #If there is no such file, the number of steps will be automatically generated based on the training set.
  nep_in_path: ./nep.in
  #Optional
  test_xyz_path: ./test.xyz
vasp:

  cpu_core: 64
  kpoints_use_gamma: true  #ASE defaults to using M-point k-mesh, but here we default to using the gamma-centered grid; this can be set to false.

  incar_path: ./INCAR

  use_k_stype: kspacing
  #--ka
  kpoints:
    - 20 #a
    - 20 #b
    - 20 #c
  kspacing: 0.1
gpumd:
#Time for iterative progressive learning in units of picoseconds.
#The first active learning is at 10ps, the second at 100ps, with a total of four active learning sessions.
  step_times:
    - 10
    - 100
    - 500
    - 1000
#Each time active learning is performed, all structures in model_path will undergo molecular dynamics (MD) simulations at the following temperatures, followed by sampling.
  temperature_every_step:
    - 50
    - 100
    - 150
    - 200
    - 250
    - 300
  model_path: ./structure
  run_in_path: ./run.in
  filter_by_bonds: true  #Enable bond length detection, and determine structures with bond lengths below 60% of the equilibrium model bond lengths as non-physical structures.

select:
  #After completing this round of MD, a maximum of max_selected structures will be selected from all trajectories.
  max_selected: 80
  min_distance: 0.01   #Hyperparameters for farthest point sampling

limit:
  force: 20  #Limit the force of the structure to between -force and force
```
## 开始训练
在登陆节点的终端执行一下命令
```shell
NepTrain train job.yaml

```
后台运行
```shell
nohup NepTrain train job.yaml &

```