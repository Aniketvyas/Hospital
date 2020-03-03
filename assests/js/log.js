function validateForm() {
  var x = document.forms["myForm"]["first_name"].value;
  var y = document.forms["myForm"]["last_name"].value;
  var z = document.forms["myForm"]["email"].value;
  var w = document.forms["myForm"]["password"].value;
  var v = document.forms["myForm"]["password1"].value;
  if (x == "") {
    //alert("Please Enter a Valid  first Name");
    return false;
  }
  if( y == ""){
    //alert("please Enter a Valid Last name");
    return false;
  }
  atpos = z.indexOf("@");
  dotpos = z.lastIndexOf(".");
         
  if (atpos < 1 || ( dotpos - atpos < 2 )) {
    //alert("Please enter correct email ID");
      document.myForm.z.focus() ;
      return false;
    }
}
  if(password==password1){
    //alert("Enter a valid password");
    return false;
  }
  alert("Please Enter Valid Credentiasl");
  return true;
}