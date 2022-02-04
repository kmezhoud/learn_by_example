function validate() 
{
	cname = document.getElementById('cname');
	pwd = document.getElementById("cpassword");
	cpwd = document.getElementById("password");
	if (cpwd.value != pwd.value) 
	{
		alert("Both Passwords must match!");
	}
}
function validate1() 
{
	rname = document.getElementById('rname');
	rpwd = document.getElementById("rpassword");
	rcpwd = document.getElementById("rcpassword");
	if (rcpwd.value != rpwd.value) 
	{
		alert("Both Passwords must match!");
	}
}
