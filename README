Description
===========
Pydiction allows you to Tab-complete Python code in Vim, including keywords, the standard library, and third-party modules.  

It consists of three main files:
    
    python_pydiction.vim -- This is an ftplugin you put in your non-system ftplugin directory (i.e., ~/.vim/after/ftplugin/, on Unix or C:\vim\vimfiles\ftplugin\, on Windows)
    complete-dict -- This is a vim dictionary file that consists of Python keywords and modules. This is what python_pydiction.vim looks at to know which things are completable.
    pydiction.py -- (Not required) This is a Python script that was used to generate complete-dict. You can optionally run this script to add more modules to complete-dict.


Install Details
===============
Unix/Linux: Put python_pydiction.vim in ~/.vim/after/ftplugin/   (If this directory doesn't already exist, create it. Vim will know to look there automatically.)
Windows: Put python_pydiction.vim in C:\vim\vimfiles\ftplugin  (Assuming you installed Vim to C:\vim\).

You may install the other files (complete-dict and pydiction.py) anywhere you want. For this example, we'll assume you put them in "C:\vim\vimfiles\ftplugin\pydiction\" (Do not put any file but python_pydiction.vim in the ftplugin\ directory, only .vim files should go there.)

In your vimrc file, first add the following line to enable filetype plugins:
  
    filetype plugin on

then make sure you set "g:pydiction_location" to the full path of where you installed complete-dict, i.e.:
    
    let g:pydiction_location = 'C:/vim/vimfiles/ftplugin/pydiction/complete-dict'

You can optionally set the height of the completion menu by setting "g:pydiction_menu_height" in your vimrc. For example:
    
    let g:pydiction_menu_height = 20

The default menu height is 15.

Note: If you were using a version of Pydiction less than 1.0, make sure you delete the old pydiction way of doing things from your vimrc. You should ***NOT*** have this in your vimrc anymore:

        if has("autocmd")
           autocmd FileType python set complete+=k/path/to/pydiction iskeyword+=.,(
        endif " has("autocmd") 


Usage
=====
Type part of a Python keyword, module name, attribute or method in "insert mode" in Vim, then hit the TAB key and it will auto-complete.

For example, typing:

    raw<Tab>

will bring up a menu of possibilities, such as:

    raw_input(
    raw_unicode_escape_decode(
    raw_unicode_escape_encode(

Typing:

    os.p<Tab>

pops up:

    os.pardir
    os.path
    os.pathconf(
    os.pathconf_names
    os.pathsep
    os.pipe(
    ...

Typing:

    co<Tab>

pops up:

    continue
    coerce(
    compile(
    ...

and so on.

As of Pydiction 1.2, there's support for completing modules that were imported via "from module import submodule". For example, you could do:

    from xml.parsers import expat
    expat.P<Tab>

which expands to:

    expat.ParserCreate(

You can also now use Shift-Tab to Tab backwards through the popup menu.

If you feel you're getting different results in your completion menu, it's probably because you don't have Vim set to ignore case. You can remedy this with ":set noic"
        

Pydiction versus other forms of completion
==========================================
Pydiction can complete Python Keywords, as well as Python module names and their attributes and methods. It can also complete both the fully-qualified module names such as "module.method", as well as non-fully qualified names such as simply "method".

Pydiction only uses the "Tab" key to complete, uses a special dictionary file to complete from, and only attempts to complete while editing Python files. This has the advantages of only requiring one keystroke to do completion and of not polluting all of your completion menus that you may be using for other types of completion, such as Vim's regular omni-completion, or other completion scripts that you may be running.

Since pydiction uses a dictionary file of possible completion items, it can complete 3rd party modules much more accurately than other ways. You have full control over what it can and cannot complete. If it's unable to complete anything you can either use pydiction.py, to automatically add a new module's contents to the dictionary, or you can manually add them using a text editor. The dictionary is just a plain text file, which also makes it portable across all platforms.  For example, if you're a PyQT user, you can add all the PyQT related modules to the dictionary file (complete-dict) by using pydiction.py. The latest default complete-dict already contains most of the standard library, all Python 2.x keywords, Pygame, OpenGL, wxPython, Twisted, PyQT4, ZSI, LDAP, numarray, PyGTK, MySQLdb, PyGreSQL, pyPgSQL, PythonCard, pyvorbis, bcrypt, openid, GnuPGInterface, OpenSSl, pygments and more.

Also, because pydiction uses a dictionary file, you don't have to import a module before you can complete it, nor do you even have to have the module installed on your machine. This makes completion very fast since it doesn't need to do any type deducing. It also frees you up to use pydiction as a way of looking up what a module or submodule without having to install it first.

If you want to, you can still use Vim 7's built-in omni-completion for Python (pythoncomplete.vim), and other forms of ins-completion, with Pydiction. In fact, they can all make a great team.

Pydiction knows when you're completing a callable method or not and, if you are, it will automatically insert an opening parentheses.

The Tab key will work as normal for everything else. Pydiction will only try to use the Tab key to complete Python code if you're editing a Python file and you first type part of some Python module or keyword.

Pydiction doesn't even require Python support to be compiled into your version of Vim.


python_pydiction.vim (filetype plugin)
======================================
Pydiction will make it so the Tab key on your keyboard is able to complete python code.

Version 1.0 and greater of Pydiction uses a new file called python_pydiction.vim, which is an ftplugin that only activates when you're editing a python file (e.g., you're editing a file with a ".py" extension or you've manually typed ":set filetype=python").  Past versions of pydiction didn't use a plugin and instead just required you to change the value of "isk" in your vimrc, which was not desirable. Version 1.0 and greater do not require you to manually change the value of isk. It now safely changes isk for you temporarily by only setting it while you're doing Tab-completion of Python code, and it automatically changes it back to its original value whenever Tab-completion isn't being activated.  Again, only Tab-completion causes pydiction to activate; not even other forms of ins-completion, such as <Ctrl-x> or <Ctrl-n> completion will activate pydiction, so you're still free to use those other types of completion whenever you want to.

Pydiction works by using Vim's ins-completion functionality by temporarily remapping the Tab key to do the same thing as I_CTRL-X_CTRL_K (dictionary only completion). This means that whenever you're editing a Python file, and you start typing the name of a python keyword or module, you can press the Tab key to complete it. For example, if you type "os.pa" and then press Tab, Pydiction will pop up a completion menu in Vim that will look something like:

    os.pardir
    os.path
    os.pathconf(
    os.pathconf_names
    os.path.
    os.path.__all__
    os.path.__builtins__
    os.path.__doc__
    ...

Pressing Tab again while the menu is open will scroll down the menu so you can choose whatever item you want to go with, using the popup-menu keys:

    CTRL-Y        Accept the currently selected match and stop completion.
    <Space>      Accept the currently selected match and insert a space.
    CTRL-E       Close the menu and not accept any match.
    ....

hitting Enter will accept the currently selected match, stop completion, and insert a newline, which is usually not what you want. Use CTRL-Y or <Space>, instead. See ":help popupmenu-keys" for more options.

As of Pydiction 1.3, you can press Shift-Tab to Tab backwards as well.

Pydiction temporarily sets completeopt to "menu,menuone", so that you can complete items that have one or more matches. It will set it back to whatever the original value you have completeopt set to when Tab-completion isn't being activated.

By default, Pydiction ignores case while doing Tab-completion. If you want it to do case-sensitive searches, then set noignorecase (:set noic).


pydiction.py
============
Note: You can skip this section if you don't plan to add more modules to complete-dict yourself.  Check if complete-dict already has the modules you intend to use.

This is the Python script used to create the "complete-dict" Vim dictionary file.  I have created and bundled a default complete-dict for your use. I created it using Ubuntu 9.04 Linux, so there won't be any real win32 specific support in it. You're free to run pydiction.py to add, or upgrade, as modules as you want.  The dictionary file will still work if you're using windows, but it won't complete win32 related modules unless you tell it to.      

Usage: In a command prompt, run:

    $ python pydiction.py <module> ... [-v]

(You need to have python 2.x installed.)

Say you wanted to add a module called "mymodule" to complete-dict, do the following:

    $ python pydiction.py mymodule

You can input more than one module name on the command-line, just separate them by spaces:

    $ python pydiction.py mymodule1 mymodule2 mymodule3

The -v option will just write the results to stdout (standard output) instead of the complete-dict file.

If the backfup file "complete-dict.last" doesn't exist in the current directory, pydiction.py will create it for you. You should always keep a backup of your last working dictionary in case anything goes wrong, as it can get tedious having to recreate the file from scratch.

If complete-dict.last already exists, pydiction will ask you if you want to overwrite your old backup with the new backup.

If you try to add a module that already exists in complete-dict, pydiction will tell you it already exists, so don't worry about adding duplicates. In fact, you can't add duplicates, every time pydiction.py runs it looks for and removes any duplicates in the file.

When pydiction adds new modules to complete-dict, it does so in two phases. First, it adds the fully-qualified name of the module. For example:

    module.attribute
    module.method(

then it adds the non-fully qualified name:

    attribute
    method(

this allows you to complete your python code in the way that you imported it. E.g.:

    import module

or:

    from module import method

Say you want to complete "pygame.display.set_mode". If you imported Pygame using "import pygame", then you can Tab-complete using:

    pygame.di<Tab>

to expand to "pygame.display.". Then type:

    se<Tab>

to expand to "pygame.display.set_mode("

Now say you imported using "from pygame import display". To expand to "display.set_mode(" just type:

    display.se<Tab>

And if you imported using "from pygame.display import set_mode" just type:

    se<Tab>

Keep in mind that if you don't use fully-qualified module names then you might get a lot of possible menu options popping up, so you may want to use more than just two letters before you hit Tab, to try to narrow down the list.

As of Pydictoin 1.1, there is also limited support for string type method completion. For example:

    "".jo<Tab>"

will expand to:

    "".join(

make sure you type at least two letters of the method name if this doesn't seem to work.

This only works for quoted strings, ie:

    'foo bar'.st<Tab>
    
to get

    'foo bar'.startswith(

but you can't yet do:

    s = 'foo bar'

    s.st<Tab>

if you want that behavior you can still use Vim 7's omni-completion:

    s.st<Ctrl-x><Ctrl-o>

which will also give you a preview window describing the methods as well as the argument list the methods take, e,g:

    startswith(prefix[, start[, end]])
    strip([chars])

To Tab-complete your own personal modules, you put your functions in a separate file to be reused, as you normally would. For example, say you put the following function in a file called "myFoo.py":

    def myBar():
        print "hi"

you would then need to add myFoo to complete-dict by doing:

    ./pydiction.py myFoo

now you can complete myFoo.myBar() by doing:  

    myFoo.my<Tab>

You don't have to restart Vim after you update complete-dict.


complete-dict
=============
This is the Vim dictionary file that python_pydiction.vim reads from and pydiction.py writes to. Without this file, pydiction wouldn't know which Python keywords and modules it can Tab-complete.

complete-dict is only an optional file in the sense that you can create your own complete-dict if you don't want to use the default one that is bundled with Pydiction.  The default complete-dict gives you a major head start, as far as what you can Tab-complete, because I did my best to put all of the Python keywords, standard library and even some popular third party modules in it for you.

The default complete-dict currently contains:

    Python keywords:

        and, del, for, is, raise, assert, elif, from, lambda, return, break, else, global, not, try, class, except, if, or, while, continue, exec, import, pass, yield, def, finally, in, print    

    Most of the standard library and built ins:  
        
        __builtin__, __future__, os, sys, time, re, sets, string, math, Tkinter, hashlib, urllib, pydoc, etc...

    It also contains some popular third-party libraries:

        Pygame, wxPython, Twisted, ZSI, LDAP, OpenGL, PyGTK, PyQT4, MySQLdb, PyGreSQL, pyPgSQL, SQLite, PythonCard, Numarray, pyvorbis, Bcrypt, OpenID, GnuPGInterface, OpenSSL and Pygments.

    Make sure you download the latest version of Pydiction to get the most up-to-date version of complete-dict. New modules are usually added to it every release.

If you open complete-dict in your text editor you'll see sections in it for each module, such as:

    --- import os ---
    os.EX_CANTCREAT
    os.EX_CONFIG
    os.EX_DATAERR
    ...

    --- from os import * ---
    EX_CANTCREAT
    EX_CONFIG
    EX_DATAERR
    ...

If certain attributes seem to be missing, it's probably because pydiction removed them because they were duplicates. This mainly happens with the non-fully qualified module sections. So first try searching the entire file for whatever string you assume is missing before you try adding it. For example, if you don't see:

    __doc__

under:

    --- import sys ---

it's probably because a previous module, such as "os", already has it.
    
If you try to recreate complete-dict from scratch, you'll need to manually add the Python keywords back to it, as those aren't generated with pydiction.py.

If you don't want certain things to Tab-complete, such as Python keywords or certain modules, simply delete them by hand from complete-dict.

Pydiction doesn't ignore "private" attributes or methods. I.e., those starting (but not ending) with one or two underscores, e.g., "_foo" or "__foo".  I have manually deleted things starting with a single underscore from the included complete-dict just to keep it a little more sane--since there were so many.  In sticking with the Python tradition of not forcing things to be private, I have left it up to the user to decide how they want to treat their own things.  If you want to delete them from your custom complete-dict's, you can use a regex to try to delete them, such as doing:

    :g/\._[a-zA-Z]/d
    :g/^_[a-zA-Z]/d
    :g/^\%(_\=[^_]\)*\zs__\%(.\{-}__\)\@!/d
    etc...


Tips
====
-Say you create a custom object, called "S" by doing something like:
    
         S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

you can complete dynamic object methods, such as "S.send()", by using Vim 7's omni-completion ftplugin (a.k.a "pythoncomplete.vim") by doing:

        S.s<Ctrl-x><Ctrl-o>

-You may get unexpected results if you use autocomplpop.vim, supertab.vim or other completion or python plugins. Try disabling them individually to find out the culprit and please don't hesitate to e-mail me any workarounds or suggestions. Thanks.


License
=======
As of version 1.0, Pydiction is now under a BSD license instead of GPL.


Further reading
===============
:help ftplugin
:help 'complete
:help compl-dictionary
:help popupmenu-completion
:help popupmenu-keys
:help iskeyword
http://docs.python.org/modindex.html

