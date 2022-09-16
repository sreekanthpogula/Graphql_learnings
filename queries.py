from ariadne import QueryType


query = QueryType()


@query.field("")
async def resolve_messages(*_):
    pass
