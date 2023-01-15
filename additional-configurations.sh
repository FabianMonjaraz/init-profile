#!/usr/bin/env bash
bashrc_configurations() {
  if [[ ! $(which pcregrep) ]]; then
    echo "Alert: pcre is not installed, additional .bashrc configurations must be made manually" 
    return 0
  fi
  SEARCH_PATTERN='configFolder=.*\nif \[ -f "\$\{configFolder\}/bash-manager" \]; then' 
  TARGET_FILE=${HOME}/.bashrc
  echo "=== Executing Additional configurations in $TARGET_FILE"
  if [[ ! $( pcregrep -M "$SEARCH_PATTERN" $TARGET_FILE ) ]]; then
    # cat <<- EOM >> $TARGET_FILE
    echo $TARGET_FILE
    # Enclosing "EOM" in quotes helps to prevent the text to transform the
    # variables used 
    cat << "EOM" >> $TARGET_FILE
configFolder="${HOME}/.config/profile"
if [ -f "${configFolder}/bash-manager" ]; then
  . ${configFolder}/bash-manager
fi
EOM

  else
    echo "Configurations in $TARGET_FILE are already present." 
  fi
}

bashrc_configurations
