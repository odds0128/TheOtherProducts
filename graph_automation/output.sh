#!/bin/bash

FS=("λ=1.0"  "λ=3.0" "λ=5.0" "λ=7.0" )
X="turn"
# Y=("Communication" "Execution")
Y=("Finished")

for fs in ${FS[@]} ; do
    for item in ${Y[@]}; do

    expect -c "
    spawn python /Users/r.funato/Documents/simple_products/graph_automation/makeGraph.py

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
