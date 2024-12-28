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
待完善
## Default INCAR
```text
SYSTEM = NepTrain-default-incar
ALGO = Normal
EDIFF = 1e-06
EDIFFG = -0.01
ENCUT = 500
GGA = PE
IBRION = -1
ISMEAR = 0
ISPIN = 1
ISTART = 0
LCHARG = False
LREAL = Auto
LWAVE = False
NELM = 100
NPAR = 4
NSW = 0
PREC = Normal
SIGMA = 0.05
```

## Example
:::{note}
如果`./INCAR`是一个无效的文件路径，会使用默认的INCAR。
:::
