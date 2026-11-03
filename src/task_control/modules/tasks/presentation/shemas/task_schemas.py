from pydantic import Field , BaseModel , ConfigDict

from task_control.modules.tasks.domain.entities import TaskStatus,Priority


class TaskCreateRequest(BaseModel):
    title:str = Field(min_length=3,max_length=120)

    description:str=Field( default="",max_length=2000)

    priority:Priority=Field(default=Priority.MEDIUM)


class TaskResponse(BaseModel):

    id:int
    title:str
    description:str 
    priority:Priority
    status:TaskStatus

    model_config=ConfigDict(from_attributes=True)


