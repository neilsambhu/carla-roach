# /bin/bash

rm -rfv /usr/src/app/UnrealEngine-carla

# git clone --depth 1 -b carla git@github.com:CarlaUnreal/UnrealEngine.git
unzip /usr/src/install/UnrealEngine-carla.zip

cd UnrealEngine-carla

echo [exe] git checkout carla
git checkout carla

echo [exe] Setup.sh
./Setup.sh

echo [exe] GenerateProjectFiles.sh
./GenerateProjectFiles.sh