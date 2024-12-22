$(document).ready(function()
{
    // Пример данных задач
    const tasks = [
      { id: 1, title: "Задача 1", deadline: "2024-03-10", project: "Проект А", members: ["Иван", "Петр"], comments: [], access: "public" },
      { id: 2, title: "Задача 2", deadline: "2024-11-15", project: "Проект Б", members: ["Мария", "Анна"], comments: [], access: "private" }
    ];
  
    // Функция для отрисовки задач на странице
    function renderTasks() {
      $("#past-tasks").empty();
      $("#today-tasks").empty();
      $("#future-tasks").empty();
  
      tasks.forEach(task => {
        const now = new Date();
        const deadline = new Date(task.deadline);
        const listId = deadline < now ? "past-tasks" : (deadline.getDate() === now.getDate() ? "today-tasks" : "future-tasks");
        const listItem = `<li class="list-group-item task-item" data-task-id="${task.id}">
                          <div class="form-check form-check-inline">
                            <input class="form-check-input" type="checkbox" id="task-checkbox-${task.id}">
                            <input class="form-control", placeholder="${task.title}">
                          </div>
                        </li>`;
                        
        $(`#${listId}`).append(listItem);

        $(document).on("click", ".task-item", function() 
        {
          const taskId = tasks.id
      
          // Заполнение модального окна данными задачи
          $("#taskModalLabel").text("Название: "+ task.title);
          $("#task-deadline").text("Дата: "+ task.deadline);
          $("#task-project").text("Проект: "+ task.project);
          $("#task-members").text("Участники: "+ task.members.join(", "));
          $("#task-comments").empty();
          task.comments.forEach(comment => {
            $("#task-comments").append(`<li class="list-group-item">${comment}</li>`);
          });
          $("#task-comment").val("");
          $("#task-access").val(task.access);
      
          // Открытие модального окна
          $("#taskModal").modal("show");
        });
      });
    }
  
  
    // Сохранение комментария
    $("#save-comment").click(function() {
      const taskId = $(".task-item.active").data("taskId");
      const comment = $("#task-comment").val();
      const access = $("#task-access").val();
  
      const task = tasks.find(t => t.id === taskId);
      task.comments.push(comment);
      task.access = access;
  
      // Обновление отображения комментариев
      $("#task-comments").append(`<li class="list-group-item">${comment}</li>`);
      $("#task-comment").val("");
  
      // Закрытие модального окна
      $("#taskModal").modal("hide");
    });
  
    // Обработка изменения состояния чекбокса
    $(document).on("change", ".form-check-input", function() {
      const taskId = $(this).closest(".task-item").data("taskId");
      const taskText = $(this).closest(".task-item").find(".task-text");
  
      if ($(this).is(":checked")) {
        taskText.addClass("text-dark"); // Темный текст
      } else {
        taskText.removeClass("text-dark"); // Стандартный текст
      }
    });

    $(document).on("click", ".form-check-input", function() {
        const taskId = $(this).closest(".task-item").data("taskId");
        const taskText = $(this).closest(".task-item").find(".task-text");
      
        if ($(this).is(":checked")) {
         taskText.addClass("text-dark"); // Темный текст
        } else {
         taskText.removeClass("text-dark"); // Стандартный текст
        }
       });
  
    // Отрисовка задач при загрузке страницы
    renderTasks();


  }

);


