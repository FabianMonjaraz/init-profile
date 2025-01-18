#!/usr/bin/env bash

DEPENDENCIES=(
  tmux
  vim
  python3
  i3-wm
  rofi
  mplayer
  bluez
  bluez-utils
  pipewire
  firefox
  which
  sudo
  man-db
)
# for i in ${DEPENDENCIES[@]}; do echo PKG $i; done
sudo pacman -S ${DEPENDENCIES[@]}
