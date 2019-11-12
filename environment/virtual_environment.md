## Virutal Environment Python di Ubuntu

Step 1: Install Virtualenv
```sh
apt-get update
apt-get install python-virtualenv
```

Step 2: Buat Virtual Environment & Install Python 3

```sh
virtualenv -p /usr/bin/python3 dir/project
```

dir = lokasi project

project = nama environment

Step 3: Activate Your Virtual Environment

```sh
cd dir/project/bin
source activate
```

atau jika berada diluar direktori

```sh
source dir/project/bin/activate
```
Jika berhasil akan tampak seperti dibawah

```sh
(project)user-ubuntu@host-ubuntu:~$
```

Menonaktifkan virtual environmnet

```sh
deactivate
```

https://www.petanikode.com/python-virtualenv/
