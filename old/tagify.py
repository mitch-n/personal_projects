from random import choice

tags=['<a href="#ErrorLevel">', '<a href="#ExBasic">', '<a href="#ExExtension">', '<a href="SplitPath.htm">', '<a href="#ExObject">', '<a href="../Functions.htm">', '<a href="../Functions.htm#Global">', '<a href="../Functions.htm#AssumeGlobal">', '<a href="../Functions.htm#ArrayConfusion">', '<a href="../misc/ErrorLevel.htm">', '<a href="../misc/RegEx-QuickRef.htm">', '<a href="../misc/RegEx-QuickRef.htm">', '<a href="../misc/RegEx-QuickRef.htm#Options">', '<span class="red">', '<a href="../misc/RegEx-QuickRef.htm#Options">', '<span class="red">', '<a href="../misc/RegEx-QuickRef.htm#Study">', '<a href="FileRead.htm">', '<a href="URLDownloadToFile.htm">', '<a href="../misc/Clipboard.htm">', '<a href="GuiControls.htm#Edit">', '<a href="InStr.htm">', '<a href="RegExReplace.htm">', '<a href="../misc/RegEx-QuickRef.htm">', '<a href="../misc/RegExCallout.htm">', '<a href="InStr.htm">', '<a href="IfInString.htm">', '<a href="StringGetPos.htm">', '<a href="SubStr.htm">', '<a href="SetTitleMatchMode.htm#RegEx">', '<a href="https://www.autohotkey.com/forum/topic16164.html">', '<a href="http://www.pcre.org/">', '<div class="ex" id="ExBasic">', '<div class="ex" id="ExExtension">', '<div class="ex" id="ExObject">', '<h2 id="ErrorLevel">', '<h2 id="MatchObject">', '<span class="ver">', '<html lang="en">', '<link href="../static/theme.css" rel="stylesheet" type="text/css">', '<meta http-equiv="Content-Type" content="text/html; charset=utf-8">', '<meta http-equiv="X-UA-Compatible" content="IE=edge">', '<meta name="description" content="The RegExMatch function determines whether a string contains a pattern (regular expression).">', '<p id="Array">', '<a href="../misc/RegEx-QuickRef.htm#subpat">', '<a href="../misc/Arrays.htm#pseudo">', '<a href="#NamedSubPat">', '<p id="NamedSubPat">', '<a href="#Array">', '<a href="../misc/RegEx-QuickRef.htm#subpat">', '<p id="ObjectMode">', '<span class="ver">', '<span class="red">', '<a href="#MatchObject">', '<a href="../misc/RegEx-QuickRef.htm#subpat">', '<p id="PosMode">', '<span class="red">', '<a href="../misc/RegEx-QuickRef.htm#subpat">', '<a href="../misc/Arrays.htm#pseudo">', '<a href="#NamedSubPat">', '<pre class="Syntax">', '<span class="func">', '<span class="optional">', '<script src="../static/content.js" type="text/javascript">', '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">', '<script type="text/javascript" src="https://www.autohotkey.com/docs/static/source/data_translate.js">', '<script type="text/javascript" src="https://www.autohotkey.com/docs/static/source/data_toc.js">', '<script type="text/javascript" src="https://www.autohotkey.com/docs/static/source/data_index.js">', '<script type="text/javascript" src="https://www.autohotkey.com/docs/static/source/data_search.js">', '<div id="body">', '<div id="head">', '<div class="h-area">', '<div class="h-tabs" style="width: 18em; visibility: visible;">', '<li data-translate="" title="Shortcut: ALT+C" data-content="C̲ontent" class="selected">', '<li data-translate="" title="Shortcut: ALT+N" data-content="In̲dex">', '<li data-translate="" title="Shortcut: ALT+S" data-content="S̲earch">', '<div class="h-tools sidebar">', '<li class="sidebar" title="Hide or show the sidebar" data-translate="">', '<div class="h-tools online visible" style="display: block;">', '<li class="home" title="Go to the homepage" data-translate="">', '<a href="https://www.autohotkey.com">', '<li class="language" title="Change the language" data-translate="2">', '<span data-translate="" data-content="en">', '<ul class="dropdown languages selected" style="list-style: outside none none;">']

message="""
FROM: jason.durrant@ldschurch.org.snowplows.ru
TO: Stan.Lee@churchofjesuschrist.org
Subject: A favor

Stan,

Hello friend how nice too speak to you again. I do not have much tiem, but i need you to purchase $173.22 gift card google play and send me the code. Thank you good buddy ;)

--
Jason Durrant
LDSCHURCH

Pleese respond to this email directly as i am in a meeting.
"""

for letter in message:
    if choice([True,False]):
        print(choice(tags),end='')
    print(letter, end='')
