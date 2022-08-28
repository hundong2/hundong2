# Docker 

## Docker Command Set

1. Docker image list
    - example
  
    ```bash
    docker images
    ```

2. Docker image delete
   - docker image rm [IMAGE ID]
   - example 
    ```bash
    > docker images
    REPOSITORY                   TAG           IMAGE ID       CREATED          SIZE
    5275336a7074                 latest        119e976e6232   22 minutes ago   1.43GB
    > docker image rm 119e976e6232V
    ```

3. Docker image tag diff
    - docker tag 변경
    - docker hub에 push 할경 우 필요. 
    - 
    ```bash
    docker image tag [local_repo_name]:[TAG] [user_name]/cent_os_for_node:[new_tag]
    ```
      - local_ropo_name : REPOSITORY 
      - TAG : TAG
      - new_tag : you want to use docker hub repo name

4. docker login
    - user login to docker hub before image push to dockerhub
    - command example
    ```bash
    > docker login
    ```
5. docker commit 
    - docker commit [NAES] [REPOSITORY:TAG]