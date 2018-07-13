#!/bin/bash

FS=("λ=7.5" "λ=2.5" "λ=10" "λ=5.0")
X="turn"
# Y=("Communication" "Execution")
Y=("Finished")

for fs in ${FS[@]} ; do
    for item in ${Y[@]}; do

    expect -c "
    spawn python /Users/r.funato/Documents/Practices/Python/Production/src/makeGraph.py

    expect \"file names:\" {
    send \"$fs\n\"
    } \"(yes/no)\" {
    send \"yes\n\"
    }

    expect \"x-axis\" {
    send \"$X\n\"
    }

    expect \"y-axes\" {
    send \"$item\n\"
    }
    send \"\n\"

    expect \"Which is labeled?\" {
    send \"1\n\"
    }

    interact
    "

    done
done
