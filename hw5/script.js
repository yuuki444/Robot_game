const taskList = document.getElementById("taskList")
const addTaskBtn = document.getElementById("addTaskBtn")
const textInput = document.getElementById("textInput")

taskList.addEventListener("click", (event) => {

  if (event.target.classList.contains("delete-btn")) {
    event.target.parentElement.remove()
  }

  if (event.target.classList.contains("task_item")) {
    event.target.classList.toggle("done")
  }

  if (event.target.classList.contains("mark-btn")) {
    event.target.parentElement.classList.toggle("blue")
  }

})

addTaskBtn.addEventListener("click", () => {
  const taskText = textInput.value.trim()

  if (taskText !== "") {
    const li = document.createElement("li")
    li.className = "task_item"

    li.innerHTML = `
      ${taskText}
      <button class="delete-btn">Удалить</button>
      <button class="mark-btn">Синяя</button>
    `

    taskList.appendChild(li)
    textInput.value = ""
  }
})
