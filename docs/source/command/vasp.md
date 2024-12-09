# vasp
**Description:**  
Performs single-point energy calculations using VASP.
## Input Parameters
**Usage:**  
```bash
NepTrain vasp <model_path> [options]
```

**Options:**  
- `<model_path>`  
  Structure path or file (supports `xyz` and `vasp` formats).
- `-dir, --directory`  
  Directory for VASP calculations. Default: `./cache/vasp`.
- `-o, --out`  
  Output file path for calculated structure. Default: `./vasp_scf.xyz`.
- `-a, --append`  
  Append to output file. Default: `False`.
- `-g, --gamma`  
  Use Gamma-centered k-point scheme. Default: `False`.
- `-n, -np`  
  Number of CPU cores. Default: `1`.
- `--incar`  
  Path to INCAR file. Default: `./INCAR`.
- `-kspacing`  
  Set k-spacing value.
- `-ka`  
  Set k-points as 1 or 3 numbers (comma-separated). Default: `[1, 1, 1]`.
## Output