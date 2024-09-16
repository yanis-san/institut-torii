import sys
import os

# Chemin vers le répertoire contenant votre projet Django
project_home = '/home/fyxszahz/institut-torii'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Définir la variable d'environnement pour le fichier de configuration Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

# Définir le chemin du fichier de journalisation de Passenger
log_file_path = '/home/fyxszahz/logs/passenger.log'
if not os.path.exists(os.path.dirname(log_file_path)):
    os.makedirs(os.path.dirname(log_file_path))

os.environ['PASSENGER_LOG_FILE'] = log_file_path

# Importer l'application WSGI de Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()