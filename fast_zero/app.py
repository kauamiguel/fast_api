from fastapi import (
    FastAPI,
)
from http import (
    HTTPStatus,
)
from fast_zero.schemas import (
    Message,
    UserSchema,
    UserPublicSchema,
    UserDB,
    UserList,
)
from fastapi.responses import (
    HTMLResponse,
)

app = FastAPI()

database = []


@app.get(
    "/",
    status_code=HTTPStatus.OK,
    response_model=Message,
)
def read_root():
    return Message(
        message="Hello World"
    )


@app.get(
    "/html",
    status_code=HTTPStatus.OK,
    response_class=HTMLResponse,
)
def read_html():
    return """
    <html>
        <head>
            <title>Hello World</title>
        </head>
        <body>
            <h1>Hello World</h1>
        </body>
    </html>
    """


@app.post(
    "/users/",
    status_code=HTTPStatus.CREATED,
    response_model=UserPublicSchema,
)
def create_user(
    user: UserSchema,
):
    user_with_id = UserDB(
        id=len(
            database
        )
        + 1,
        **user.model_dump(),
    )
    return user_with_id


@app.get(
    "/users/",
    status_code=HTTPStatus.OK,
    response_model=UserList,
)
def read_users():
    return UserList(
        users=database
    )
