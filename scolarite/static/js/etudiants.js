$(function () {

    /* Functions */
  
    var loadForm = function () {
      var btn = $(this);
      $.ajax({
        url: btn.attr("data-url"),
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-etudiant").modal("show");
        },
        success: function (data) {
          $("#modal-etudiant .modal-content").html(data.html_form);
        }
      });
    };
  
    var saveForm = function () {
      var form = $(this);
      $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
          if (data.form_is_valid) {
            $("#mytable tbody").html(data.liste);
            $("#modal-etudiant").modal("hide");
          }
          else {
            $("#modal-etudiant .modal-content").html(data.form);
          }
        }
      });
      return false;
    };
  
  
    /* Binding */
  
    // Create book
    $(".js-create-etudiant").click(loadForm);
    $("#modal-etudiant").on("submit", ".js-etudiant-create-form", saveForm);
  
    // Update book
    $("#mytable").on("click", ".js-update-book", loadForm);
    $("#modal-etudiant").on("submit", ".js-book-update-form", saveForm);
  
  });
