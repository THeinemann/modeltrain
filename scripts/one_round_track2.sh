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


speed 100
direction forward
switch 1 turn
switch 2 turn
section 2 true
sleep 3
section 2 false
#sleep 3.5
#speed 28
