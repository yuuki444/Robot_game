const commentInput = document.getElementById("commentInput");
const commentBtn = document.getElementById("commentBtn");
const commentError = document.getElementById("commentError");
const commentResult = document.getElementById("commentResult");

commentBtn.addEventListener("click", () => {
    const comment = commentInput.value.trim();

    commentError.textContent = "";
    commentResult.textContent = "";

    if (comment === "") {
        commentError.textContent = "комментарий не может быть пустым";
        return;
    }

    if (comment.length < 5) {
        commentError.textContent = "комментарий слишком короткий";
        return;
    }

    if (comment.length > 50) {
        commentError.textContent = "комментарий слишком длинный";
        return;
    }

    commentResult.textContent = comment;

    commentInput.value = "";
});
