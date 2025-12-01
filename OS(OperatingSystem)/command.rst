Linux Grep Command
==================

- ``ripgrep`` - Search for processes by name or other attributes.
- `ripgrep <https://github.com/BurntSushi/ripgrep?tab=readme-ov-file#installation>`_.

.. code-block:: shell

    brew install ripgrep
    rg <pattern> <file path>

Fuzzy Finder
============

- ``fzf`` - A command-line fuzzy finder.
- ``find``, ``rg``, ``ls``

.. code-block:: shell

    brew install fzf 
    history | fzf 

- ``vim $(fzf)`` - Open a file selected via fzf in vim.

- https://github.com/junegunn/fzf

tmux
====

.. code-block:: shell

    tmux new -s work
    # ... do works ...
    tmux detach 
    tmux attach -t work

- https://github.com/tmux/tmux/wiki/Getting-Started
- https://thoughtbot.com/blog/a-tmux-crash-course

watch
=====

.. code-block:: shell
    watch -n 2 df -h

- `df -h` - Display disk space usage in human-readable format. (h: human)
- `-n 2` - Update every 2 seconds.
- `watch` - Run a command periodically, showing output fullscreen.

rsync 
=====

.. code-block:: shell
    rsync -avh --progress /source/directory/ /destination/directory/
- `-a` - Archive mode; preserves permissions, timestamps, symbolic links, etc.
- `-v` - Verbose output.
- `-h` - Human-readable output.
- `--progress` - Show progress during transfer.