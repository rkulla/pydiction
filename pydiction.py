#!/usr/bin/env python
"""

pydiction.py 1.2.3 by Ryan Kulla (rkulla AT gmail DOT com).
License: BSD.

Description: Creates a Vim dictionary of Python module attributes for Vim's
             completion feature.  The created dictionary file is used by
             the Vim ftplugin "python_pydiction.vim".

Usage: pydiction.py <module> [<module> ...] [-v]

Example: The following will append all the "time" and "math" modules'
         attributes to a file, in the current directory, called "pydiction",
         with and without the "time." and "math." prefix:

             $ python pydiction.py time math

         To output only to stdout and not append to file, use -v:

             $ python pydiction.py -v time math
"""


__author__ = "Ryan Kulla (rkulla AT gmail DOT com)"
__version__ = "1.2.3"
__copyright__ = "Copyright (c) 2003-2014 Ryan Kulla"


import os
import sys
import types
import shutil


# Path/filename of the vim dictionary file to write to:
PYDICTION_DICT = r'complete-dict'
# Path/filename of the vim dictionary backup file:
PYDICTION_DICT_BACKUP = r'complete-dict.last'

# Sentintal to test if we should only output to stdout:
STDOUT_ONLY = False


def get_submodules(module_name, submodules):
    """Build a list of all the submodules of modules."""

    # Try to import a given module, so we can dir() it:
    try:
        imported_module = my_import(module_name)
    except ImportError:
        return submodules

    mod_attrs = dir(imported_module)

    for mod_attr in mod_attrs:
        try:
            if isinstance(getattr(imported_module, mod_attr), types.ModuleType):
                submodules.append(module_name + '.' + mod_attr)
        except AttributeError as e:
            print e

    return submodules

def get_format(imported_module, mod_attr, use_prefix):
    format = ''

    if use_prefix:
        format_noncallable = '%s.%s'
        format_callable = '%s.%s('
    else:
        format_noncallable = '%s'
        format_callable = '%s('

    try:
        if callable(getattr(imported_module, mod_attr)):
            # If an attribute is callable, show an opening parentheses:
            format = format_callable
        else:
            format = format_noncallable
    except AttributeError as e:
        print e

    return format

def write_dictionary(module_name, module_list):
    """Write to module attributes to the vim dictionary file."""
    python_version = '%s.%s.%s' % get_python_version()

    try:
        imported_module = my_import(module_name)
    except ImportError:
        return

    mod_attrs = dir(imported_module)

    # If a module was passed on the command-line we'll call it a root module
    if module_name in module_list:
        try:
            module_version = '%s/' % imported_module.__version__
        except AttributeError:
            module_version = ''
        module_info = '(%spy%s/%s/root module) ' % (
            module_version, python_version, sys.platform)
    else:
        module_info = ''

    write_to.write('--- import %s %s---\n' % (module_name, module_info))

    for mod_attr in mod_attrs:
        format = get_format(imported_module, mod_attr, True)
        if format != '':
            write_to.write(format % (module_name, mod_attr) + '\n')

    # Generate submodule names by themselves, for when someone does
    # "from foo import bar" and wants to complete bar.baz.
    # This works the same no matter how many .'s are in the module.
    if module_name.count('.'):
        # Get the "from" part of the module. E.g., 'xml.parsers'
        # if the module name was 'xml.parsers.expat':
        first_part = module_name[:module_name.rfind('.')]
        # Get the "import" part of the module. E.g., 'expat'
        # if the module name was 'xml.parsers.expat'
        second_part = module_name[module_name.rfind('.') + 1:]
        write_to.write('--- from %s import %s ---\n' %
                       (first_part, second_part))
        for mod_attr in mod_attrs:
            format = get_format(imported_module, mod_attr, True)
            if format != '':
                write_to.write(format % (second_part, mod_attr) + '\n')

    # Generate non-fully-qualified module names:
    write_to.write('--- from %s import * ---\n' % module_name)
    for mod_attr in mod_attrs:
        format = get_format(imported_module, mod_attr, False)
        if format != '':
            write_to.write(format % mod_attr + '\n')


def my_import(name):
    """Make __import__ import "package.module" formatted names."""
    mod = __import__(name)
    components = name.split('.')
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod


def remove_duplicates(seq, keep=()):
    """

    Remove duplicates from a sequence while perserving order.

    The optional tuple argument "keep" can be given to specificy
    each string you don't want to be removed as a duplicate.
    """
    seq2 = []
    seen = set()
    for i in seq:
        if i in (keep):
            seq2.append(i)
            continue
        elif i not in seen:
            seq2.append(i)
        seen.add(i)
    return seq2


def get_yesno(msg="[Y/n]?"):
    """

    Returns True if user inputs 'n', 'Y', "yes", "Yes"...
    Returns False if user inputs 'n', 'N', "no", "No"...
    If they enter an invalid option it tells them so and asks again.
    Hitting Enter is equivalent to answering Yes.
    Takes an optional message to display, defaults to "[Y/n]?".

    """
    while True:
        answer = raw_input(msg)
        if answer == '':
            return True
        elif len(answer):
            answer = answer.lower()[0]
            if answer == 'y':
                return True
                break
            elif answer == 'n':
                return False
                break
            else:
                print "Invalid option. Please try again."
                continue


def main(write_to, module_list):
    """Generate a dictionary for Vim of python module attributes."""
    submodules = []

    for module_name in module_list:
        try:
            my_import(module_name)
        except ImportError, err:
            print "Couldn't import: %s. %s" % (module_name, err)
            module_list.remove(module_name)

    # Step through each command line argument:
    for module_name in module_list:
        print "Trying module: %s" % module_name
        submodules = get_submodules(module_name, submodules)

        # Step through the current module's submodules:
        for submodule_name in submodules:
            submodules = get_submodules(submodule_name, submodules)

    # Add the top-level modules to the list too:
    for module_name in module_list:
        submodules.append(module_name)

    submodules = remove_duplicates(submodules)
    submodules.sort()

    # Step through all of the modules and submodules to create the dict file:
    for submodule_name in submodules:
        write_dictionary(submodule_name, module_list)

    if STDOUT_ONLY:
        return

    # Close and Reopen the file for reading and remove all duplicate lines:
    write_to.close()
    print "Removing duplicates..."
    f = open(PYDICTION_DICT, 'r')
    file_lines = f.readlines()
    file_lines = remove_duplicates(file_lines)
    f.close()

    # Delete the original file:
    os.unlink(PYDICTION_DICT)

    # Recreate the file, this time it won't have any duplicates lines:
    f = open(PYDICTION_DICT, 'w')
    for attr in file_lines:
        f.write(attr)
    f.close()
    print "Done."


def get_python_version():
    """Returns the major, minor, micro python version as a tuple"""
    return sys.version_info[0:3]


def remove_existing_modules(module_list):
    """Removes any existing modules from module list to try"""
    f = open(PYDICTION_DICT, 'r')
    file_lines = f.readlines()

    for module_name in module_list:
        for line in file_lines:
            if line.find('--- import %s ' % module_name) != -1:
                print '"%s" already exists in %s. Skipping...' % \
                    (module_name, PYDICTION_DICT)
                module_list.remove(module_name)
                break
    f.close()
    return module_list


if __name__ == '__main__':
    """Process the command line."""

    if get_python_version() < (2, 3):
        sys.exit("You need at least Python 2.3")

    if len(sys.argv) <= 1:
        sys.exit("%s requires at least one argument. None given." %
                 sys.argv[0])

    module_list = sys.argv[1:]

    if '-v' in sys.argv:
        write_to = sys.stdout
        module_list.remove('-v')
        STDOUT_ONLY = True
    elif os.path.exists(PYDICTION_DICT):
        module_list = remove_existing_modules(sys.argv[1:])

        if len(module_list) < 1:
            # Check if there's still enough command-line arguments:
            sys.exit("Nothing new to do. Aborting.")

        if os.path.exists(PYDICTION_DICT_BACKUP):
            answer = get_yesno('Overwrite existing backup "%s" [Y/n]? ' %
                                PYDICTION_DICT_BACKUP)
            if (answer):
                print "Backing up old dictionary to: %s" % \
                    PYDICTION_DICT_BACKUP
                try:
                    shutil.copyfile(PYDICTION_DICT, PYDICTION_DICT_BACKUP)
                except IOError, err:
                    print "Couldn't back up %s. %s" % (PYDICTION_DICT, err)
            else:
                print "Skipping backup..."

            print 'Appending to: "%s"' % PYDICTION_DICT
        else:
            print "Backing up current %s to %s" % \
                (PYDICTION_DICT, PYDICTION_DICT_BACKUP)
            try:
                shutil.copyfile(PYDICTION_DICT, PYDICTION_DICT_BACKUP)
            except IOError, err:
                print "Couldn't back up %s. %s" % (PYDICTION_DICT, err)
    else:
        print 'Creating file: "%s"' % PYDICTION_DICT

    if not STDOUT_ONLY:
        write_to = open(PYDICTION_DICT, 'a')

    main(write_to, module_list)
