function toggle_comment_form(id) {
  const form = document.getElementById(`form_${id}`);
  const comment = document.getElementById(`comment_${id}`)



  if (form.style.display === "none") {
    form.style.display = "block";
  } else {
    form.style.display = "none";
  }

      if (comment.style.display === "block") {
    comment.style.display = "none";
  }
    else {
    comment.style.display = "block";
  }
}

function toggleDeleteComment(id) {
  const form = document.getElementById(`delete_comment_form${id}`)
  const comment = document.getElementById(`comment_${id}`)
  const delete_icon = document.getElementById(`delete-icon${id}`)


    if (form.style.display === "none") {
    form.style.display = "block";
  } else {
    form.style.display = "none";
  }

      if (comment.style.display === "block") {
    comment.style.display = "none";
    delete_icon.style.display = 'none';
  }
    else {
    comment.style.display = "block";
    delete_icon.style.display = 'block';
  }
  
}



