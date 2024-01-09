# curl error

```sh
curl: (60) SSL certificate problem: self signed certificate in certificate chain
```

## Resolve

```sh
vim  ~/.curlrc

--insecure
```
