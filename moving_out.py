import digitalocean
import json

CONFIG = 'config.json'


def move_out():
    print('We have been banned. Moving out..')

    def _get_valid_id(items):
        try:
            return items[int(input())]
        except (ValueError, IndexError):
            print('Invalid input.')
            return _get_valid_id(items)

    try:
        with open(CONFIG) as json_config:
            config = json.load(json_config)
    except json.decoder.JSONDecodeError:
        raise ValueError('Invalid config json formatting')

    do_manager = digitalocean.Manager(token=config['token'])

    try:
        region = config['region']
        name = config['name']
        size = config['size']
        image = config['image']
    except KeyError:
        print('Fix config.')
        return

    with open('deploy.sh') as f:
        user_data = f.read()

    droplet = digitalocean.Droplet(
        token=config['token'],
        region=region,
        ssh_keys=do_manager.get_all_sshkeys(),
        image=image,
        name=name,
        size=size,
        user_data=user_data
    )

    droplet.create()
