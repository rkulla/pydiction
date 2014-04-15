Description
===========
Pydiction allows you to Tab-complete Python code in Vim such as keywords, built-ins, standard library, and third-party modules. 

It doesn't require installing any dependencies. It simply consists of three main files:
    
    python_pydiction.vim  -- Vim plugin that autocompletes Python code.
    complete-dict         -- Dictionary file of Python keywords, modules, etc.
    pydiction.py          -- Python script to add more words to complete-dict.

The bundled dictionary comes with most things you will likely need in your day-to-day Python programming, and the included
Python script allows you to easily append new modules to the dictionary. So you don't have to wait around for me to add them.
And you can teach Pydiction to complete your project's own API very quickly. Some third-party libraries already supported are:
`Django` `Flask` `Requests` `Twisted` `Numpy` `Psycopg2` `PyGreSQL` `SQLite3` `MySQLdb` `OpenGL` `Pygame` `wxPython` `PyGTK` 
`PyQT4` `OpenID` `Scrapy` `Celery` and more.

Since Pydiction just uses a flat dictionary file, it's extremely flexible because you can do things like re-order how you want
things to appear in your popup completion menus. By default it will be in alphabetical order, but if you want `else` to come 
before `elif`, you can.

Pydiction is often misunderstood when compared to other forms of python code completion. Pydiction doesn't have to do 
any source code analysis. It only uses the dictionary of terms. This is its strength and weakness when used alone. It's a
strength because of how stable it allows the plugin to be. And Pydiction really shines when completing 3rd party libraries
and frameworks and basic keywords, but not for things that dictionary completion isn't suited for. For that, you'll want 
omni-completion too. See the `Tips` section for how to get the best of all worlds. 

Installation
============
If you have Pathogen installed:

    cd ~/.vim/bundle
    git clone https://github.com/rkulla/pydiction.git

or use a plugin manager like Vimogen (https://github.com/rkulla/vimogen) to install and manage Pydiction and all of your plugins.

Otherwise:

    - UNIX/LINUX/OSX: Put python_pydiction.vim in ~/.vim/after/ftplugin/ 
    Create this directory if doesn't yet exist. Vim looks there automatically

    - WINDOWS: Put python_pydiction.vim in C:\vim\vimfiles\ftplugin\
    Assuming you installed Vim to C:\vim\

You may install complete-dict and pydiction.py anywhere (see the Configuration section),
but only python_pydiction.vim in the ftplugin directory because for .vim files only.

Configuration
=============
In your vimrc file, first add the following line to enable filetype plugins:
  
    filetype plugin on

then make sure you set g:pydiction_location to the full path of where you installed complete-dict. Ex:
    
    let g:pydiction_location = '/path/to/complete-dict'

for example, if you used Pathogen to install Pydiction, you would set this to:

    let g:pydiction_location = '/home/user/.vim/bundle/pydiction/complete-dict'

and the dictionary will be available to all of your virtualenv's as well.

You can change the height of the completion menu by setting g:pydiction_menu_height in your vimrc:
    
    let g:pydiction_menu_height = 3

The default menu height is 8, meaning 8 items at a time will be shown. Some people prefer more or less and you can make it as large as you want since it will automatically know where to position the menu to be visible.

If you want to configure other things, such as how to get Pydiction to work with other plugins like `SnipMate` or the color of the menu, see the `Tips` section of this documentation.


Usage (Plugin)
==============
In Vim's INSERT mode, type part of a Python keyword, module name, attribute or method, then hit TAB:

    raw<Tab>

will bring up a menu of possibilities, such as:

    raw_input(
    raw_unicode_escape_decode(
    raw_unicode_escape_encode(

Pressing `Tab` again scrolls down the menu so you can select something else. Then type a popup-menu key:

    <Space>              -- Accept current match and insert a space.
    CTRL-Y               -- Accept current match and and don't insert a space.
    <Enter>              -- Accept current match and insert a newline.
    <ESC> or CTRL-E      -- Close the menu and do not accept any match.

    You can also now use Shift-Tab to Tab backwards through the popup menu.

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

Typing:

    dj[Tab]

pops up:

    django
    django.db
    django.utils
    django.conf
    django.template
    ...

Typing:

    def __i<Tab>

pops up:

    def __init__(
    def __iter__(

You can complete modules that were imported via `from module import submodule`. For example:

    from xml.parsers import expat
    expat.P<Tab>

expands to:

    expat.ParserCreate(

Python's newer `import module as X` syntax isn't supported by default, since it would be impossible for Pydiction to know what you'll alias a module to. However, you can either add the alias to complete-dict or just use pythoncomplete.vim's Omnicompletition by typing `<C-X><C-O>`. You can also use the omni-completion to complete other things that aren't in the complete-dict dictionary, such as variables:

    i = 3
    i.b<Ctrl-x><Ctrl-o>   # expands to: i.bit_length(

The same goes for relative import syntax. I have included a few common Django relative import words such as `.models` `.views` and `.forms` and you can add more.

See my Tips section below for more.


If you feel you're getting different results in your completion menu, it's probably because you don't have Vim set to ignore case. You can remedy this with ":set noic". It also helps to type at least 2 letters before hitting Tab, to help Vim narrow down what you mean to complete.
        
Usage (Dictionary generator)
============================
You can skip this section if you don't plan to add more modules to complete-dict yourself. Consult complete-dict to see if it already has the modules you intend to use.

This is the Python script used to create the "complete-dict" Vim dictionary file. I have curated and bundled a default complete-dict for your use. I created it using a Linux system, so there won't be many real win32 specific modules in it. You're free to run pydiction.py to add or upgrade as many modules as you need. The dictionary file will still work if you're using windows, but it won't complete win32 related modules unless you tell it to. 

USAGE: At a command prompt, run:

    $ python pydiction.py <module> [<module> ...] [-v]

(You need to have at least python 2.x installed.)

Say you wanted to add a module called "mymodule" to complete-dict. Do the following:

    $ python pydiction.py mymodule

You can input more than one module name on the command-line by separating them with spaces:

    $ python pydiction.py mymodule1 mymodule2 mymodule3

The -v option will just write the results to stdout (standard output) instead of the complete-dict file:

    $ ./pydiction.py -v datetime math

If the backup file "complete-dict.last" doesn't exist in the current directory, pydiction.py will create it for you. You should always keep a backup of your last working dictionary in case anything goes wrong, as it can get tedious having to recreate the file from scratch.

If complete-dict.last already exists, the script will ask if you want to overwrite your old backup with the new backup.

If you try to add a module that already exists in complete-dict, Pydiction will tell you it already exists, so don't worry about adding duplicates. In fact you can't add duplicates because every time pydiction.py runs it looks for and removes any duplicates in the file.

When pydiction.py adds new modules to complete-dict, it does so in two phases. First it adds the fully-qualified name of the module. For example:

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

Now say you imported using "from pygame import display". To expand to "display.set_mode(" type:

    display.se<Tab>

And if you imported using "from pygame.display import set_mode" type:

    se<Tab>

Keep in mind that if you don't use fully-qualified module names then you might get a lot of possible menu options popping up, so you may want to use more than just two letters before you hit Tab, to try to narrow down the list.

As of Pydiction 1.1 there is also limited support for string type method completion. For example:

    "".jo<Tab>"

will expand to:

    "".join(

make sure you type at least two letters of the method name if this doesn't seem to work.

This only works for quoted strings, ie:

    'foo bar'.st<Tab>
    
to get:

    'foo bar'.startswith(

but you can't do:

    s = 'foo bar'

    s.st<Tab>

if you want that behavior you can still use Vim 7's omni-completion:

    s.st<Ctrl-x><Ctrl-o>

which will also give you a preview window describing the methods as well as the argument list the methods take, e,g:

    startswith(prefix[, start[, end]])
    strip([chars])

To Tab-complete your own personal modules, you can put your functions in a separate file to be reused, as you normally would. For example, say you put the following function in a file called "myFoo.py":

    def myBar():
        print "hi"

you would then need to add myFoo to complete-dict by doing:

    $ ./pydiction.py myFoo

now you can complete myFoo.myBar() by doing:  

    myFoo.my<Tab>

Note: You don't have to restart Vim after you update complete-dict nor do you have to use the pydiction.py script to add stuff to it; it's just a text file that you can also manually edit.


About python_pydiction.vim
==========================
See the `Usage (vim)` section if you just want to know how to use Pydiction inside of Vim. This section will go into detail what this plugin does behind the scenes.

Pydiction version 1.0 and greater uses a file called python_pydiction.vim, which is an ftplugin that only activates when you're editing a python file (e.g., you're editing a file with a .py extension or you've manually typed `:set filetype=python`). 

Past versions of pydiction didn't use a plugin but only required you to change the value of "isk" in your vimrc, which was not desirable. Version 1.0 and greater do not require you to manually change the value of isk. It now safely changes isk for you temporarily by only setting it while you're doing Tab-completion of Python code. It automatically changes isk back to its original value whenever Tab-completion isn't being activated. Again, only Tab-completion causes Pydiction to activate; not even other forms of ins-completion, such as `<Ctrl-x>` or `<Ctrl-n>` completion will activate Pydiction. So you're still free to use those other types of completion whenever you want to.

Pydiction works by using Vim's dictionary ins-completion functionality by temporarily remapping the Tab key to do the same thing as `I_CTRL-X_CTRL_K` (dictionary only completion). So when you are editing a Python file and you start typing the name of a Python keyword or module, you can press the Tab key to complete it. For example, if you type os.pa then press Tab, a pop up completion menu opens with:

    os.pardir
    os.path
    os.pathconf(
    os.pathconf_names
    os.path.
    os.path.__all__
    os.path.__builtins__
    os.path.__doc__
    ...

Pressing Tab again while the menu is open will scroll down the menu. Then you should use a popup-menu key:

    <Space>               Accept current match and insert a space.
    CTRL-Y                Accept current match and and don't insert a space.
    <Enter>               Accept current match and insert a newline.
    <ESC> or CTRL-E       Close the menu and do not accept any match.

    See `:help popupmenu-keys` for more options.

As of Pydiction 1.3 you can press Shift-Tab to complete searches in backwards order.

Pydiction temporarily sets completeopt to "menu,menuone", so that you can complete items that have one or more matches. It will set completeopt back to what it was originally after Tab-completion has finished.

By default, Pydiction ignores case while doing Tab-completion. If you want it to do case-sensitive searches, then `set noignorecase` (:set noic).


About complete-dict
===================
This is the dictionary file that python_pydiction.vim reads from and pydiction.py writes to. Without this file, Pydiction wouldn't know which Python keywords, built-ins and modules it can Tab-complete.

You can create your own complete-dict if you don't want to use the default one. The default complete-dict gives you a major head start as far as what you will be able to Tab-complete.

The default complete-dict currently contains python keywords: `and` `as` `assert` `break` `class` `continue` `def` `del` `elif` `else` `except` `exec` `finally` `for` `from` `global` `if` `import` `in` `is` `lambda` `nonlocal` `not` `or` `pass` `print` `raise` `return` `try` `while` `with` `yield`

It also contains most of the standard library and built-ins:  `__builtin__` `__future__` `os` `sys` `time` `re` `string` `str` `Tkinter` `urllib` etc.

It even contains complete-dict even comes with many third-party libraries such
as: `Django` `Twisted` `Flask` `Requests` `Numpy` `Psycopg2` `PyGreSQL` `SQLite3` `MySQLdb` `ZSI` `LDAP` `OpenGL` `Pygame` `wxPython` `PyGTK` `PyQT4` `Urwid` `PyOgg` `Bcrypt` `OpenID` `GnuPGInterface` `OpenSSL` `lxml` `Scrapy` `Celery` `Pygments` and more.

And it contains useful dunder methods, conventions, etc such as: `self` `object` `__init__(` `__name__` `__main__` etc. This type of thing was manually added near the top of the bundled file. Anything you want to always appear first should go near the top of the file since it reads top-down.

Because it's just a text file, it's very flexible since you can do things like re-order how you want things to appear in your popup completion menus. By default 
things will appear in alphabetical order, but if you want `else` to come before `elif`, there's nothing stopping you. In fact, the bundled dictionary comes with some keywords and stuff re-arranged by likely usage as best as I could manage.

Make sure you download the latest version of Pydiction to get the most up-to-date version of complete-dict. New modules are usually added to it every release.

If you open complete-dict in your text editor you'll see sections in it for each module, such as:

    --- import os ---
    os.path
    os.chdir(
    os.chmod(
    ...

    --- from os import * ---
    EX_CANTCREAT
    EX_CONFIG
    EX_DATAERR
    ...

If certain attributes seem to be missing, it's probably because Pydiction removed them because they were duplicates. So first try searching the entire file for whatever string you assume is missing before you try adding it. 

If you try to recreate complete-dict from scratch, you'll need to manually add the Python keywords and non-module stuff back into it. See the top few sections of the bundled complete-dict file for what I mean. Instead of deleting the file, I would use those manually added sections as a starting point, and then just append your own stuff from there.

If you don't want certain things to Tab-complete, such as Python keywords or certain modules, you can just delete them by hand from complete-dict.

Pydiction doesn't ignore "private" attributes or methods. I.e., those starting (but not ending) with one or two underscores, e.g., "_foo" or "__foo".  I have deleted most things starting with single underscore or double underscores from the included complete-dict just to keep it a little more sane since there were so many.  Python doesn't force things to be private, and you're free to add them if and when you want them. If you find any that you want to delete, open complete-dict in vim and run

    :g/\._[a-zA-Z]/d
    :g/^_[a-zA-Z]/d
    :g/^\%(_\=[^_]\)*\zs__\%(.\{-}__\)\@!/d
    etc...

Pydiction vs other forms of completion
======================================
- Pydiction doesn't require any dependencies to be installs and you don't even need Python support to be compiled into your version of Vim. The dictionary based completion is very stable because it's native to Vim and the Pydiction plugin is only about 50 lines of code and unlikely to have errors -- not counting potential conflicts with other plugins, but those are usually easily fixable.

- Because Pydiction uses a dictionary file, you don't have to import a module before you can complete it, nor do you even have to have the module installed on your machine. This makes completion very fast since it doesn't need to do any type deducing.

- And because the dictionary file is just a static text file, you re-arrange how you want things to appear in the popup menus. By default things are sorted alphabetically, but if ou want `else` to come before `elif`, you can customize.

- There is only one global instance of the dictionary file, which means pydiction won't try to dynamically create dictionaries in your project's folder. So there's no project folders you have to add to .gitignores or anything. And there's nothing special that you have to do to get Pydiction to work with `virtualenv` or other operating systems.

- It can complete Python Keywords, built-ins, and Python module names and their attributes and methods. It can complete both the fully-qualified and non-fully qualified names. For example: `string.upper(`, `upper(`, `''.upper(`, and so forth.

- Pydiction only uses the "Tab" key to complete, uses a special dictionary file to complete from, and only attempts to complete while editing Python files. This has the advantage of only requiring one keystroke to do completion and of not polluting all of the completion menus that you might be using for other types of completion, such as Vim's regular omni-completion or other completion scripts that you may be running.

- Because Pydiction uses a dictionary file of possible completion items, it can complete 3rd party modules more accurately than other methods. You have full control over what it can and cannot complete. If it's unable to complete anything you can use pydiction.py to add a new module's contents to the dictionary, or you can manually add them using a text editor. In other words, you can teach Pydiction to learn what new things it can complete, just like you can with any snippet-based system -- except the snippets are for autocompleting the rest of a word and not for pasting entire templates like SnipMate does.

- The dictionary is just a text file, which makes it portable across all platforms. For example, if you're a Pyramid user you can add all the Pyramid related modules to the dictionary file.py. The latest default complete-dict already contains all of the standard library, Python keywords, and many 3rd party modules like Django, Twisted, Numpy, Flask, Requests, Pygame, wxPython, PyQT4, PyGTK, Urwid, ZSI, LDAP, MySQLdb, Psycopg2, PyGreSQL, OpenId, OpenSSL, Celery, Scrapy, lxml, Pygments and much more. To see the full-list of python modules Pydiction knows about, open complete-dict in Vim and run `:g/root modules`.

- If you want to you can use use Pydiction in tandem with Vim 7's builtin omni-completion for Python (pythoncomplete.vim) as well as other forms of completion like SnipMate or Python-mode (see the Tips section). In fact, they can all make a great team.

- Pydiction knows when you're completing an attribute vs a callable method. If it's a callable then it will automatically insert an opening parentheses.

- The Tab key will work as normal for everything else. Pydiction will only try to use the Tab key to complete Python code if you're editing a Python file and you first type part of some Python module or keyword.

Tips
====
- If you want to have case-insensitive menu searches, :set ignorecase. Otherwise :set noic. Or add them to your vimrc.

- SnipMate and Pydiction make a great team, but they both use the Tab key to complete. This is easy to fix, by adding the following to your .vimrc file:

        " Remap snipmate's trigger key from tab to <C-J>
        imap <C-J> <Plug>snipMateNextOrTrigger
        smap <C-J> <Plug>snipMateNextOrTrigger

 now `cl[Tab]` will use Pydiction to complete "class" and `cl<C-J>` will use the SnipMate snippet and you can still the tab key to iterate through the snippet placeholders.

- Say you create a custom object, called `S` by doing something like:
    
         S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  You can complete dynamic object methods, such as `S.send()`, by using Vim 7's omni-completion ftplugin "pythoncomplete.vim" (requires Vim to be compiled with Python support) by doing:

        S.s<Ctrl-x><Ctrl-o>

 You must import the module for this to work. (e.g. `import socket`). You may get unexpected results if you use rope.vim, python-mode.vim, autocomplpop.vim, supertab.vim or other completion or python plugins. Try disabling them individually to find out the culprit. I personally think that different types of completion need different commands, and have had a lot of bad luck trying to use SuperTab or similar plugins to try to force everything to use a Tab. If you don't like typing <C-X><C-O> you can remap them to something other than Tab, such as `<Leader>o`:

        imap <Leader>o <C-X><C-O> 

 If you use the `python-mode` plugin, I was able to get omnicomplete to work with it by deleting the line:

        setlocal omnifunc=pymode#rope#completion 
        
 from python-mode/after/ftplugin/python.vim, but YMMV.

- Similarly, you can use omni-completion for completing "import module as" syntax:

        import itertools as itr
        itr.<C-X><C-O>

 Or, if you really want it to work with Pydiction/Tab, then add your alias to complete-dict by copying an existing block like:

        --- import itertools ---
        itertools.chain(
        itertools.ccombinations(
        itertools.count(
        ...

 and paste and edit that to replace itertools with itr:

        --- import itertools as itr ---
        itr.chain(
        itr.ccombinations(
        itr.count(
        ...

 In fact, complete-dict contains some of this already for certain conventions, such as `Psycopg2` conventions of using `conn` and `cur` for connection and cursor objects, respectively. Near the top of the bundled complete-dict I've taken the liberty of adding:
         
        --- Psycopg2 / PEP 249 (Assumes conventional object names: conn and cur) ---
        conn.close(
        conn.commit(
        conn.rollback(
        conn.cursor(
        ...
        cur.execute(
        cur.executemany(
        cur.fetchall(
        ...

- Vim comes with other forms of insert completion, such as completing keywords in the current file. Here's the full list:

        1. Whole lines                                  |i_CTRL-X_CTRL-L|
        2. keywords in the current file                 |i_CTRL-X_CTRL-N|
        3. keywords in 'dictionary'                     |i_CTRL-X_CTRL-K|
        4. keywords in 'thesaurus', thesaurus-style     |i_CTRL-X_CTRL-T|
        5. keywords in the current and included files   |i_CTRL-X_CTRL-I|
        6. tags                                         |i_CTRL-X_CTRL-]|
        7. file names                                   |i_CTRL-X_CTRL-F|
        8. definitions or macros                        |i_CTRL-X_CTRL-D|
        9. Vim command-line                             |i_CTRL-X_CTRL-V|
        10. User defined completion                     |i_CTRL-X_CTRL-U|
        11. omni completion                             |i_CTRL-X_CTRL-O|
        12. Spelling suggestions                        |i_CTRL-X_s|
        13. keywords in 'complete'                      |i_CTRL-N|

  Number 3 is what Pydiction does for you when you press Tab.

- Because pydiction.py will complain if you try to add a module that already exists, this can make updating an existing module a little harder.
The workaround is to edit complete-dict and manually delete the related module sections. For example to update `__future__`, delete the sections `-- import __future__ ---` and `--- from __future__ import * ---`.

 Pydiction v1.2.2 and greater adds special markers in each module section of complete-dict that tell you if a module is a "root module", meaning it's a top-level module or package that was specified as an argument to pydiction.py. This is helpful because pydiction.py will automatically dig into as many submodules as it can find, but it doesn't know about separate packages. For example `curses.textpad`, `curses.ascii`, `curses.panel` and `curses.wrapper` are not submodules of 'curses', so they have to be added separately, like:

        $ ./pydiction curses curses.textpad curses.ascii curses.panel

 Fortunately, you can `grep 'root module' complete-dict` to see a list of all the root modules:

        $ grep 'root module' complete-dict | grep curses
        --- import curses (py2.7.3/linux2/root module) ---
        --- import curses.ascii (py2.7.3/linux2/root module) ---
        --- import curses.textpad (py2.7.3/linux2/root module) ---
        --- import curses.wrapper (py2.7.3/linux2/root module) ---

 As you can see, pydiction.py also adds other information such as which version of Python and which operating system was used to add the module to the dictionary file. It will also put the version of the module if its `.__version__` attribute was set.

- You can change the colors of the popup menu by editing your vim color scheme's source file and changing the values of `Pmenu` `PmenuSel` `PmenuSBar` and `PmenuThumb`. If you're using Vim in a terminal, change the values of ctermfg and ctermbg, otherwise change guifg and guibg. I use the molokai colorscheme and a terminal and use:

        " complete menu
        hi Pmenu       ctermfg=green  ctermbg=black guifg=#66D9EF  guibg=#000000
        hi PmenuSel    ctermfg=green  ctermbg=black                guibg=#808080
        hi PmenuSbar                                               guibg=#080808
        hi PmenuThumb                               guifg=#66D9EF

- If you use Vim on Linux, OS X, and Windows you can configure different paths to complete-dict in your vimrc like:

        if has('win32')
          let g:pydiction_location = 'C:/vim/vimfiles/ftplugin/pydiction/complete-dict'
        else
          if system('uname')=~'Darwin'
            let g:pydiction_location = '/Users/you/.vim/bundle/pydiction/complete-dict'
          else
            let g:pydiction_location = '/home/you/.vim/bundle/pydiction/complete-dict'
          endif
        endif

Further reading
===============
`:help ftplugin`
`:help 'complete`
`:help compl-dictionary`
`:help popupmenu-completion`
`:help popupmenu-keys`
`:help iskeyword`

http://docs.python.org/2/py-modindex.html
