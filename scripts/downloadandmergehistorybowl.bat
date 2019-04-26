@echo off

pushd ..\db\python\history_bowl

python download_nationals.py
python download_regionals.py
python merge_auto.py

popd