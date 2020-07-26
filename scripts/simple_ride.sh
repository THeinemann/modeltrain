#!/bin/sh

HOST=pi
PORT=5000

function speed() {
    curl "$HOST:$PORT/speed" -X PUT -H Content-Type:application/json -d "$1"
}

function direction() {
    curl "$HOST:$PORT/direction" -X PUT -H Content-Type:application/json -d "\"$1\""
}

function switch() {
    curl "$HOST:$PORT/switches/$1/$2" -X PUT
}

function section() {
    curl "$HOST:$PORT/sections/$1" -X PUT -H Content-Type:application/json \
         -d "{\"enabled\": $2}"
}


while true
do
    ./one_round_track1.sh
    sleep 10
    ./one_round_track2.sh
    sleep 10
done

