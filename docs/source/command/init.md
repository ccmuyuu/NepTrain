# init
**Description:**  
Initializes file templates for NepTrain.
## Input Parameters

**Usage:**  
```bash
NepTrain init [-f]
```

**Options:**  
- `-f, --force`  
  Force overwriting of generated templates. Default: `False`.

## Output
:::{tip}
These output files serve as inputs for the `train` command. Detailed modification instructions are provided in the [train](train.md) section.
::: 
- `job.yaml`  
  The configuration file for automatic training (`config_path`).  

- `run.in`  
  The template file for molecular dynamics (MD).  

- `structure/`  
  This folder must contain the structures required for active learning. Multiple structures can be included, and the file format should be either `.xyz` or `.vasp`.  

- `sub_gpu.sh`  
  A script file for submitting NEP and GPUMD tasks. <span style="color:red;">Modify the queue information based on your cluster setup.</span>  

- `sub_vasp.sh`  
  A script file for submitting VASP tasks. <span style="color:red;">Modify the queue information based on your cluster setup. </span> 
