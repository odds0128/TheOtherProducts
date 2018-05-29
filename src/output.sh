#!/bin/bash

FS="λ=7.5"
X="turn"
Y=("Finished" "Communication" "Execution")

for item in ${Y[@]}; do
expect -c "
spawn python makeGraph.py

expect \"file names:\" {
send \"$FS\n\"
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

interact
"
done