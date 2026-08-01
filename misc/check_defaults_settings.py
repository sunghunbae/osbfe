from openfe.protocols import openmm_rfe

# Fetch defaults for Relative Binding Free Energy (RBFE)
settings = openmm_rfe.RelativeHybridTopologyProtocol.default_settings()

# View the full configuration dictionary
for section, subdict in settings.dict().items():
    if isinstance(subdict, dict):
        print(f"\n{section}")
        for k, v in subdict.items():
            if isinstance(v, list):
                print(f"    {k:<40}")  
                for vv in v:
                    print(f"    {" ":<40} {vv}")  
            elif isinstance(v, dict) and 'val' in v and 'unit' in v:
                print(f"    {k:<40} {v['val']} ({v['unit']})")  
            else:
                print(f"    {k:<40} {v}")  
    else:
        v = subdict
        print(f"\n{section:<44} {v}")
