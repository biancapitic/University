from UI.App import UI
from Service.Service import Service

service = Service()
ui = UI(service)
ui.run_app()