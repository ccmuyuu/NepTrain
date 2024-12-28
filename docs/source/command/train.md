# train
**Description:**  
Performs automatic training for NEP.
## Input Parameters

:::{important}
- You should use `NepTrain init` to generate `job.yaml`, and then use `NepTrain train job.yaml` to start the training task.  

- After the program runs, a `restart.yaml` file will be generated. To continue training, you can use `NepTrain train restart.yaml`.
::: 
**Usage:**  
```bash
NepTrain train <config_path>
```

**Options:**  
- `<config_path>`  
  Path to configuration file, such as `job.yaml`.
 
 


 
## Example
 
### 初始化操作
在命令行输入`NepTrain init`产生`job.yaml`，包括工作流中的所有控制参数，可修改。
将会产生一个job.yaml文件，打开这个文件，里边将会显示默认的执行参数以及对每个参数的解释，
在首次运行时，你可能需要逐行对参数进行设置，在以后运行时，你可以复制这个job.yaml文件到以后运行的工作目录作为训练的模板文件。
:::{tip}
如果您拷贝之前修改后的job.yaml。如果涉及版本变化，可以拷贝到工作路径，后执行`NepTrain init`。会将新加入的参数同步过来！
:::
#### 修改队列信息
我们需要对sub_vasp.sh和sub_gpu.sh进行修改。
:::{tip}
- 注意这里只需要修改队列信息以及环境设置，不要动最后一行。更不要加入任何计算命令！
- 没有测试多卡训练。谨慎使用！
:::
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
 
$@
```
#### 修改训练参数
1. 主动学习过程迭代时间，通常可以指定如下
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

2. 每次主动学习使用最远点采样最多采到的结构数目以及最远点采样最小间隔。
   ```yaml
    select:
      #After completing this round of MD, a maximum of max_selected structures will be selected from all trajectories.
      max_selected: 50
      min_distance: 0.01   #Hyperparameters for farthest point sampling
   ```
3. 最远点采样留下的力的阈值，力超过这一数值的结构将会被丢弃，通常运行MD时的力在10eV/埃以下，因此，这个值通常设置为20-40.
   ```yaml
   limit:
     force: 20  # Limit the force of the structure to between -force and force
   ```
在这里，我们设置VASP10节点计算单点能、K点使用kspacing设置0.1。主动学习跑10、100、500、1000ps。每次md的温度范围设置0-300k。
因为我们需要先进行单点能计算后才进入训练，所以这里current_job设置vasp。如果训练集是计算后的。可以初始任务设置nep
修改后的job.yaml如下。
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
  max_selected: 50
  min_distance: 0.01   #Hyperparameters for farthest point sampling

limit:
  force: 20  #Limit the force of the structure to between -force and force
```

### 准备初始结构
放一个或多个exyz、vasp格式的结构文件到`structure`，这里应该是结构超胞，作为主动学习时的初始结构。

### 开始训练
在登陆节点的终端执行一下命令
```shell
neptrain train job.yaml

```
后台运行
```shell
nohup neptrain train job.yaml &

```