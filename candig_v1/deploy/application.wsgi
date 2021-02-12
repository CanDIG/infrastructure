activate_this = '/home/vagrant/candig-server-env/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from candig.server.frontend import app as application
import candig.server.frontend as frontend
frontend.configure("/srv/candig/config.py")
