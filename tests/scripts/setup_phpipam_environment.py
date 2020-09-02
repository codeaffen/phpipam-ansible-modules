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

class PhpipamBaseContainerNetwork():
    container_network_specs = [
        dict(
            name="phpipam_database",
        ),
    ]


class PhpipamEnvironment(PhpipamBaseContainer, PhpipamBaseContainerNetwork):
    def __init__(self, **kwargs):
        self.container_specs = self.container_specs + kwargs.pop('container_specs', [])
        self.container_network_specs = self.container_network_specs + kwargs.pop('container_network_specs', [])
        self.docker_client = docker.from_env()

    def deploy_phpipam(self):
        for container in self.container_specs:
            self._pull_image(image=container['image'])

        for network in self.container_network_specs:
            self._create_network(name=network['name'])

        for container in self.container_specs:
            self._spawn_container()

    def _pull_image(self, **kwargs):
        _image_name = kwargs.get('image')
        _image_tag = kwargs.get('tag', 'latest')
        self.docker_client.images.pull(repository=_image_name, tag=_image_tag)

    def _get_network(self, **kwargs):
        _network_name = kwargs.get('name')
        return self.docker_client.networks.list(names=_network_name)

    def _create_network(self, **kwargs):
        _network_name = kwargs.get('name')
        _network_driver = kwargs.get('driver', 'bridge')
        _network_exists = self._get_network(name=_network_name)
        if not _network_exists:
            self.docker_client.networks.create(name=_network_name, driver=_network_driver)

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
