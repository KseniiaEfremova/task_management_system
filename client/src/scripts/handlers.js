export const BASE_LOCATION = 'http://localhost:1234/';

export const handleUpdateTask = (e) => {
    if (e.target.getAttribute('data-id').includes('update')) {
        const taskId = { task_id: +(e.target.getAttribute('data-id').slice(7)), project_id: +(e.target.getAttribute('data-id').slice(9)) };
        localStorage.setItem('task-id', JSON.stringify(taskId));
        window.location.href = BASE_LOCATION + "update_task.html"; 
    } else {
        return
    } 
}

export const handleDeleteTask = (e) => {
    if (e.target.getAttribute('data-id').includes('delete')) {
        const taskId = { task_id: +(e.target.getAttribute('data-id').slice(7)), project_id: +(e.target.getAttribute('data-id').slice(9)) }
        deleteTask(taskId);
        for (list of taskLists) {
            while (list.lastElementChild) {
                list.removeChild(list.lastElementChild);
            }
        }
       
       renderTasksByStatus();
    } else {
        return
    }
}

export const handleGetProjectTasks = (e) => {
    if (e.target.getAttribute('data-id').includes('project')) {
        const projectId = { project_id: +(e.target.getAttribute('data-id').slice(8)) };
        localStorage.setItem('project-id', JSON.stringify(projectId));
        window.location.href = BASE_LOCATION + 'tasks'; 
        return false;
    } else {
        return
    }
     
}

export const handleDeleteProject = (e) => {
        if (e.target.getAttribute('data-id').includes('delete')) {
        const projectId = { project_id: +(e.target.getAttribute('data-id').slice(7)) }
        deleteProject(projectId[project_id]);
        for (list of projectLists) {
            while (list.lastElementChild) {
                list.removeChild(list.lastElementChild);
            }
        }
       
       renderProjects();
    } else {
        return
    }
}
