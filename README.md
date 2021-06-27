# Welcome to Weasyl!

[Weasyl][] is a social gallery website designed for artists, writers, musicians, and more to share their work with other artists and fans. We seek to bring the creative world together in one easy to use, friendly, community website.


## Starting a Weasyl development environment

Requirements:

- [Docker][docker]
- [docker-compose][] (included with Docker on Windows and macOS)


[docker]: https://docs.docker.com/get-docker/
[docker-compose]: https://docs.docker.com/compose/install/


### Get the sample database

Save https://pypi.weasyl.dev/02-weasyl-latest-staff.sql.gz into the `containers/postgres/` directory.


### Configure services

This copies the sample configuration into the `config` volume, and only needs to be done each time the volume is recreated or the sample configuration changes.

```shell
./wzl configure
```


### Run database migrations

```shell
./wzl migrate
```

Future changes to migrations can be applied with `./wzl migrate --build`.


### Copy assets

```shell
./wzl assets
```

Future changes to assets can be applied with `./wzl assets --build`.


### Start Weasyl

Start all the remaining Weasyl services in the background:

```shell
./wzl up -d
```

Future changes to the application server can be applied with `./wzl up -d --build web`.

You can check its logs with `./wzl logs web`, or attach to it with `./wzl up web`. Detaching can be done from another shell with `pkill -x -HUP docker-compose`.


### Configure the `weasyl` hostname

Add this entry to `/etc/hosts`:

```
127.0.0.1 weasyl
```

Weasyl should now be running at <http://weasyl:8080/>!


## Running tests

```shell
./wzl test --build
```


## Making migrations

```shell
./wzl revision --autogenerate -m 'Revision summary'
```


## Troubleshooting and getting help

If you have questions or get stuck, you can trying talking to Weasyl project members in the project’s [Gitter room](https://gitter.im/Weasyl/weasyl).


## Code of conduct

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.


## Style guide

When committing code, be sure to follow the [Style and Best Practices Guide](STYLE_GUIDE.md).


[Weasyl]: https://www.weasyl.com/
