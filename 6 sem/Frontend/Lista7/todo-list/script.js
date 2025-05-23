// Wybrałem podejście z tablicą i renderowaniem, bo ułatwia ono zarządzanie stanem aplikacji i pozwala na czyste, łatwe do debugowania operacje na tablicy.

const todoForm = document.getElementById("add-todo-form");
const todoInput = todoForm.querySelector("input[name='todo-name']");
const todoList = document.getElementById("todo-list");
const clearBtn = document.getElementById("todos-clear");
const countSpan = document.getElementById("count");

let todos = [];

function render() {
  todoList.innerHTML = "";
  todos.forEach((todo, index) => {
    const li = document.createElement("li");
    li.className = "todo__container";
    if (todo.completed) li.classList.add("todo__container--completed");
    li.innerHTML = `
      <div class="todo-element todo-name">${todo.name}</div>
      <button class="todo-element todo-button move-up">↑</button>
      <button class="todo-element todo-button move-down">↓</button>
      <button class="todo-element todo-button">${todo.completed ? "Revert" : "Done"}</button>
      <button class="todo-element todo-button">Remove</button>`;

    const [upBtn, downBtn, toggleBtn, removeBtn] = li.querySelectorAll(".todo-button");

    upBtn.addEventListener("click", () => {
      if (index > 0) {
        [todos[index - 1], todos[index]] = [todos[index], todos[index - 1]];
        render();
      }
    });

    downBtn.addEventListener("click", () => {
      if (index < todos.length - 1) {
        [todos[index + 1], todos[index]] = [todos[index], todos[index + 1]];
        render();
      }
    });

    toggleBtn.addEventListener("click", () => {
      todo.completed = !todo.completed;
      render();
    });

    removeBtn.addEventListener("click", () => {
      todos.splice(index, 1);
      render();
    });
  });

  updateCount();
}

function updateCount() {
  const remaining = todos.filter((t) => !t.completed).length;
  countSpan.textContent = remaining;
}

// New todo
todoForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const name = todoInput.value.trim();
  if (name !== "") {
    todos.push({ name, completed: false });
    todoInput.value = "";
    render();
  }
});

// Clear all
clearBtn.addEventListener("click", () => {
  todos = [];
  render();
});

// Initial load with example items
window.addEventListener("DOMContentLoaded", () => {
  todos = [
    { name: "Buy milk", completed: false },
    { name: "Go to the gym", completed: true },
    { name: "Read a book", completed: false },
    { name: "Write code", completed: true },
    { name: "Walk the dog", completed: false },
    {
      name:
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris vel metus sed justo vehicula rutrum vel ut est. Maecenas a dictum nunc. Proin congue libero risus, et lobortis purus venenatis eu. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Morbi pulvinar ullamcorper tortor, quis cursus quam.",
      completed: false,
    },
  ];
  render();
});
