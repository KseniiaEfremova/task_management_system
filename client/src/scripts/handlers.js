import { deleteTask, deleteProject, getProjects } from './requests';
import { BASE_LOCATION, taskLists, mainList } from './utils';

export const BASE_LOCATION = 'http://localhost:1234/';
export const mainList = document.querySelector('.section__list-wrapper');
export const taskLists = document.querySelectorAll('.list__wrapper');

export const createProjectElem = (listElem) => {
    return `
                <h3 class="list__elem-title">${listElem['project_name']}</h3>
                <p class="list__elem-desc">${listElem['project_id']}</p>
                <div class="list__elem-just-between">
                    <button data-id="delete-${listElem.project_id}">
                        <img class="list__elem-img" src='/delete.8dd9e795.png' alt='delete' data-id="delete-${listElem.project_id}" />
                    </button>
                      <button data-id="project-${listElem.project_id}" type="button">
                        <img class="list__elem-img" src='/update.eaa90a6d.png' alt='update' data-id="project-${listElem.project_id}"/>
                    </button>
                </div>
            </a>
            `}

export const createListElem = (listElements, list) => {
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
        console.log(list)    
        list.append(listElem)
    }
}

export const renderTasksByStatus = async () => {
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

export const renderProjects = async () => {
    const projects = await getProjects();
    createListElem(projects, mainList)
}

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
        const taskId = { task_id: +(e.target.getAttribute('data-id').slice(7)) }
        deleteTask(taskId['task_id']);
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
        window.location.href = BASE_LOCATION + 'tasks.html'; 
        console.log(projectId)
    } else {
        return
    } 
}

export const handleDeleteProject = (e) => {
    if (e.target.getAttribute('data-id').includes('delete')) {
        const projectId = { project_id: +(e.target.getAttribute('data-id').slice(7)) }
        deleteProject(projectId['project_id']);
        const projectLists = mainList.childNodes;
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
