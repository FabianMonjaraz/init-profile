#!/usr/bin/env bash

DEPENDENCIES=(
  tmux
  git
  ranger
  vim
  htop
  bc
  wget
  7zip
  unzip
  openssh
  sshpass
  sshfs
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
  caja
  i3-wm
  i3status
  kitty
  eog
  feh
  rofi
  mplayer
  pavucontrol
  spotify-launcher
  telegram-desktop
  signal-desktop
  docker
  fakeroot
  debugedit
  flameshot
)
# for i in ${DEPENDENCIES[@]}; do echo PKG $i; done
sudo pacman -S ${DEPENDENCIES[@]}
