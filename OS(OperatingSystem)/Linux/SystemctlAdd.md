# Systemctl port recovery

## port check script 

- `cd /`
- `touch reopen.sh`
 
```sh
#!/bin/bash
if ! nc -z localhost 22; then
    echo "22 port not opened"
    systemctl restart sshd.socket 
else
    echo "22 port opened"
fi
```  

## Add systemctl service 

- `/etc/systemd/system` path to add service file. 
- `vi /etc/systemd/system/reopen.service`.

```sh
[Unit]
Description=Reopen sshd.socket ( 22 ) service.

[Service]
Type=oneshot
ExecStart=/reopen.sh

[Install]
WantedBy=multi-user.target
```

- `oneshot` type is just one called.  

## Add Timer file ( instead crontab )

1. create a timer unit file.  
2. Set the timer to trigger every minute.
3. Link the timer to the service.  
4. `vi /etc/systemd/system/reopen.timer`  
5. if you want to set other time, then for example, `10s` is 10 seconds.  
```sh
[Unit]
Description=for run reopen.service every 1 minute.  

[Timer]
OnActiveSec=1min
OnUnitActiveSec=1min
Unit=reopen.service

[Install]
WantedBy=timers.target
```

## Register timer unit to systemctl

```sh
sudo systemctl damon-reload
sudo systemctl enable reopen.timer
sudo systemctl start reopen.timer
```

## check running 

```sh
systemctl status reopen.timer
```

## service running log 

```sh
journalctl -u reopen.service 
```

```sh
journalctl -f -u reopen.service
```

## reference 

- https://man7.org/linux/man-pages/man5/systemd.socket.5.html
- https://velog.io/@markyang92/systemd-timer  

