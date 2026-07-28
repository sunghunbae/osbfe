#!/usr/bin/bash

for file in network_setup/transformations/*.json; do
  name=${file:30}    # strip off parent path "network_setup/transformations/"
  prefix=${name%.*}  # strip off extension ".json"
  for r in {1..3}; do
      job="network_setup/transformations/${prefix}_${r}.job"
      cmd="openfe quickrun $file -o results/replicate_${r}/$name -d results/replicate_${r}/$prefix"
      echo -e "#!/usr/bin/env bash\n${cmd}" > $job
      #sbatch $job
  done
done
