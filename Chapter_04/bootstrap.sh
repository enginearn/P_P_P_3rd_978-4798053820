#!/usr/bin/env bash

export LANGUAGE=ja_JP:ja >> $HOME/.bashrc
sudo apt-get update
sudo apt-get upgrade -y
sudo do-release-upgrade -y
sudo apt-get install python3-pip
