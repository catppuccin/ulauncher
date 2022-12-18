#!/bin/bash

if ! which ulauncher >/dev/null; then
    echo "Couldn't find ulauncher"
fi

if which python >/dev/null; then

    python ${PWD}/options.py $@
else

    python3 $PWD/options.py $@
fi
