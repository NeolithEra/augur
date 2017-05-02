#!/bin/bash


BASE_STRING=`cat ./augur/VERSION`
BASE_LIST=(`echo $BASE_STRING | tr '.' ' '`)
V_MAJOR=${BASE_LIST[0]}
V_MINOR=${BASE_LIST[1]}
V_PATCH=${BASE_LIST[2]}
echo "Current version : $BASE_STRING"
# V_MINOR=$((V_MINOR + 1))
# V_PATCH=0
V_PATCH=$((V_PATCH + 1))
NEXT_PATCH_VERSION="$V_MAJOR.$V_MINOR.$V_PATCH"
echo "Setting new version to be $NEXT_PATCH_VERSION"
echo $NEXT_PATCH_VERSION > ./augur/VERSION