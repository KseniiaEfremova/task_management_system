import { getProjects, getTasksByStatus } from './requests';
import { handleGetProjectTasks, handleDeleteProject, handleDeleteTask, handleUpdateTask } from './handlers';
const mainList = document.querySelector('.section__list-wrapper');
const taskLists = document.querySelectorAll('.list__wrapper');
const deleteProjectButton = document.querySelector('.list__delete-project');
const BASE_LOCATION = 'http://localhost:1234/';


const createProjectElem = (listElem) => {
    return `
                <h3 class="list__elem-title">${listElem['project_name']}</h3>
                <p class="list__elem-desc">${listElem['project_id']}</p>
                <div class="list__elem-just-between">
                    <button data-id="delete-${listElem.project_id}" class="list__delete-project">
                        <img class="list__elem-img" src='/delete.8dd9e795.png' alt='delete' data-id="delete-${listElem.project_id}" class="list__delete-project"/>
                    </button>
                      <button data-id="project-${listElem.project_id}" type="button">
                        <img class="list__elem-img" src='/update.eaa90a6d.png' alt='update' data-id="project-${listElem.project_id}"/>
                    </button>
                </div>
            </a>
            `}


const createTaskElem = (listElem, date) => {
    return  `<h3 class="list__elem-title">${listElem.description}</h3>
                <div class="list__elem-just-between">
                    <h4 class="list__elem-status">${listElem.status}</h4>
                    <p class="list__elem-date">${date.toJSON().split('T')[0]}</p>
                </div>
                <div class="list__elem-just-between">
                    <a href='#' data-id="update-${listElem.task_id}-${listElem.project_id}">
                        <img class="list__elem-img" src='update.eaa90a6d.png' alt='update' data-id="update-${listElem.task_id}-${listElem.project_id}"/>
                    </a>
                    <button data-id="delete-${listElem.task_id}-${listElem.project_id}" >
                        <img class="list__elem-img" src='delete.8dd9e795.png' alt='delete' data-id="delete-${listElem.task_id}-${listElem.project_id}"/>
                    </button>
                </div>
            `
}

const createListElem = (listElements, list) => {
     for (const listEl of listElements) {
        const listElem = document.createElement('li')
        listElem.classList.add('list__elem')
         if (window.location.href === BASE_LOCATION) {
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
    const projects = await getProjects();
    createListElem(projects, mainList)
}

const renderTasksByStatus = async () => {
    const projectId = JSON.parse(localStorage.getItem('project-id'))['project_id'];
    const taskListTodo = document.querySelector('.list__wrapper-todo');
    const taskListInProgress = document.querySelector('.list__wrapper-inprogress');
    const taskListInReview = document.querySelector('.list__wrapper-inreview');
    const taskListDone = document.querySelector('.list__wrapper-done');
    const todoTasks = await getTasksByStatus(projectId, 'todo');
    const inReviewTasks = await getTasksByStatus(projectId, 'in review');
    const inProgressTasks = await getTasksByStatus(projectId, 'in progress');
    const doneTasks = await getTasksByStatus(projectId, 'done');
    if (todoTasks) {
       createListElem(todoTasks, taskListTodo)
    }
    if (inReviewTasks) {
       createListElem(inReviewTasks, taskListInReview)
    }
    if (inProgressTasks) {
       createListElem(inProgressTasks, taskListInProgress)
    }
    if (doneTasks) {
       createListElem(doneTasks, taskListDone)
    }
}

if (window.location.href === BASE_LOCATION) renderProjects();
if (window.location.href === BASE_LOCATION + 'tasks') renderTasksByStatus();

if (taskLists) taskLists.forEach((list) => list.addEventListener('click', handleDeleteTask));
if (taskLists) taskLists.forEach((list) => list.addEventListener('click', handleUpdateTask));
if (deleteProjectButton) deleteProjectButton.addEventListener('click', handleDeleteProject);
if (mainList && window.location.href === BASE_LOCATION )mainList.addEventListener('click', handleGetProjectTasks)