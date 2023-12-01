import { postNewTask, postNewProject, updateExistingTask, getTaskById } from "./requests";

const form = document.querySelector('.form__control');
const formError = document.querySelector('.form__error');
const submitTaskButton = document.querySelector('.submit__button-task');
const submitProjectButton = document.querySelector('.submit__button-project');
const BASE_LOCATION = 'http://localhost:1234/';


const submitProject = (e) => {
    e.preventDefault();
    const projectForm = document.querySelector('.form__control-project')
    const project_name = projectForm[0].value.trim();
    if (project_name !== '') {
        formError.classList.remove('active');
        const newProject = { project_name };
        postNewProject(newProject);
        projectForm[0].value = '';
        window.location.href = BASE_LOCATION
    } else {
        formError.classList.add('active')
    }
}

const submitForm = (e) => {
    e.preventDefault();
    const description = form[0].value.trim();
    const status = form[1].value.trim();
    const deadline = form[2].value.trim();
    const project_id = form[3].value.trim();
    if (project_id !== '' && description !== '' && status !== '' && deadline !== '') {
        formError.classList.remove('active')
        if (window.location.href === BASE_LOCATION + "new_task.html") {
            const newTask = { description, status, deadline, project_id }
            postNewTask(newTask);
        } else {
            const task_id = JSON.parse(localStorage.getItem('task-id'))['task_id']
            const project_id = JSON.parse(localStorage.getItem('task-id')['project_id'])
            const taskToUpdate = {project_id, description, status, deadline, task_id }
            updateExistingTask(taskToUpdate)
        }
        form[0].value = '';
        form[1].value = '';
        form[2].value = '';
        form[3].value = '';
        window.location.href = BASE_LOCATION
    } else {
        formError.classList.add('active')
    }
}

const prepopulateForm = async (task_id, project_id) => {
    
    const taskToUpdate = await getTaskById(task_id, project_id);
    console.log(taskToUpdate)
    const { description, status, deadline } = taskToUpdate[0];
    date = new Date(deadline)
    form[0].value = description;
    form[1].value = status;
    form[2].value = date.toJSON().split('T')[0];
    form[3].value = project_id;
}

if (window.location.href === BASE_LOCATION + "update_task.html") {
    const taskFromLocal = JSON.parse(localStorage.getItem('task-id'))
    const projectFromLocal = JSON.parse(localStorage.getItem('project-id'))
    const taskToUpdateId = taskFromLocal.task_id
    const taskToUpdateProject = projectFromLocal.project_id
    prepopulateForm(taskToUpdateId, taskToUpdateProject)
}

if (submitTaskButton) submitTaskButton.addEventListener('click', submitForm);
if (submitProjectButton) submitProjectButton.addEventListener('click', submitProject)