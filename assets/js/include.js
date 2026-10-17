document.addEventListener("DOMContentLoaded", function() {
    function loadComponent(id, file) {
        fetch(file)
            .then(response => {
                if (!response.ok) throw new Error("Could not load " + file + " (Status: " + response.status + ")");
                return response.text();
            })
            .then(data => {
                const element = document.getElementById(id);
                if (element) element.innerHTML = data;
            })
            .catch(error => console.error("Component load error:", error));
    }

    // Use absolute paths starting from the web server root
    loadComponent('site-header', '/components/header.html');
    loadComponent('site-footer', '/components/footer.html');
});