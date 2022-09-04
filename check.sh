#! /bin/bash

for dir in extracted/*/*
do
    # tar -xvf "$dir" 
    # suffix=".tar.gz"
    # foo=${dir%"$suffix"}
    tar -xvf "${dir}" -C "$(dirname "$dir")"
    # rm "${dir}"
    echo "$dir"
    echo "$(dirname "$dir")"
done