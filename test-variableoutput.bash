#!/bin/bash

JAIL=`atq`

echo "$JAIL"

## Determine if a bash variable is empty or not ##
if [ -z "${JAIL}" ]; then
    echo "JAIL is unset or set to the empty string"
fi
if [ -z "${JAIL+set}" ]; then
    echo "JAIL is unset"
fi
if [ -z "${JAIL-unset}" ]; then
    echo "JAIL is set to the empty string"
fi
if [ -n "${JAIL}" ]; then
    echo "JAIL is set to a non-empty string"
fi
if [ -n "${JAIL+set}" ]; then
    echo "JAIL is set, possibly to the empty string"
fi
if [ -n "${JAIL-unset}" ]; then
    echo "JAIL is either unset or set to a non-empty string"
fi

