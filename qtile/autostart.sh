#!/bin/bash
nitrogen --restore &
picom --experimental-backends --animations --animation-window-mass 0.5 --animation-for-open-window zoom --animation-stiffness 350 -b &
