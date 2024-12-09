# gpumd

**Description:**  
Runs molecular dynamics simulations using GPUMD.

**Usage:**  
```bash
NepTrain gpumd <model_path> [options]
```

**Options:**  
- `<model_path>`  
  Structure path or file (supports `xyz` and `vasp` formats).
- `-dir, --directory`  
  Path for GPUMD calculations. Default: `./cache/gpumd`.
- `-in, --in`  
  Path to `run.in` file. Default: `./run.in`.
- `-nep, --nep`  
  Path to potential function file. Default: `./nep.txt`.
- `-t, --time`  
  Molecular dynamics simulation time (ps). Default: `10`.
- `-T, --temperature`  
  Simulation temperature(s) (K). Default: `[300]`.
- `-o, --out`  
  Output file for trajectory. Default: `./trajectory.xyz`.
