# Nuget Error

## Unable to load the service index for source https://api.nuget.org/v3/index.json

```sh
apt remove --purge -V ca-certificates
apt install ca-certificates -y
```

or

```sh
SSL_CERT_DIR=/etc/pki/tls/certs
SSL_CERT_FILE=/etc/pki/tls/certs/ca-bundle.crt
```

or

```sh
echo $SSL_CERT_DIR
```

is nothing then

```sh
SSL_CERT_DIR=/etc/ssl/certs
```

## error NU1301: Failed to retrieve information about 'Microsoft.NETCore.App.Host.win-x64' from remote source 'https://api.nuget.org/v3-flatcontainer/microsoft.netcore.app.host.win-x64/index.json'.

```sh
dotnet dev-certs https --trust
```

### reference

- [linuxquestions](https://www.linuxquestions.org/questions/linux-from-scratch-13/nuget-error-ssl-connection-could-not-be-established-4175711236/)
- [stackoverflow](https://stackoverflow.com/questions/41157069/nuget-not-connecting)
- [microsoft-nuget.config](https://learn.microsoft.com/ko-kr/nuget/reference/nuget-config-file#config-section)
-
