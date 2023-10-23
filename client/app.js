const mainList = document.querySelector('.section__list-wrapper');
const taskLists = document.querySelectorAll('.list__wrapper');

const createProjectElem = (listElem) => {
    return `<h3 class="list__elem-title">${listElem['title']}</h3>
                <p class="list__elem-desc">${listElem['project_id']}</p>
                <div class="list__elem-just-between">
                    <button data-id="delete-${listElem.project_id}" class="list__delete-project">
                        <img class="list__elem-img" src='./static/assets/delete.png' alt='delete' data-id="delete-${listElem.project_id} class="list__delete-project""/>
                    </button>
                </div>
            `}

const createTaskElem = (listElem, date) => {
    return  `<h3 class="list__elem-title">${listElem.description}</h3>
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
         if (window.location.href === "http://127.0.0.1:5500/client/index.html") {
            listElem.insertAdjacentHTML(
                'afterbegin', createProjectElem(listEl))
         } else {
            const date = new Date(listEl.deadline)
            listElem.insertAdjacentHTML(
                'afterbegin', createTaskElem(listEl, date))
         }
            
        list.append(listElem)
    }
}

const renderProjects = async () => {
    // const projects = await getProjects();
    // TODO: change this hardcoded data to projects pulled from db
    const projects = [{ project_id: 2, title: 'Learn Flask' }, {project_id: 1, title: 'task management system'}]
    createListElem(projects, mainList)
}

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

if (window.location.href === "http://127.0.0.1:5500/client/index.html") renderProjects();
if (window.location.href === "http://127.0.0.1:5500/client/tasks.html") renderTasksByStatus();

if (taskLists) taskLists.forEach((list) => list.addEventListener('click', handleDeleteTask));
if (taskLists) taskLists.forEach((list) => list.addEventListener('click', handleUpdateTask));
if (deleteProjectButton) deleteProjectButton.addEventListener('click', handleDeleteProject);