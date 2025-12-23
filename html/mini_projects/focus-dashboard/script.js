// Clock
function updateClock() {
    document.getElementById("time").textContent =
        new Date().toLocaleTimeString();
}
setInterval(updateClock, 1000);
updateClock();

// Theme toggle
document.getElementById("themeBtn").onclick = () => {
    document.body.classList.toggle("light");
};

// Tasks
const input = document.getElementById("taskInput");
const list = document.getElementById("taskList");
let tasks = JSON.parse(localStorage.getItem("tasks")) || [];

function save() {
    localStorage.setItem("tasks", JSON.stringify(tasks));
}

function render() {
    list.innerHTML = "";
    tasks.forEach((t, i) => {
        const li = document.createElement("li");
        li.textContent = t;
        li.onclick = () => {
            tasks.splice(i, 1);
            save();
            render();
        };
        list.appendChild(li);
    });
}

document.getElementById("addTaskBtn").onclick = () => {
    if (!input.value.trim()) return;
    tasks.push(input.value);
    input.value = "";
    save();
    render();
};

render();
