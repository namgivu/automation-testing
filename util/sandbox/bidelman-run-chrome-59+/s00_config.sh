#!/usr/bin/env bash

##region common bash util

  #get SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path
  s=${BASH_SOURCE} ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ;
  SCRIPT_HOME=$s

  s="$SCRIPT_HOME/.." ; s=$(cd "$s" && pwd) ;
  UTIL_HOME=$s

  #import common setting
  source "$UTIL_HOME/common.sh"

##endregion common bash util


#load input
PRIVATE_HOME="$SCRIPT_HOME/_private_"