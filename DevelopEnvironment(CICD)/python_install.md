# python install information

## python version information

```sh
ls /usr/bin/python*
```

## if not exist /usr/bin/python

```sh
ln -fs /usr/bin/python3.10 /usr/bin/python
```

## if not executable python

```sh
vi ~/.bashrc
```

- modify bashrc file

```sh
alias python="python3"
alias pip="pip3"
alias python-config="python3-config"
```

```sh
source ~/.bashrc
```

## python delete

### python normal delete

```sh
sudo apt-get remove python3.10
```

### Add dependent package and delete

```sh
sudo apt-get remove --auto-remove python3.10
```

### Add python compose and data file and delete

```sh
sudo apt-get purge python3.10
```

### Add python compose and data file and delete all

```sh
sudo apt-get purge --auto-remove python3.10
```

### delete usr/lib python folder

```sh
rm -r /usr/lib/python3.10
```

## WARNING: Running pip as the 'root' user can result in broken permissions

[WARNING: Running pip as the 'root' user can result in broken permissions](https://bobbyhadz.com/blog/python-warning-running-pip-as-the-root-user-can-result-in-broken-permissions)
