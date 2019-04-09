@echo off

pushd QuizBug

npm install .
npm install -g jspm
jspm install .

popd