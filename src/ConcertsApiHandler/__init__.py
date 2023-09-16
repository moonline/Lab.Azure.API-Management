import logging
import json

import azure.functions as func

from .controller.concerts_controller import ConcertsController
from .repository.concerts_repository import ConcertsRepository


repository = ConcertsRepository()
controller = ConcertsController(repository)


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    body = {}
    try:
        body = req.get_json()
    except ValueError:
        pass

    parameters = {
        **req.params,
        **body
    }

    return controller.get_concerts_action(parameters, {})
