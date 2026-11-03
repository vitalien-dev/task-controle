
from typing import Annotated

from fastapi import APIRouter,Depends,HTTPException,status

from task_control.modules.tasks.presentation.shemas.task_schemas import TaskCreateRequest,TaskResponse
from task_control.modules.tasks.application.use_cases.create_task import CreateTask

from task_control.api.dependencies import get_create_task
router=APIRouter(
    prefix="/tasks",
    tags=["Tags"]
)


@router.post("",response_model=TaskResponse,status_code=status.HTTP_201_CREATED)
def create_task(
        payload:TaskCreateRequest,
        use_case:Annotated[CreateTask,Depends(get_create_task)]
    )->TaskResponse:

        try:

            task= use_case.execute(
                  title=payload.title,
                  description=payload.description,
                  priority=payload.priority
            )
        except ValueError as exc:
              raise HTTPException(
                    status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
                    detail=str(exc)
              ) from exc

        return TaskResponse.model_validate(task)



