#!/usr/bin/env bash

DEPENDENCIES=(
  tmux
  ranger
  vim
  python3
  tldr
  bluez
  bluez-utils
  pipewire
  which
  sudo
  man-db
  lemurs
  rust
  xorg-xinit
  xorg-server
  firefox
  i3-wm
  i3status
  kitty
  eog
  feh
  rofi
  mplayer
  pavucontrol
)
# for i in ${DEPENDENCIES[@]}; do echo PKG $i; done
sudo pacman -S ${DEPENDENCIES[@]}
