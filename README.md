# docker_django_project

## 测试Docker的小Django项目，只保留最基本功能供docker学习测试使用

## 使用方法

>       1. 首先确保服务器上安装了docker及docker-compose

>       2. 确认使用本GitHub中的dockerfile项目创建好了两个相应的基础镜像fanghao/ubuntu_python:1.0和fanghao/ubuntu_django:1.0

>       3. 确保宿主机的git可用

>       4. 创建项目目录

```
cd /home
mkdir -p data/docker/docker_django_project/project
mkdir -p data/docker/docker_django_project/logs
mkdir -p data/docker/docker_django_project/venv
(创建时如果提示权限不足，请尝试使用sudo，创建完成后注意修改文件夹的权限)
```

>       5. clone代码到/home/data/docker/docker_django_project/project下，并cd至项目文件etc目录下

>       6. 创建容器：docker-compose up -d
