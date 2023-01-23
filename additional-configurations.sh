#!/usr/bin/env bash
bashrc_configurations() {
  if [[ ! $(which pcregrep) ]]; then
    echo "=== Alert: pcregrep not found; additional .bashrc configurations may need to be setted manually" 
    return 1
  fi
  SEARCH_PATTERN='configFolder=.*\nif \[ -f "\$\{configFolder\}/bash-manager" \]; then' 
  TARGET_FILE=${HOME}/.bashrc
  echo "=== Executing Additional configurations in $TARGET_FILE"
  if [[ ! $( pcregrep -M "$SEARCH_PATTERN" $TARGET_FILE 2>/dev/null ) ]]; then
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
  source $TARGET_FILE

  else
    echo "Configurations in $TARGET_FILE are already present." 
  fi
}

clone_scripts() {
  if [[ ! $(which git) ]]; then
    echo "=== Alert: git not found; couldn't get the scripts project" 
    return 1
  fi

  echo "=== Pulling scripts from github"
  PROJECT="https://github.com/FabianMonjaraz/linux-scripts.git"
  PROJECT_DIR=$(awk -F/ '{print $NF}' <<< ${PROJECT%.*})
  CURRENT=$(pwd)

  [[ ! -d ${HOME}/git ]] && mkdir -v ${HOME}/git
  [[ ! -d ${HOME}/scripts ]] && mkdir -v ${HOME}/scripts

  cd ${HOME}/git
  if [[ ! -d ${PROJECT_DIR}/.git ]]; then
    git clone $PROJECT
    RC=$?
    [[ $RC -ne 0 ]] && return $RC
  else
    cd $PROJECT_DIR
    git pull
    RC=$?
    [[ $RC -ne 0 ]] && return $RC
    cd -
  fi

  echo "=== Linking scripts"
  cd $PROJECT_DIR
  for script in $(ls ./*); do
    ln -s -v -t ${HOME}/scripts $(realpath $script) 2>/dev/null
  done
  cd $CURRENT
}

bashrc_configurations
clone_scripts
