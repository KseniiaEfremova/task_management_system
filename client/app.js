const BASE_URL = 'http://127.0.0.1:5001/';
const mainList = document.querySelector('.section__list-wrapper');


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

const postNewTask = (newTask) => {
    const params = {
        endpointUrl: 'new_task',
        method: 'POST',
        body: newTask,
        errorMessage: 'Could not add new todo!'
    }
    getResponse(params)
}