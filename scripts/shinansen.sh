#!/usr/bin/sh

source ./commands.sh


function round() {
    direction backward
    speed 35
    switch 1 straight
    switch 2 straight
    section 1 true
    sleep 7
    speed 70
    sleep 5
    speed 100
    sleep 5
    speed 150
    echo "Max speed!"
    sleep 10
    speed 70
    sleep 5
    speed 25
    section 1 false
}

function loop() {
    while true
    do
        round
        sleep 15
        echo "Next round!"
    done
}

if [ "$1" == 'loop' ]
then
    loop
else
    round
fi

