from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)

from task_control.api.dependencies import get_create_user

from task_control.modules.identity.application.use_cases.create_user import (
    CreateUser,
)

from task_control.modules.identity.domain.exceptions import (
    EmailAlreadyRegistered,
)

from task_control.modules.identity.presentation.schemas.user_schemas import (
    UserCreateRequest,
    UserResponse,
)



router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    payload: UserCreateRequest,
    use_case: Annotated[
        CreateUser,
        Depends(get_create_user),
    ],
) -> UserResponse:

    try:

        user = use_case.execute(
            email = str(payload.email),
            password = str(payload.password)
        )

    except EmailAlreadyRegistered as exc:

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        ) from exc

    except ValueError as exc:

        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(exc),
        ) from exc

    return UserResponse(
        id=user.id,
        email=user.email,
    )