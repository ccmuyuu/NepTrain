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
  Path to configuration file.
## Output