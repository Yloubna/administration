let all_students;
let students_pergrp;
let nb_grps;
$("#calculate").click(function() {
    console.log("button calculate clicked");
    all_students = $("#allstudents").val();
    students_pergrp = $("#students").val();
    console.log("all students : "+all_students);
    console.log("students per groupe : "+students_pergrp);
    nb_grps = Math.trunc(all_students/students_pergrp);
    console.log(nb_grps);
    for ( i = 0; i < nb_grps; i++ ) {
        console.log("create new div");
       /* $("#mycontainer").append('<div class="x_panel"> <div class="x_title"> <h2>Groupe ..</h2>  <ul class="nav navbar-right panel_toolbox"> <li><a class="collapse-link"><i class="fa fa-chevron-up"></i></a> </li> </ul> <div class="clearfix"></div> </div>  <div class="x_content"> <table class="table table-striped projects"> <thead> <tr><th style="width: 1%">#</th><th style="width: 20%">Noms</th> <th>Prénoms</th> <th>Dates de naissances</th> <th></th><th style="width: 20%">#Edit</th></tr></thead> <tbody><tr> <td>#</td> <td><a></a> <br /><small></small> </td> <td></td> <td class="project_progress">  </td><td>  </td> <td>  <a href="#" class="btn btn-primary btn-xs"><i class="fa fa-folder"></i> View </a> <a href="#" class="btn btn-info btn-xs"><i class="fa fa-pencil"></i> Edit </a> <a href="#" class="btn btn-danger btn-xs"><i class="fa fa-trash-o"></i> Delete </a>  </td> </tr> </tbody> </table> </div> </div>');
    */ }
    
})