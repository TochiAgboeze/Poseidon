#!usr/bin/bash

list=($(cat ./sampling_points_ids.txt))

for id in "${list[@]}"
do
    if [[ -f "Monthly_Average_Groundwater_Level/$id.csv" ]]; then
        cp "Monthly_Average_Groundwater_Level/$id.csv" ./487_sampling_points
    fi
done
