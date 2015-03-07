# This bootstraps the settings.
# Do not insert anything in here. Use the conf package instead.
import yaml


CONF = yaml.load(open('/etc/citra-web/settings.yaml'))

if CONF['environment'] == 'local':
    from .conf.local import *
elif CONF['environment'] == 'staging':
    from .conf.staging import *
elif CONF['environment'] == 'production':
    from .conf.production import *
else:
    raise Exception('Could not determine environment.')
