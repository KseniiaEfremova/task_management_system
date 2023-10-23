const BASE_URL = 'http://127.0.0.1:5001/';

const getProjects = () => {
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