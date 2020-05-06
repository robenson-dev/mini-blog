

$(document).ready( async() => {
 await console.log('hello world ');

})
$.ajax({
  method: 'GET',
  url: 'api/',
  success: (data) => {
    console.log(data);
  },
  error: (err) => {
    console.log(err);
  }
})
