from task_management.repository.elastic_repository import ElasticRepository
from task_management.config import ES_CONFIG


class TaskManagementApp(ElasticRepository):
    """
    This class is the main class of the application. It is responsible for managing tasks.
    This class have 4 functionalitis CRUD: Create, Read, Update, and Delete task.

    Each task has a title, description, and status.
    Using Elastic Search as a repository to store the tasks.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._build_template(ES_CONFIG.PATH_TO_QUERY_TEMPLATE)

    def create_task(self, title: str, description: str, status: str):
        """
        Create a new task with the given title and description.
        """
        
        self.es.index(
            index=ES_CONFIG.INDEX_NAME,
            id=title,
            body={
                "title": title,
                "description": description,
                "status": status
            })

    def read_task(self, title: str):
        """
        Read the task with the given title.
        """
        
        task = self.es.get(index=ES_CONFIG.INDEX_NAME, id=title)
        if task:
            return task["_source"]
        else:
            return "Task not found, please check the title."

    def update_task(self, title: str, type: str, value: str):
        """
        Update the task with the given title.
        User can update the task description or status.
        """
        
        self.es.update(
            index=ES_CONFIG.INDEX_NAME,
            id=title,
            body={
                "doc": {
                    type: value
                }
            })

    def delete_task(self, title: str):
        """
        Delete the task with the given title.
        """
        
        self.es.delete(index=ES_CONFIG.INDEX_NAME, id=title)

    def show_all_tasks(self):
        """
        Show all the tasks.
        """
        
        tasks = self.es.search(index=ES_CONFIG.INDEX_NAME)
        return [task["_source"] for task in tasks["hits"]["hits"]]
