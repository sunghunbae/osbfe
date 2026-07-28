from openfe.protocols.openmm_afe import AbsoluteBindingProtocol

import openmm

platforms = [openmm.Platform.getPlatform(i).getName() for i in range(openmm.Platform.getNumPlatforms())]

print(f'Installed OpenMM supports {platforms}')

# Instantiate default settings for a protocol
settings = AbsoluteBindingProtocol.default_settings()

# Check the configured compute platform
print(f'OpenFE ABFE is configured with {settings.engine_settings.compute_platform}')

