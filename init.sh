#!/usr/bin/env bash
FILES_PATH=$(cd -- "$(dirname -- ${BASH_SOURCE[0]})" &>/dev/null && pwd)
while read LOCATION; do
  IFS=: read ORIGIN DEST <<< $LOCATION
  ORIGIN=files/${ORIGIN}
  # eval is used to expand the $HOME or ~ variables inside $DEST
  eval echo "=== Copy data from ${ORIGIN%\*} to $DEST"
  eval [[ ! -d $DEST ]] && mkdir -v -p $DEST
  if [[ $ORIGIN =~ .*\* ]]; then
    # When ussing eval and find together, if -exec is used with '\;' it must be escaped
    # like this: \\\;
    eval find ${FILES_PATH}/${ORIGIN%\*} -maxdepth 1 -mindepth 1 -exec cp -v -r {} $DEST \\\;
  else
    eval cp -v -r ${FILES_PATH}/${ORIGIN} $DEST
  fi
  echo
done < ${FILES_PATH}/locations

[[ -f additional-configurations.sh ]] && bash additional-configurations.sh


echo -e "\n=== All the personal configurations has been setted. Please, restart your session."
