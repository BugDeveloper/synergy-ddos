import digitalocean
import json

CONFIG_PATH = 'config.json'

try:
    with open(CONFIG_PATH) as json_config:
        config = json.load(json_config)
except json.decoder.JSONDecodeError:
    raise ValueError('Invalid config json formatting')

do_manager = digitalocean.Manager(token=config['token'])


def move_out(current_droplet_id):
    create_new_droplet()
    current = do_manager.get_droplet(current_droplet_id)
    current.destroy()


def create_new_droplet():
    try:
        region = config['region']
        name = config['name']
        size = config['size']
        image = do_manager.get_all_snapshots()[0].id
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
