function getId(url) {
    const regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|&v=)([^#&?]*).*/;
    const match = url.match(regExp);

    return (match && match[2].length === 11)
      ? match[2]
      : null;
}

figure = document.querySelectorAll('figure[class="media"]')

document.querySelectorAll('oembed[url]').forEach((element, x) => {
  figure[x].innerHTML = ''
  let video_id = getId(element.attributes.url.value);

  let iframe = '<div class="embed-responsive embed-responsive-16by9"><iframe class="embed-responsive-item" src="//www.youtube.com/embed/'
  + video_id + '" frameborder="0" allowfullscreen></iframe></div>';
  figure[x].innerHTML = iframe
});



(function () {

  function truncateString(str, num) {

    if (str.length <= num) {
      return str
    }
    return str.slice(0, num) + '...'
  }

  let state = {
    'posts': [],
    'values': []
  }

  $.ajax({
    method: 'GET',
    url: 'api/',
    success: (res) => {

      for(let i in res){

        let key = Object.keys(res[i]);
        let value = Object.values(res[i]);

        state.posts.push(truncateString(value[0], 6))
        state.values.push(value[1])
      }

      chart_customization()
    },
    error: (err) => {
      console.log(err);
    }
  })

  function chart_customization() {

    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: state.posts,
            datasets: [{
                label: '# of Votes',
                data: state.values,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });

  }

})()
