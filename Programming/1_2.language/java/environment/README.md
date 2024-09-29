# JAVA Environment 


## update-alternatives 

```sh
sudo update-alternatives --config java
[sudo] password for songdong: 
There are 2 choices for the alternative java (providing /usr/bin/java).

  Selection    Path                                            Priority   Status
------------------------------------------------------------
* 0            /usr/lib/jvm/java-17-openjdk-amd64/bin/java      1711      auto mode
  1            /usr/lib/jvm/java-17-openjdk-amd64/bin/java      1711      manual mode
  2            /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java   1081      manual mode

```

### setting 

```sh
sudo update-alternatives --install <link> <name> <path> <priority>
sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/~
```

Install your Java version of choice (with XX of your preferred version):
`sudo apt install openjdk-XX-jdk-headless`

List all your installed version and remember path
`sudo update-alternatives --config java`

Change to your version of choice:
`sudo update-java-alternatives --set /path/to/java/version`

## reference 

- [update-alternatives](https://choincnp.tistory.com/117)  
- [update-alternatives-stackoverflow](https://stackoverflow.com/questions/77003785/updating-jdk-openjdk-on-wsl2-to-use-with-intellij-and-versions-questions)  
- [open JDK download](https://jdk.java.net/23/)  
- [open JDK download & install each platform](https://openjdk.org/install/)  

