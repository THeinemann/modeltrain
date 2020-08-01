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


speed 90
direction backward
switch 1 straight
switch 2 straight
section 1 true
sleep 3
section 1 false
section 1 false

