import graphene
from board.schema import BoardQuery, BoardCreate, BoardDelete, BoardUpdate

class Query(
    BoardQuery,
    ):
    pass

class Mutations(graphene.ObjectType):
    board_create = BoardCreate.Field()
    board_delete = BoardDelete.Field()
    board_update = BoardUpdate.Field()

schema = graphene.Schema(
    query=Query,
    mutation=Mutations
)