from ariadne import MutationType
import uuid
from Data import UserDetails

mutation = MutationType()


@mutation.field('createUser')
def resolve_create_user(*_, name, id, email, username, input):
    input['name'] = name
    input['id'] = uuid.uuid4()
    input['email'] = email
    input['username'] = username
    input.update(id)
    UserDetails.append(input)
    return input


# mutation {
#     createUser(email: "david@atheros.ai", firstName: "David", lastName: "Mráz", phone: "123456789", username: "a7v8x") {
#         user {
#             id,
#             name,
#             email,
#             username,
#         }
#     }
# }
