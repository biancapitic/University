from enum import Enum
from services.undo_redo import UndoOperation
import copy


def add_entity_handler(service, *parameters):
    entity = copy.deepcopy(parameters[0])
    service[0].remove_by_id(parameters[0].id)
    rentals_list = []
    if len(service) > 1:
        for rental in parameters[1]:
            rentals_list.append(rental)
            service[1].remove_by_id(rental.id)
    opposite_operation = UndoOperation(service, UndoHandler.DELETE_ENTITY_HANDLER, [entity] + [rentals_list])
    return opposite_operation


def delete_entity_handler(service, *parameters):
    if hasattr(parameters[0], 'title'):
        service[0].add_movie(parameters[0].id, parameters[0].title, parameters[0].description, parameters[0].genre)
    elif hasattr(parameters[0], 'name'):
        service[0].add_client(parameters[0].id, parameters[0].name)
    else:
        service[0].add_rental(parameters[0].id, parameters[0].movie_id, parameters[0].client_id,
                              parameters[0].rented_date,
                              parameters[0].due_date, parameters[0].returned_date, 'undo')
    if len(service) > 1:
        for rental in parameters[1]:
            service[1].add_rental(rental.id, rental.movie_id, rental.client_id, rental.rented_date, rental.due_date,
                                  rental.returned_date, 'undo')
        opposite_operation = UndoOperation([service[0], service[1]], UndoHandler.ADD_ENTITY_HANDLER,
                                           [service[0].get_element_by_id(parameters[0].id), parameters[1]])
    else:
        opposite_operation = UndoOperation([service[0]], UndoHandler.ADD_ENTITY_HANDLER,
                                           [service[0].get_element_by_id(parameters[0].id)])
    return opposite_operation


def return_movie_handler(service, *parameters):
    element_id = parameters[0]
    opposite_operation = UndoOperation(service, UndoHandler.REDO_RETURN_MOVIE_HANDLER, [element_id,
                                                                                        service.get_list_of_rentals()[parameters[0]].returned_date])
    new_element = copy.deepcopy(service.get_list_of_rentals()[parameters[0]])
    new_element.returned_date = ''
    service.replace_element_with_id_given(element_id, new_element)
    return opposite_operation


def redo_return_movie_handler(service, *parameters):
    element_id = parameters[0]
    opposite_operation = UndoOperation(service, UndoHandler.RETURN_MOVIE_HANDLER, [element_id])
    redo_element = copy.deepcopy(service.get_list_of_rentals()[element_id])
    redo_element.returned_date = parameters[1]  # the returned date from the opposite
    service.replace_element_with_id_given(element_id, redo_element)
    return opposite_operation


def update_entity_handler(service, *parameters):
    entity = parameters[0]
    id_entity = parameters[1]
    old_entity = copy.deepcopy(service.get_element_by_id(id_entity))
    opposite_operation = UndoOperation(service, UndoHandler.UPDATE_ENTITY_HANDLER, [old_entity, id_entity])
    service.replace_element_with_id_given(id_entity, entity)
    return opposite_operation


class UndoHandler(Enum):
    ADD_ENTITY_HANDLER = add_entity_handler
    DELETE_ENTITY_HANDLER = delete_entity_handler
    RETURN_MOVIE_HANDLER = return_movie_handler
    REDO_RETURN_MOVIE_HANDLER = redo_return_movie_handler
    UPDATE_ENTITY_HANDLER = update_entity_handler
