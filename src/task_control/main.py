
from fastapi import FastAPI


from task_control.modules.tasks.presentation.routes.task_routes import  router as task_route


app=FastAPI(
    title="Task controle Api",
    description= "Ceci est une api de gestion de tache multi users",
    version="0.1.0"
)   

app.include_router(task_route,prefix="/api/v1")

