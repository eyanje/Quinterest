@echo off

pushd db\python\history_bowl

python .\merge_pdfs.py

echo Please convert the pdfs in db/python/history_bowl into docx files and place them back ito db/python/history_bowl.
echo https://pdf2docx.com/ works
echo After that, run historybowl.bat

popd