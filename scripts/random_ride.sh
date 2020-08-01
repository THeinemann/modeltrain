#!/bin/sh

while true
do
    if [ $(($RANDOM % 2)) == 0 ]
    then
        ./one_round_track2.sh
    else
        ./one_round_track1.sh
    fi
    sleep 10
done

