# fingerprint error

## fingerprint error ssh

```sh
sudo sed -i s/"#   StrictHostKeyChecking ask"/"   StrictHostKeyChecking no"/g /etc/ssh/ssh_config
cat /etc/ssh/ssh_config | grep StrictHostKeyChecking
```

or

```sh
sudo sed -i 's/#\?StrictHostKeyChecking\s\+ask/StrictHostKeyChecking no/g' /etc/ssh/ssh_config
```
