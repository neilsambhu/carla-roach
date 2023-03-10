# /bin/bash

# rm -rfv /usr/src/app/UnrealEngine
# cd /usr/src/app/
# unzip /usr/src/install/UnrealEngine.zip

# cd UnrealEngine
# echo [exe] Setup.sh
# ./Setup.sh
# echo [exe] GenerateProjectFiles.sh
# ./GenerateProjectFiles.sh
# echo [exe] make -j 48
# make -j 48
# echo [exe] chmod -Rv 777 /usr/src/app/UnrealEngine
# chmod -Rv 777 /usr/src/app/UnrealEngine

rm -rfv /usr/src/app/carla
cd /usr/src/app/
unzip /usr/src/install/carla.zip

export UE4_ROOT=/usr/src/app/UnrealEngine

cd carla
# git checkout 0.9.13
echo [exe] Update.sh
./Update.sh
echo [exe] make -j 48 PythonAPI
make -j 48 PythonAPI
echo [exe] make -j 48 launch
make -j 48 launch
echo [exe] chmod -Rv 777 /usr/src/app/carla
chmod -Rv 777 /usr/src/app/carla