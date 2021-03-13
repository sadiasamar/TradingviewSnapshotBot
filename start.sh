#!/bin/bash
trap 'kill $(jobs -pr)' SIGINT SIGTERM EXIT
./index.js &
./tvsnapshotbot.py &
wait