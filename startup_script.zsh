#!/bin/zsh

# A script that opens apps needed for work, changes the working directory and displays git status
# In order to properly change directory and display git status (gits) it needs to be sourced

PATH_TO_PROJECT="~/path-to-your-project"

open -a Spotify
open -a ClickUp
open -a Slack
open -a RapidAPI
open -a Safari "https://chat.openai.com"
open -a Safari "https://bitbucket.org"

cd $PATH_TO_PROJECT
xed .
gits

return
