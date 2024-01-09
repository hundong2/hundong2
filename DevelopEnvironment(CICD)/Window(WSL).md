# WSL environment setting

## User Password Setting

### WSL

```sh
wsl --user root
```

- execute wsl and input 'passwd' 
- setting new password 
- setting user {User}

```sh
wsl --user <User>
```

### ubuntu

```sh
ubuntu config --default-user root
```

- execute ubuntu and input 'passwd command'
- setting new password
- setting user {User}

```sh
root@User:~# passwd
New password:
Retype new password:
exit
ubuntu config --default-user "User"
```

