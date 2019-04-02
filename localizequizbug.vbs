Set fso = CreateObject("Scripting.FileSystemObject")

Set file = fso.OpenTextFile("QuizBug\index.js", 1)

str = file.ReadAll

file.Close

newStr = Replace(str, "quinterest.org", "127.0.0.1")

Set file = fso.OpenTextFile("QuizBug\index.js", 2)

file.WriteLine newStr

file.Close
