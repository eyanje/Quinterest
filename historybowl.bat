@echo off

SETLOCAL ENABLEEXTENSIONS

pushd db\python\history_bowl

python .\merge_pdfs.py -a

for /r %%i IN (*.docx) do (
    python ..\read_individual.py "%%i"
)

popd
