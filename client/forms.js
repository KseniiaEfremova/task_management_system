const form = document.querySelector('.form__control');
const formError = document.querySelector('.form__error');
const submitButton = document.querySelector('.submit__button');
const submitProjectButton = document.querySelector('.submit__button-project')
const deleteProjectButton = document.querySelector('.list__delete-project');

const submitProject = (e) => {
    e.preventDefault();
    const projectForm = document.querySelector('.form__control-project')
    const project_id = projectForm[0].value.trim();
    if (project_id !== '') {
        formError.classList.remove('active');
        const newProject = { project_id };
        postNewProject(newProject);
         form[0].value = ''
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
    const { description, status, deadline } = taskToUpdate[0];
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

if (submitButton) submitButton.addEventListener('click', submitForm);
if (submitProjectButton) submitProjectButton.addEventListener('click', submitProject)