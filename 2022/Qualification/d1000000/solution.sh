#!/bin/bash
read T
for ((t=1; t<=T; t++))
do
    read N
    read -a S
    S=($(for i in ${S[@]}; do echo $i; done | sort -n))
    max_straight=0
    for i in ${S[@]}
    do
        if [ $i -gt $max_straight ]
        then
            max_straight=$((max_straight+1))
        fi
    done
    echo "Case #$t: $max_straight"
done