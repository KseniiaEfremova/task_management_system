const BASE_URL = 'http://127.0.0.1:5001/';
const mainList = document.querySelector('.section__list-wrapper');
const taskLists = document.querySelectorAll('.list__wrapper');
const form = document.querySelector('.form__control');
const formError = document.querySelector('.form__error');
const submitButton = document.querySelector('.submit__button');


const getProjects = async () => {
     try {
         const response = await fetch(BASE_URL + 'projects', {
             headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Access-Control-Origin': '*',
                },})
    if (!response.ok) {
        throw new Error('Could not fetch projects!');
    }
        const projects = await response.json();
        return projects;
    } catch (err) {
        console.log(err);
    }
}

const createProjectElem = (listElem) => {
    return `<h3 class="list__elem-title">${listElem['title']}</h3>
                <p class="list__elem-desc">${listElem['project_id']}</p>
                <div class="list__elem-just-between">
                    <a href='#' data-id="update-${listElem.project_id}">
                        <img class="list__elem-img" src='./static/assets/update.png' alt='update' data-id="update-${listElem.project_id}"/>
                    </a>
                    <button data-id="delete-${listElem.project_id}" >
                        <img class="list__elem-img" src='./static/assets/delete.png' alt='delete' data-id="delete-${listElem.project_id}"/>
                    </button>
                </div>
            `}

const createTaskElem = (listElem) => {
    return        `<h3 class="list__elem-title">${listElem.description}</h3>
                <div class="list__elem-just-between">
                    <h4 class="list__elem-status">${listElem.status}</h4>
                    <p class="list__elem-date">${date.toJSON().split('T')[0]}</p>
                </div>
                <div class="list__elem-just-between">
                    <a href='#' data-id="update-${listElem.task_id}-${listElem.project_id}">
                        <img class="list__elem-img" src='../assets/update.png' alt='update' data-id="update-${listElem.task_id}-${listElem.project_id}"/>
                    </a>
                    <button data-id="delete-${listElem.task_id}-${listElem.project_id}" >
                        <img class="list__elem-img" src='../assets/delete.png' alt='delete' data-id="delete-${listElem.task_id}-${listElem.project_id}}"/>
                    </button>
                </div>
            `
}


const createListElem = (listElements, list) => {
     for (const listEl of listElements) {
        const listElem = document.createElement('li')
        listElem.classList.add('list__elem')
         if (listElements !== 'projects') {
             const date = new Date(listEl.deadline)
         }
            listElem.insertAdjacentHTML(
                'afterbegin', createProjectElem(listEl))
            list.append(listElem)
    }
}

const renderProjects = async () => {
    // const projects = await getProjects();
    // TODO: change this hardcoded data to projects pulled from db
    const projects = [{ project_id: 2, title: 'Learn Flask' }, {project_id: 1, title: 'task management system'}]
    createListElem(projects, mainList)
}

if (window.location.href === "http://127.0.0.1:5500/client/index.html") renderProjects();


const renderTasksByStatus = async () => {
    const projectId = JSON.parse(localstorage.getItem('projectId')['project_id']);
    const taskListTodo = document.querySelector('.list__wrapper-todo');
    const taskListInProgress = document.querySelector('.list__wrapper-inprogress');
    const taskListInReview = document.querySelector('.list__wrapper-inreview');
    const taskListDone = document.querySelector('.list__wrapper-done');
    const todoTasks = await getTasksByStatus(projectId, 'todo');
    const inReviewTasks = await getTasksByStatus(projectId, 'in review');
    const inProgressTasks = await getTasksByStatus(projectId, 'in progress');
    const doneTasks = await getTasksByStatus(projectId, 'done');
    if (todoTodos) {
       createListElem(todoTasks, taskListTodo)
    }
    if (inReviewTasks) {
       createListElem(inReviewTodos, taskListInReview)
    }
    if (inProgressTasks) {
       createListElem(inProgressTasks, taskListInProgress)
    }
    if (doneTasks) {
       createListElem(doneTasks, taskListDone)
    }
}


const getResponse = async (params) => {
    const { endpointUrl, method, body, errorMessage } = params
    try {
              const response = await fetch(BASE_URL + endpointUrl,
            {
                method: method,
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    "Access-Control-Origin": "*",
                },
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

const getTaskById = async (taskId, projectId) => {
    try {
        const response = await fetch(BASE_URL + `projects/${projectId}/${taskId}`, {
            headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Access-Control-Origin': '*',
                },})
    if (!response.ok) {
        throw new Error('Could not fetch this one!');
    }
        const task = await response.json();
        return task
    } catch (err) {
        console.log(err);
    }
}

const getTasksByStatus = async (status, project_id) => {
     try {
         const response = await fetch(BASE_URL + `projects/${project_id}/${status}`, {
             headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Access-Control-Origin': '*',
                },})
    if (!response.ok) {
        throw new Error('Could not fetch tasks!');
    }
        const tasks = await response.json();
        return tasks;
    } catch (err) {
        console.log(err);
    }
}

const postNewTask = (newTask) => {
    const params = {
        endpointUrl: 'new_task',
        method: 'POST',
        body: newTask,
        errorMessage: 'Could not add new task!'
    }
    getResponse(params)
}

const updateExistingTask = (taskToUpdate) => {
    const params = {
        endpointUrl: 'update_task',
        method: 'PUT',
        body: taskToUpdate,
        errorMessage: 'Could not update this task!'
    }
    getResponse(params)
}

const deleteTask = (taskId) => {
    const params = {
        endpointUrl: '/',
        method: 'DELETE',
        body: taskId,
        errorMessage: 'Could not delete todo!'
    }
    getResponse(params)
}

const submitForm = (e) => {
    e.preventDefault();
    const description = form[0].value.trim();
    const status = form[1].value.trim();
    const deadline = form[2].value.trim();
    const project_id = form[3].value.trim();
    if (project_id !== '' && description !== '' && status !== '' && deadline !== '') {
        formError.classList.remove('active')
        const newTask = { description, status, deadline, project_id }
        const task_id = JSON.parse(localStorage.getItem('task-id'))['task_id']
        const project_id = JSON.parse(localStorage.getItem('task-id')['project_id'])
        const taskToUpdate = {project_id, description, status, deadline, task_id }
        if (window.location.href === "http://localhost:5500/client/new_task.html") {
            postNewTask(newTask);
        } else {
            updateExistingTask(taskToUpdate)
        }
        form[0].value = '';
        form[1].value = '';
        form[2].value = '';
        form[3].value = '';
        window.location.href = "http://localhost:5500/client/index.html"
    } else {
        formError.classList.add('active')
    }
}

const prepopulateForm = async (task_id, project_id) => {
    const taskToUpdate = await getTaskById(task_id, project_id);
    const { project_id, description, status, deadline } = taskToUpdate[0];
    date = new Date(deadline)
    form[0].value = description;
    form[1].value = status;
    form[2].value = date.toJSON().split('T')[0];
    form[3].value = project_id;
}

if (window.location.href === "http://localhost:5500/client/update_task.html") {
    const taskToUpdateId = JSON.parse(localStorage.getItem('task-id')['task_id']);
    const taskToUpdateProject = JSON.parse(localStorage.getItem('task-id')['project_id']);
    prepopulateForm(taskToUpdateId, taskToUpdateProject)
}

const handleUpdateTask = (e) => {
    if (e.target.getAttribute('data-id').includes('update')) {
        const taskId = { task_id: +(e.target.getAttribute('data-id').slice(7)), project_id: +(e.target.getAttribute('data-id').slice(9)) };
        localStorage.setItem('task-id', JSON.stringify(taskId));
        window.location.href = "http://localhost:5500/client/update_task.html"; 
    } else {
        return
    } 
}



if (submitButton) submitButton.addEventListener('click', submitForm);