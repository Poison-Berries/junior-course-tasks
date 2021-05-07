# Netcat maths

A ppc task on netcat expressions evaluation. Solver should evaluate 100 sum, difference or
multiplication expressions, each within 2 seconds, numbers are from 1 to 1000.

## Usage

Running a server requires the `ncat` utility (can be installed with `apt install ncat`),
the command is:
```bash
ncat -klp <PORT> -e server.py
```
where `<PORT>` is the port number to listen on. Send a `SIGINT` or press `^C` to stop the
server.

## Author

[Nikolay Nechaev (aka @kolayne)](https://github.com/kolayne). Originally created in 2020,
but modified in 2021
