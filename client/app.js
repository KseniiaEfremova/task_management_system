const BASE_URL = 'http://127.0.0.1:5001/';
const mainList = document.querySelector('section__list-wrapper')

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

const projectElem = `<h3 class="list__elem-title">${list['title']}</h3>
                <p class="list__elem-desc">${list['project_id']}</p>
                <div class="list__elem-just-between">
                    <a href='#' data-id="update-${project.project_id}">
                        <img class="list__elem-img" src='../assets/update.png' alt='update' data-id="update-${list.project_id}"/>
                    </a>
                    <button data-id="delete-${project.project_id}" >
                        <img class="list__elem-img" src='../assets/delete.png' alt='delete' data-id="delete-${list.project_id}"/>
                    </button>
                </div>
            `


const createListElem = (listElements, elem, list) => {
     for (const listElem of listElement) {
            const listElem = document.createElement('li')
            listElem.classList.add('list__elem')
            const date = new Date(project.deadline)
            listElem.insertAdjacentHTML(
                'afterbegin', elem)
            list.append(listElem)
    }
}

const renderProjects = async () => {
    const projects = await getProjects();
    console.log(projects);
    createListElem(projects, projectElem, mainList)
}

//if (window.location.href === "http://localhost:5001/client/index.html")
renderProjects();