const BASE_URL = 'http://127.0.0.1:5001/';

const headers = {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    "Access-Control-Origin": "*",
                }

const getResponse = async (params) => {
    const { endpointUrl, method, body, errorMessage } = params
    try {
              const response = await fetch(BASE_URL + endpointUrl,
            {
                method: method,
                headers: headers,
                body: JSON.stringify(body),
            })    
        if (!response.ok) {
            throw new Error(errorMessage);
        }
        const data = await response.json();
        return data;
    } catch (err) {
        console.log(err);
    }
}

export const getProjects = async () => {
     try {
         const response = await fetch(BASE_URL + 'projects', {
             headers: headers})
    if (!response.ok) {
        throw new Error('Could not fetch projects!');
    }
        const projects = await response.json();
        return projects;
    } catch (err) {
        console.log(err);
    }
}


export const getTaskById = async (taskId, projectId) => {
    try {
        const response = await fetch(BASE_URL + `projects/${projectId}/${taskId}`, {
            headers: headers})
    if (!response.ok) {
        throw new Error('Could not fetch this one!');
    }
        const task = await response.json();
        return task
    } catch (err) {
        console.log(err);
    }
}

export const getTasksByStatus = async (project_id, status) => {
     try {
         const response = await fetch(BASE_URL + `projects/${project_id}/${status}`, {
             headers: headers})
    if (!response.ok) {
        throw new Error('Could not fetch tasks!');
    }
        const tasks = await response.json();
        return tasks;
    } catch (err) {
        console.log(err);
    }
}

export const postNewTask = (newTask) => {
    const params = {
        endpointUrl: 'newtask',
        method: 'POST',
        body: newTask,
        errorMessage: 'Could not add new task!'
    }
    getResponse(params)
}

export const postNewProject = (newProject) => {
     const params = {
        endpointUrl: 'new_project',
        method: 'POST',
        body: newProject,
        errorMessage: 'Could not add new project!'
    }
    getResponse(params)
}

export const updateExistingTask = (taskToUpdate) => {
    const params = {
        endpointUrl: 'update_task',
        method: 'PUT',
        body: taskToUpdate,
        errorMessage: 'Could not update this task!'
    }
    getResponse(params)
}

export const deleteTask = (taskId) => {
    const params = {
        endpointUrl: '/',
        method: 'DELETE',
        body: taskId,
        errorMessage: 'Could not delete todo!'
    }
    getResponse(params)
}

export const deleteProject = (projectId) => {
    const params = {
        endpointUrl: '/delete',
        method: 'DELETE',
        body: projectId,
        errorMessage: 'Could not delete this project!'
    }
    getResponse(params)
}