@echo off
del /Q QuizBug.zip
curl https://codeload.github.com/quid256/QuizBug/zip/master --output QuizBug.zip
del /Q QuizBug
rmdir /S /Q QuizBug
unzip -o -q -d . QuizBug.zip
move /Y QuizBug-master QuizBug
del QuizBug.zip

scripts\localizequizbug.vbs
