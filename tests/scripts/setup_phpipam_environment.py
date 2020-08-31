#!/usr/bin/env python

import docker


class PhpipamBaseContainer():
    container_specs = [
        dict(
            name="phpIPAM",
            image="phpipam/phpipam-www",
            detach=True,
        ),
        dict(
            name="phpIPAM-db",
            image="mysql",
            detach=True,
        ),
    ]


class PhpipamEnvironment(PhpipamBaseContainer):
    def __init__(self, **kwargs):
        self.container_specs = self.container_specs + kwargs.pop('container_specs', [])
        self.docker_client = docker.from_env()

        for idx, container in enumerate(self.container_specs):
            self._pull_image(image=container['image'])

    def deploy_phpipam(self):
        self._create_network()
        for idx, container in enumerate(self.container_specs):
            self._spawn_container()

    def _pull_image(self, **kwargs):
        _image_name = kwargs.get('image')
        _image_tag = kwargs.get('tag', 'latest')
        self.docker_client.images.pull(repository=_image_name, tag=_image_tag)

    def _create_network(self, **kwargs):
        print("create docker network")

    def _delete_network(self, **kwargs):
        pass

    def _spawn_container(self, **kwargs):
        print("spawn docker container ")

    def _stop_container(self, **kwargs):
        pass

    def _delete_container(self, **kwargs):
        pass


def main():
    p = PhpipamEnvironment()
    p.deploy_phpipam()


if __name__ == "__main__":
    main()
