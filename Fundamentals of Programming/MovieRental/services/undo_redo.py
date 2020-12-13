from dataclasses import dataclass
from exception.errors import EmptyError

@dataclass
class UndoOperation:
    source_object: object
    handler: object
    parameters: object


class UndoRedoManager:
    __undo_operations = []
    __redo_operations = []

    @staticmethod
    def add_undo_operation(source_object, handler, *parameters):
        UndoRedoManager.__undo_operations.append(UndoOperation(source_object, handler, parameters))

    @staticmethod
    def add_redo_operation(operation):
        UndoRedoManager.__redo_operations.append(operation)

    @staticmethod
    def redo():
        if not UndoRedoManager.__redo_operations:
            raise EmptyError('There is nothing to redo.')

        redo_operation = UndoRedoManager.__redo_operations.pop()
        opposite_operation = redo_operation.handler(redo_operation.source_object, *redo_operation.parameters)
        UndoRedoManager.add_undo_operation(opposite_operation.source_object, opposite_operation.handler, *opposite_operation.parameters)
    @staticmethod
    def undo():
        if not UndoRedoManager.__undo_operations:
            raise EmptyError('There is nothing to undo.')

        undo_operation = UndoRedoManager.__undo_operations.pop()
        opposite_operation = undo_operation.handler(undo_operation.source_object, *undo_operation.parameters)
        UndoRedoManager.add_redo_operation(opposite_operation)

