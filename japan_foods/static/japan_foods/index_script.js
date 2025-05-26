function toggle_comment_form(id) {
  const form = document.getElementById(`form_${id}`);
  const comment = document.getElementById(`comment_${id}`)
  console.log('comment is',comment)
  console.log('edit comment form is',form.id)


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


